"""拡張ユークリッドの互除法と乗法逆元。"""


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """gcd(a, b)とax + by = gcd(a, b)を満たすx, yを返す。

    計算量はO(log(min(abs(a), abs(b))))。
    """
    if b == 0:
        gcd = abs(a)
        return gcd, 1 if a >= 0 else -1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    return gcd, y1, x1 - (a // b) * y1


def mod_inverse(value: int, modulus: int) -> int:
    """modulusを法とするvalueの乗法逆元を返す。

    逆元が存在しない場合はValueError。計算量はO(log(modulus))。
    """
    if modulus <= 1:
        raise ValueError("modulus must be greater than 1")
    gcd, inverse, _ = extended_gcd(value % modulus, modulus)
    if gcd != 1:
        raise ValueError(f"inverse does not exist for {value} modulo {modulus}")
    return inverse % modulus
