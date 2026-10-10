import unittest

from mylib.bit.count_set_bits import count_numbers_with_i_th_bit_set
from mylib.bit.popcount import popcount


class BitTest(unittest.TestCase):
    def test_popcount(self) -> None:
        self.assertEqual(popcount(0), 0)
        self.assertEqual(popcount(0b101101), 4)

    def test_popcount_rejects_negative_value(self) -> None:
        with self.assertRaises(ValueError):
            popcount(-1)

    def test_count_numbers_with_i_th_bit_set(self) -> None:
        for bit in range(5):
            for upper in range(20):
                expected = sum((value >> bit) & 1 for value in range(upper + 1))
                self.assertEqual(count_numbers_with_i_th_bit_set(bit, upper), expected)


if __name__ == "__main__":
    unittest.main()
