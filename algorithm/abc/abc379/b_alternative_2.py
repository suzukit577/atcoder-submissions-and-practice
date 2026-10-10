# 別解 (ランレングス圧縮)
from typing import Iterable, List, Tuple, TypeVar

T = TypeVar("T")


def run_length_encode(iterable: Iterable[T]) -> List[Tuple[T, int]]:
    """与えられたイテラブルに対してランレングス圧縮を行う
    （イテラブルの長さを N として、計算量は O(N)）

    Args:
        iterable (Iterable[T]): 任意のイテラブルなオブジェクト

    Returns:
        List[Tuple[T, int]]: 要素とその出現回数のペアのリスト
    """
    if not iterable:
        return []

    result = []
    iterator = iter(iterable)
    prev = next(iterator)
    count = 1

    for item in iterator:
        if item == prev:
            count += 1
        else:
            result.append((prev, count))
            prev = item
            count = 1

    result.append((prev, count))  # 最後の要素を追加
    return result


N, K = map(int, input().split())
S = input()
rle_S = run_length_encode(S)
ans = 0
for t in rle_S:
    if t[0] == "O":
        ans += t[1] // K
print(ans)
