import unittest

from mylib.graph.bellman_ford import bellman_ford
from mylib.graph.bfs import bfs_distances
from mylib.graph.dfs import dfs_order
from mylib.graph.dijkstra import dijkstra
from mylib.graph.floyd_warshall import floyd_warshall
from mylib.graph.kruskal import kruskal


class GraphTest(unittest.TestCase):
    def test_bfs_distances(self) -> None:
        graph = [[1, 2], [0, 3], [0, 3], [1, 2], []]
        self.assertEqual(bfs_distances(graph, 0), [0, 1, 1, 2, -1])

    def test_dfs_order(self) -> None:
        graph = [[1, 2], [3], [3], []]
        self.assertEqual(dfs_order(graph, 0), [0, 1, 3, 2])

    def test_dijkstra(self) -> None:
        graph = [
            [(1, 4), (2, 1)],
            [(3, 1)],
            [(1, 2), (3, 5)],
            [],
            [],
        ]
        self.assertEqual(dijkstra(graph, 0, 999), [0, 3, 1, 4, 999])

    def test_dijkstra_rejects_negative_weight(self) -> None:
        with self.assertRaises(ValueError):
            dijkstra([[(1, -1)], []], 0)

    def test_bellman_ford(self) -> None:
        distances, has_negative_cycle = bellman_ford(
            4,
            [(0, 1, 1), (1, 2, -2), (0, 2, 4), (2, 3, 2)],
            0,
        )
        self.assertEqual(distances, [0, 1, -1, 1])
        self.assertFalse(has_negative_cycle)

    def test_bellman_ford_detects_reachable_negative_cycle(self) -> None:
        _, has_negative_cycle = bellman_ford(3, [(0, 1, 1), (1, 2, -2), (2, 1, -2)], 0)
        self.assertTrue(has_negative_cycle)

    def test_floyd_warshall(self) -> None:
        infinity = 10**9
        original = [[0, 3, infinity], [infinity, 0, 2], [1, infinity, 0]]
        result = floyd_warshall(original)
        self.assertEqual(result, [[0, 3, 5], [3, 0, 2], [1, 4, 0]])
        self.assertEqual(original[0][2], infinity)

    def test_kruskal(self) -> None:
        total, selected = kruskal(
            4,
            [(0, 1, 1), (1, 2, 2), (0, 2, 4), (2, 3, 3), (0, 3, 10)],
        )
        self.assertEqual(total, 6)
        self.assertEqual(len(selected), 3)


if __name__ == "__main__":
    unittest.main()
