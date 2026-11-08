from __future__ import annotations

__all__: list[str] = ["TestVersion"]

import unittest
from collections import abc
from contextlib import redirect_stdout
from io import StringIO
from typing import Self

from expit import main


class TestVersion(unittest.TestCase):
    def go(self: Self, /, args: abc.Iterable[str]) -> str:
        buffer: StringIO
        text: str
        buffer = StringIO()
        with redirect_stdout(buffer):
            main(args)
        text = buffer.getvalue()
        self.assertTrue(text.startswith("expit, "))
        self.assertTrue(text.endswith("\n"))
        self.assertEqual(text.count("\n"), 1)
        return text[7:-1]

    def test_0(self: Self, /) -> None:
        versions: set[str]
        versions = set()
        versions.add(self.go(["-V"]))
        versions.add(self.go(["--version"]))
        self.assertEqual(len(versions), 1)


if __name__ == "__main__":
    unittest.main()
