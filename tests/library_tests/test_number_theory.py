import unittest

from mylib.number_theory.divisors import divisors
from mylib.number_theory.is_prime import is_prime
from mylib.number_theory.mod_inverse import extended_gcd, mod_inverse
from mylib.number_theory.prime_factorization import prime_factorization
from mylib.number_theory.sieve import sieve


class NumberTheoryTest(unittest.TestCase):
    def test_divisors(self) -> None:
        self.assertEqual(divisors(1), [1])
        self.assertEqual(divisors(36), [1, 2, 3, 4, 6, 9, 12, 18, 36])

    def test_prime_factorization(self) -> None:
        self.assertEqual(prime_factorization(1), [])
        self.assertEqual(prime_factorization(360), [(2, 3), (3, 2), (5, 1)])

    def test_is_prime(self) -> None:
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(99))

    def test_sieve(self) -> None:
        self.assertEqual(sieve(1), [False, False])
        self.assertEqual(
            [value for value, prime in enumerate(sieve(20)) if prime],
            [2, 3, 5, 7, 11, 13, 17, 19],
        )

    def test_extended_gcd(self) -> None:
        gcd, x, y = extended_gcd(30, 18)
        self.assertEqual(gcd, 6)
        self.assertEqual(30 * x + 18 * y, gcd)

    def test_mod_inverse(self) -> None:
        self.assertEqual(mod_inverse(3, 11), 4)
        self.assertEqual(mod_inverse(-3, 11), 7)
        with self.assertRaises(ValueError):
            mod_inverse(6, 9)


if __name__ == "__main__":
    unittest.main()
