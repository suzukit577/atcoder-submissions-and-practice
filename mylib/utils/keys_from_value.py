"""辞書の値からキーを取得する。"""

from collections.abc import Mapping
from typing import TypeVar

K = TypeVar("K")
V = TypeVar("V")


def keys_from_value(mapping: Mapping[K, V], value: V) -> list[K]:
    """valueと等しい値を持つキーを挿入順で返す。

    要素数をNとして計算量はO(N)。
    """
    return [key for key, candidate in mapping.items() if candidate == value]
