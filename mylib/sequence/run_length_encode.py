"""ランレングス圧縮。"""

from collections.abc import Iterable
from itertools import groupby
from typing import TypeVar

T = TypeVar("T")


def run_length_encode(values: Iterable[T]) -> list[tuple[T, int]]:
    """連続する同一要素を(要素, 個数)へ圧縮する。

    要素数をNとして計算量はO(N)。
    """
    return [(value, sum(1 for _ in group)) for value, group in groupby(values)]
