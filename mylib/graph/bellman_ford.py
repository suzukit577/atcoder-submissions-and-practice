"""Bellman-Ford法。"""

from collections.abc import Sequence


def bellman_ford(
    vertex_count: int,
    edges: Sequence[tuple[int, int, int]],
    start: int,
    infinity: int = 10**30,
) -> tuple[list[int], bool]:
    """最短距離と、到達可能な負閉路が存在するかを返す。

    有向辺は(from, to, weight)で指定。計算量はO(VE)。
    """
    if vertex_count < 0:
        raise ValueError("vertex_count must be non-negative")
    if not 0 <= start < vertex_count:
        raise IndexError("start is out of range")

    distances = [infinity] * vertex_count
    distances[start] = 0
    for iteration in range(vertex_count):
        updated = False
        for source, destination, weight in edges:
            if distances[source] == infinity:
                continue
            candidate = distances[source] + weight
            if candidate >= distances[destination]:
                continue
            distances[destination] = candidate
            updated = True
            if iteration == vertex_count - 1:
                return distances, True
        if not updated:
            break
    return distances, False
