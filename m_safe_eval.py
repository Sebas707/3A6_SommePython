"""
Définitions utiles pourune évaluation sécuritaire du code.

Inclue un DIRO (Drop-in Replacement Object) pour la builtin eval.

2020, Sébastien Fortier
"""

import math
from typing import Any


SAFE_GLOBALS = {
    "__builtins__": {},
    **math.__dict__,
    "abs": abs,
    "min": min,
    "max": max,
    "sum": sum
}
"""Globals sécuritaire pour eval """

def sanitize(code : str) -> str:
    """Assainit le code source insécure"""
    return code.replace('__', '')


def safe_eval(__source: str, __globals: dict = None, __locals: dict = None) -> Any:
    """Évalue sécuritairement l'expression. DIRO pour eval."""
    return eval(sanitize(__source), __globals or SAFE_GLOBALS, __locals)