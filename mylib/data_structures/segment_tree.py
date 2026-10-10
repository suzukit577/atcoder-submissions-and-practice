"""Segment Tree。"""

from collections.abc import Callable, Sequence
from typing import Generic, TypeVar

T = TypeVar("T")


class SegmentTree(Generic[T]):
    """モノイドに対する一点更新・区間積を管理するデータ構造。"""

    def __init__(
        self,
        values: Sequence[T],
        operator: Callable[[T, T], T],
        identity: T,
    ) -> None:
        self._length = len(values)
        self._operator = operator
        self._identity = identity
        self._size = 1
        while self._size < self._length:
            self._size <<= 1
        self._data = [identity] * (2 * self._size)
        self._data[self._size : self._size + self._length] = values
        for index in range(self._size - 1, 0, -1):
            self._update(index)

    def __len__(self) -> int:
        return self._length

    def set(self, index: int, value: T) -> None:
        """indexの値をvalueへ更新する。計算量はO(log N)。"""
        self._validate_index(index)
        index += self._size
        self._data[index] = value
        while index > 1:
            index >>= 1
            self._update(index)

    def get(self, index: int) -> T:
        """indexの値を返す。計算量はO(1)。"""
        self._validate_index(index)
        return self._data[self._size + index]

    def prod(self, left: int, right: int) -> T:
        """半開区間[left, right)の積を返す。計算量はO(log N)。"""
        if not 0 <= left <= right <= self._length:
            raise IndexError("invalid range")
        left += self._size
        right += self._size
        left_result = self._identity
        right_result = self._identity
        while left < right:
            if left & 1:
                left_result = self._operator(left_result, self._data[left])
                left += 1
            if right & 1:
                right -= 1
                right_result = self._operator(self._data[right], right_result)
            left >>= 1
            right >>= 1
        return self._operator(left_result, right_result)

    def all_prod(self) -> T:
        """全要素の積を返す。計算量はO(1)。"""
        return self._data[1]

    def _update(self, index: int) -> None:
        self._data[index] = self._operator(
            self._data[index << 1], self._data[index << 1 | 1]
        )

    def _validate_index(self, index: int) -> None:
        if not 0 <= index < self._length:
            raise IndexError("index is out of range")
