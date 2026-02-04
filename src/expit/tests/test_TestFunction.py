import math
import sys
import unittest
from typing import *

from expit.core import function

__all__ = ["TestFunction"]


class TestFunction(unittest.TestCase):
    def test_function_regular_values(self: Self) -> None:
        # Test regular values of x
        self.assertAlmostEqual(function(0), 0.5)
        self.assertAlmostEqual(function(1), 1 / (1 + math.exp(-1)), places=5)
        self.assertAlmostEqual(function(-1), 1 / (1 + math.exp(1)), places=5)

    def test_function_large_positive(self: Self) -> None:
        # Test large positive values of x (result should approach 1)
        self.assertAlmostEqual(function(100), 1.0, places=5)
        self.assertAlmostEqual(function(1000), 1.0, places=5)

    def test_function_large_negative(self: Self) -> None:
        # Test large negative values of x (result should approach 0)
        self.assertAlmostEqual(function(-100), 0.0, places=5)
        self.assertAlmostEqual(function(-1000), 0.0, places=5)

    def test_function_overflow(self: Self) -> None:
        # Test overflow values to ensure they are handled without errors
        self.assertAlmostEqual(function(sys.float_info.max), 1.0, places=5)
        self.assertAlmostEqual(function(-sys.float_info.max), 0.0, places=5)

    def test_function_infinity(self: Self) -> None:
        # Test positive and negative infinity inputs
        self.assertEqual(function(float("inf")), 1.0)
        self.assertEqual(function(float("-inf")), 0.0)

    def test_function_nan(self: Self) -> None:
        # Test NaN input; behavior may vary, but we can ensure it doesn't throw an error
        result: Any
        result = function(float("nan"))
        self.assertTrue(
            math.isnan(result) or result in [0.0, 1.0]
        )  # Depending on interpretation, could be NaN, 0, or 1


if __name__ == "__main__":
    unittest.main()
