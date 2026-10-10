"""ダイクストラ法。"""

from collections.abc import Sequence
from heapq import heappop, heappush


def dijkstra(
    graph: Sequence[Sequence[tuple[int, int]]],
    start: int,
    infinity: int = 10**30,
) -> list[int]:
    """非負重み付きグラフでstartからの最短距離を返す。

    到達不能な頂点の距離はinfinity。計算量はO((V + E) log V)。
    """
    if not 0 <= start < len(graph):
        raise IndexError("start is out of range")

    distances = [infinity] * len(graph)
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        distance, vertex = heappop(queue)
        if distance != distances[vertex]:
            continue
        for neighbor, weight in graph[vertex]:
            if weight < 0:
                raise ValueError("edge weights must be non-negative")
            candidate = distance + weight
            if candidate >= distances[neighbor]:
                continue
            distances[neighbor] = candidate
            heappush(queue, (candidate, neighbor))
    return distances
