"""Kruskal法。"""

from collections.abc import Sequence


def kruskal(
    vertex_count: int,
    edges: Sequence[tuple[int, int, int]],
) -> tuple[int, list[tuple[int, int, int]]]:
    """最小全域森の重みと採用辺を返す。

    辺は(u, v, weight)で指定。計算量はO(E log E)。
    """
    if vertex_count < 0:
        raise ValueError("vertex_count must be non-negative")

    parent_or_size = [-1] * vertex_count

    def leader(vertex: int) -> int:
        if parent_or_size[vertex] < 0:
            return vertex
        parent_or_size[vertex] = leader(parent_or_size[vertex])
        return parent_or_size[vertex]

    total_weight = 0
    selected: list[tuple[int, int, int]] = []
    for left, right, weight in sorted(edges, key=lambda edge: edge[2]):
        left_leader = leader(left)
        right_leader = leader(right)
        if left_leader == right_leader:
            continue
        if parent_or_size[left_leader] > parent_or_size[right_leader]:
            left_leader, right_leader = right_leader, left_leader
        parent_or_size[left_leader] += parent_or_size[right_leader]
        parent_or_size[right_leader] = left_leader
        total_weight += weight
        selected.append((left, right, weight))
    return total_weight, selected
