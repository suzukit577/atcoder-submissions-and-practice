"""指定したビットが立つ整数の個数を数える。"""


def count_numbers_with_i_th_bit_set(bit: int, upper: int) -> int:
    """0以上upper以下でbit番目が1となる整数の個数を返す。

    bitは0-indexed。計算量はO(1)。
    """
    if bit < 0:
        raise ValueError("bit must be non-negative")
    if upper < 0:
        raise ValueError("upper must be non-negative")

    bit_value = 1 << bit
    cycle = bit_value << 1
    full_cycles, remainder = divmod(upper + 1, cycle)
    return full_cycles * bit_value + max(0, remainder - bit_value)
