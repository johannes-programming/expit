import sys
import unittest
from typing import *

from click.testing import CliRunner

from expit.core import function, main

__all__ = ["TestMainCommand"]


class TestMainCommand(unittest.TestCase):
    def setUp(self: Self) -> None:
        # Set up CliRunner for Click command-line testing
        self.runner = CliRunner()

    def test_main_help_option(self: Self) -> None:
        # Test help option (-h, --help) to ensure it displays usage information
        result: Any
        result = self.runner.invoke(main, ["--help"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Usage", result.output)
        self.assertIn("applies the expit function to x", result.output)

        result = self.runner.invoke(main, ["-h"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Usage", result.output)
        self.assertIn("applies the expit function to x", result.output)

    def test_main_version_option(self: Self) -> None:
        # Test version option (-V, --version) to check version output
        result: Any
        result = self.runner.invoke(main, ["--version"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("version", result.output.lower())

        result = self.runner.invoke(main, ["-V"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("version", result.output.lower())

    def test_main_valid_input(self: Self) -> None:
        # Test main function with a valid float input, checking output
        expected_output: str
        result: Any
        result = self.runner.invoke(main, ["1"])
        expected_output = f"{function(1)}\n"
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, expected_output)

        result = self.runner.invoke(main, ["--", "-1"])
        expected_output = f"{function(-1)}\n"
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, expected_output)

    def test_main_edge_case(self: Self) -> None:
        # Test main function with extreme float inputs
        result: Any
        result = self.runner.invoke(main, [str(sys.float_info.max)])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, f"{function(sys.float_info.max)}\n")

        result = self.runner.invoke(main, ["--", str(-sys.float_info.max)])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, f"{function(-sys.float_info.max)}\n")

    def test_main_invalid_input(self: Self) -> None:
        # Test main function with invalid input, expecting an error
        result: Any
        result = self.runner.invoke(main, ["abc"])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Invalid value for 'X'", result.output)


if __name__ == "__main__":
    unittest.main()
