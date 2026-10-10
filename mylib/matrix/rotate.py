"""行列の回転。"""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def rotate_matrix_clockwise(matrix: Sequence[Sequence[T]]) -> list[list[T]]:
    """長方形行列を時計回りに90度回転した新しい行列を返す。

    要素数をNとして計算量と空間計算量はO(N)。
    """
    if not matrix:
        return []
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("matrix must be rectangular")
    return [list(row) for row in zip(*matrix[::-1])]
