import unittest

from mylib.data_structures.segment_tree import SegmentTree
from mylib.data_structures.union_find import UnionFind


class UnionFindTest(unittest.TestCase):
    def test_merge_and_groups(self) -> None:
        union_find = UnionFind(5)
        union_find.merge(0, 1)
        union_find.merge(1, 2)
        union_find.merge(3, 4)

        self.assertTrue(union_find.same(0, 2))
        self.assertFalse(union_find.same(0, 3))
        self.assertEqual(union_find.size(1), 3)
        self.assertEqual(union_find.groups(), [[0, 1, 2], [3, 4]])


class SegmentTreeTest(unittest.TestCase):
    def test_sum_and_update(self) -> None:
        tree = SegmentTree([2, 1, 4, 3], lambda left, right: left + right, 0)

        self.assertEqual(tree.prod(1, 4), 8)
        self.assertEqual(tree.all_prod(), 10)
        tree.set(2, 10)
        self.assertEqual(tree.get(2), 10)
        self.assertEqual(tree.all_prod(), 16)

    def test_non_commutative_operator(self) -> None:
        tree = SegmentTree(["a", "b", "c"], lambda left, right: left + right, "")
        self.assertEqual(tree.prod(0, 3), "abc")
        self.assertEqual(tree.prod(1, 3), "bc")


if __name__ == "__main__":
    unittest.main()
