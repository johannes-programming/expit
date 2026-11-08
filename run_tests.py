from __future__ import annotations

__all__: list[str] = []

import sys

import expit.tests

sys.exit(1 - expit.tests.test().wasSuccessful())
