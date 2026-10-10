"""素数判定。"""


def is_prime(value: int) -> bool:
    """valueが素数ならTrueを返す。

    計算量はO(sqrt(value))。
    """
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2

    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True
