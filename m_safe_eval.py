"""
Définitions utiles pourune évaluation sécuritaire du code.

Inclue un DIRO (Drop-in Replacement Object) pour la builtin eval.

2020, Sébastien Fortier
"""

import math
from typing import Any


GLOBALS = {
    "__builtins__": {},
    **math.__dict__,
    "abs": abs,
    "min": min,
    "max": max,
    "sum": sum
}
"""Globals sécuritaire pour eval """