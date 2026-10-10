import unittest

from mylib.sequence.coordinate_compression import coordinate_compression
from mylib.sequence.run_length_encode import run_length_encode
from mylib.utils.keys_from_value import keys_from_value


class SequenceAndUtilsTest(unittest.TestCase):
    def test_run_length_encode(self) -> None:
        self.assertEqual(
            run_length_encode("aaabbcaaaa"),
            [("a", 3), ("b", 2), ("c", 1), ("a", 4)],
        )
        self.assertEqual(run_length_encode(iter(())), [])

    def test_coordinate_compression(self) -> None:
        self.assertEqual(coordinate_compression([100, 50, 100, -2]), [2, 1, 2, 0])

    def test_keys_from_value(self) -> None:
        self.assertEqual(keys_from_value({"a": 1, "b": 2, "c": 1}, 1), ["a", "c"])


if __name__ == "__main__":
    unittest.main()
