"""座標圧縮。"""

from collections.abc import Sequence


def coordinate_compression(values: Sequence[int]) -> list[int]:
    """valuesを0始まりの順位へ変換する。

    要素数をNとして計算量はO(N log N)。
    """
    rank = {value: index for index, value in enumerate(sorted(set(values)))}
    return [rank[value] for value in values]
