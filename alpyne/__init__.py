"""Convenience re-exports for the framework."""

from importlib import import_module
import sys

_pkg = import_module("src.alpyne")

from src.alpyne import *  # noqa: F401,F403

# expose subpackages so ``from alpyne.core`` works
sys.modules[__name__ + ".core"] = _pkg.core
sys.modules[__name__ + ".common"] = _pkg.common

