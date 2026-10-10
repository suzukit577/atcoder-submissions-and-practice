"""エラトステネスの篩。"""


def sieve(upper: int) -> list[bool]:
    """0以上upper以下について素数判定表を返す。

    計算量はO(upper log log upper)、空間計算量はO(upper)。
    """
    if upper < 0:
        raise ValueError("upper must be non-negative")

    is_prime = [True] * (upper + 1)
    if upper >= 0:
        is_prime[0] = False
    if upper >= 1:
        is_prime[1] = False

    prime = 2
    while prime * prime <= upper:
        if is_prime[prime]:
            for composite in range(prime * prime, upper + 1, prime):
                is_prime[composite] = False
        prime += 1
    return is_prime
