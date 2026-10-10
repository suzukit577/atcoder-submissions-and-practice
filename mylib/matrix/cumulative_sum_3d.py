"""3次元累積和。"""

from collections.abc import Sequence


def build_cumulative_sum_3d(
    values: Sequence[Sequence[Sequence[int]]],
) -> list[list[list[int]]]:
    """3次元配列の累積和を構築する。

    要素数をNとして計算量と空間計算量はO(N)。
    """
    x_size = len(values)
    y_size = len(values[0]) if x_size else 0
    z_size = len(values[0][0]) if y_size else 0
    if any(len(plane) != y_size for plane in values):
        raise ValueError("values must be rectangular")
    if any(len(row) != z_size for plane in values for row in plane):
        raise ValueError("values must be rectangular")

    cumulative = [
        [[0] * (z_size + 1) for _ in range(y_size + 1)] for _ in range(x_size + 1)
    ]
    for x in range(1, x_size + 1):
        for y in range(1, y_size + 1):
            for z in range(1, z_size + 1):
                cumulative[x][y][z] = (
                    values[x - 1][y - 1][z - 1]
                    + cumulative[x - 1][y][z]
                    + cumulative[x][y - 1][z]
                    + cumulative[x][y][z - 1]
                    - cumulative[x - 1][y - 1][z]
                    - cumulative[x - 1][y][z - 1]
                    - cumulative[x][y - 1][z - 1]
                    + cumulative[x - 1][y - 1][z - 1]
                )
    return cumulative


def query_cumulative_sum_3d(
    cumulative: Sequence[Sequence[Sequence[int]]],
    x1: int,
    x2: int,
    y1: int,
    y2: int,
    z1: int,
    z2: int,
) -> int:
    """半開直方体[x1,x2)×[y1,y2)×[z1,z2)の総和を返す。"""
    x_size = len(cumulative) - 1
    y_size = len(cumulative[0]) - 1
    z_size = len(cumulative[0][0]) - 1
    if not (0 <= x1 <= x2 <= x_size):
        raise IndexError("invalid x range")
    if not (0 <= y1 <= y2 <= y_size):
        raise IndexError("invalid y range")
    if not (0 <= z1 <= z2 <= z_size):
        raise IndexError("invalid z range")

    return (
        cumulative[x2][y2][z2]
        - cumulative[x1][y2][z2]
        - cumulative[x2][y1][z2]
        - cumulative[x2][y2][z1]
        + cumulative[x1][y1][z2]
        + cumulative[x1][y2][z1]
        + cumulative[x2][y1][z1]
        - cumulative[x1][y1][z1]
    )
