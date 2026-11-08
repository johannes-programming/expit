from __future__ import annotations

__all__: list[str] = ["function", "main", "parse_args", "run", "test"]

import sys

from expit.core import function, main, parse_args, run
from expit.tests import test

if __name__ == "__main__":
    sys.exit(main())
