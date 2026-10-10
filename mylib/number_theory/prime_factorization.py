"""素因数分解。"""


def prime_factorization(value: int) -> list[tuple[int, int]]:
    """正整数valueを(素因数, 指数)のリストへ分解する。

    valueが1の場合は空リスト。計算量はO(sqrt(value))。
    """
    if value < 1:
        raise ValueError("value must be positive")

    factors: list[tuple[int, int]] = []
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor != 0:
            divisor += 1
            continue
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        factors.append((divisor, exponent))
        divisor += 1
    if remaining > 1:
        factors.append((remaining, 1))
    return factors
