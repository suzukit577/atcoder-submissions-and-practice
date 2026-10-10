"""幅優先探索。"""

from collections import deque
from collections.abc import Sequence


def bfs_distances(graph: Sequence[Sequence[int]], start: int) -> list[int]:
    """無重みグラフでstartからの最短距離を返す。

    到達不能な頂点の距離は-1。計算量はO(V + E)。
    """
    if not 0 <= start < len(graph):
        raise IndexError("start is out of range")

    distances = [-1] * len(graph)
    distances[start] = 0
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if distances[neighbor] != -1:
                continue
            distances[neighbor] = distances[vertex] + 1
            queue.append(neighbor)
    return distances
