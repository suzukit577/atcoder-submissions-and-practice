"""Union-Find。"""


class UnionFind:
    """素集合データ構造。

    経路圧縮とunion by sizeにより、各操作の償却計算量はO(alpha(N))。
    """

    def __init__(self, size: int) -> None:
        if size < 0:
            raise ValueError("size must be non-negative")
        self._parent_or_size = [-1] * size

    def __len__(self) -> int:
        return len(self._parent_or_size)

    def leader(self, node: int) -> int:
        """nodeが属する集合の代表元を返す。"""
        self._validate(node)
        parent = self._parent_or_size[node]
        if parent < 0:
            return node
        self._parent_or_size[node] = self.leader(parent)
        return self._parent_or_size[node]

    def merge(self, left: int, right: int) -> int:
        """leftとrightの集合を併合し、併合後の代表元を返す。"""
        left_leader = self.leader(left)
        right_leader = self.leader(right)
        if left_leader == right_leader:
            return left_leader

        if self._parent_or_size[left_leader] > self._parent_or_size[right_leader]:
            left_leader, right_leader = right_leader, left_leader
        self._parent_or_size[left_leader] += self._parent_or_size[right_leader]
        self._parent_or_size[right_leader] = left_leader
        return left_leader

    def same(self, left: int, right: int) -> bool:
        """leftとrightが同じ集合に属するか返す。"""
        return self.leader(left) == self.leader(right)

    def size(self, node: int) -> int:
        """nodeが属する集合の要素数を返す。"""
        return -self._parent_or_size[self.leader(node)]

    def groups(self) -> list[list[int]]:
        """すべての集合を代表元の昇順で返す。"""
        result: dict[int, list[int]] = {}
        for node in range(len(self)):
            result.setdefault(self.leader(node), []).append(node)
        return [result[leader] for leader in sorted(result)]

    def _validate(self, node: int) -> None:
        if not 0 <= node < len(self):
            raise IndexError("node is out of range")
