import unittest

from mylib.matrix.cumulative_sum_3d import (
    build_cumulative_sum_3d,
    query_cumulative_sum_3d,
)
from mylib.matrix.rotate import rotate_matrix_clockwise


class MatrixTest(unittest.TestCase):
    def test_rotate_matrix_clockwise(self) -> None:
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(rotate_matrix_clockwise(matrix), [[4, 1], [5, 2], [6, 3]])

    def test_rotate_matrix_rejects_non_rectangular_input(self) -> None:
        with self.assertRaises(ValueError):
            rotate_matrix_clockwise([[1], [2, 3]])

    def test_cumulative_sum_3d(self) -> None:
        values = [
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
        ]
        cumulative = build_cumulative_sum_3d(values)

        self.assertEqual(query_cumulative_sum_3d(cumulative, 0, 2, 0, 2, 0, 2), 36)
        self.assertEqual(query_cumulative_sum_3d(cumulative, 1, 2, 0, 2, 0, 2), 26)
        self.assertEqual(query_cumulative_sum_3d(cumulative, 0, 2, 1, 2, 1, 2), 12)


if __name__ == "__main__":
    unittest.main()
