# Run Length Encoding
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
new_rle_S = []
cnt = 0
for char, length in rle_S:
    if char == "1":
        cnt += 1
    if char == "1" and cnt == K:
        popped_cl = new_rle_S.pop()
        new_rle_S.append((char, length))
        new_rle_S.append(popped_cl)
    else:
        new_rle_S.append((char, length))
for char, length in new_rle_S:
    print(char * length, end="")
