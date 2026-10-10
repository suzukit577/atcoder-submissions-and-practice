"""深さ優先探索。"""

from collections.abc import Sequence


def dfs_order(graph: Sequence[Sequence[int]], start: int) -> list[int]:
    """startから到達可能な頂点を深さ優先順で返す。

    隣接リストに記載された順序を優先。計算量はO(V + E)。
    """
    if not 0 <= start < len(graph):
        raise IndexError("start is out of range")

    visited = [False] * len(graph)
    order: list[int] = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if visited[vertex]:
            continue
        visited[vertex] = True
        order.append(vertex)
        for neighbor in reversed(graph[vertex]):
            if not visited[neighbor]:
                stack.append(neighbor)
    return order
