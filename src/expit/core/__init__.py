from __future__ import annotations

__all__: list[str] = ["function", "main", "parse_args", "run"]

import argparse
import logging
import math
from collections import abc
from importlib import metadata


def function(x: float, /) -> float:
    "This function is the logistical sigmoid, i.e. the expit function."
    p: float
    try:
        p = math.exp(-x)
    except OverflowError:
        p = float("+inf")
    return 1 / (1 + p)


def main(args: abc.Iterable[str] | None = None) -> int:
    "This command applies"
    space: argparse.Namespace
    try:
        space = parse_args(args)
    except SystemExit as exit:
        if isinstance(exit.code, int):
            return exit.code
        else:
            return int(bool(exit.code))
    try:
        run(space.x)
    except Exception as exc:
        logging.exception(exc)
        return 1
    return 0


def parse_args(args: abc.Iterable[str] | None = None) -> argparse.Namespace:
    parser: argparse.ArgumentParser
    version: str
    parser = argparse.ArgumentParser(
        add_help=False,
        description="This command applies the expit function to x.",
        fromfile_prefix_chars="@",
        prog="expit",
    )
    parser.add_argument(
        "-h",
        "--help",
        action="help",
        help="show this help message and exit",
    )
    version = "%(prog)s, version " + metadata.version("expit")
    parser.add_argument("-V", "--version", action="version", version=version)
    parser.add_argument("x", type=float)
    return parser.parse_args(args)


def run(x: float) -> None:
    print(function(x))
