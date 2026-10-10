"""立っているビットの個数を数える。"""


def popcount(value: int) -> int:
    """非負整数の1ビットの個数を返す。

    計算量は整数のビット長をBとしてO(B)。
    """
    if value < 0:
        raise ValueError("value must be non-negative")
    return value.bit_count()
