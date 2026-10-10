"""約数列挙。"""


def divisors(value: int) -> list[int]:
    """正整数valueの約数を昇順で返す。

    計算量はO(sqrt(value))。
    """
    if value < 1:
        raise ValueError("value must be positive")

    lower: list[int] = []
    upper: list[int] = []
    divisor = 1
    while divisor * divisor <= value:
        if value % divisor == 0:
            lower.append(divisor)
            if divisor != value // divisor:
                upper.append(value // divisor)
        divisor += 1
    return lower + upper[::-1]
