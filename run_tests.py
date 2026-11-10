from __future__ import annotations

__all__: list[str] = []

import sys

import expit.tests


def main() -> int:
    return 1 - expit.tests.test().wasSuccessful()


if __name__ == "__main__":
    sys.exit(main())
