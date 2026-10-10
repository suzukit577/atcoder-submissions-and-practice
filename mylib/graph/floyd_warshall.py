"""Floyd-Warshall法。"""

from collections.abc import Sequence


def floyd_warshall(distances: Sequence[Sequence[int]]) -> list[list[int]]:
    """全頂点対の最短距離を新しい行列として返す。

    入力行列は変更しない。頂点数をVとして計算量はO(V^3)。
    """
    vertex_count = len(distances)
    if any(len(row) != vertex_count for row in distances):
        raise ValueError("distances must be a square matrix")

    result = [list(row) for row in distances]
    for middle in range(vertex_count):
        for source in range(vertex_count):
            for destination in range(vertex_count):
                result[source][destination] = min(
                    result[source][destination],
                    result[source][middle] + result[middle][destination],
                )
    return result
