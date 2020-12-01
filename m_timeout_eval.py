"""
Version minutée (et sécuritaire) de la fonction builtin eval (DIRO)

2020, Sébastien Fortier
"""

from typing import Any
from wrapt_timeout_decorator import timeout  # noqa
from m_safe_eval import safe_eval

DELAI_SEC = 1.0
"""Délai par défaut pour l'évaluation"""


@timeout(DELAI_SEC)  # Décorateur
def capped_eval(__source: str,
                __globals: dict = None,
                __locals: dict = None,
                safe: bool = True) -> Any:
    """
    Évalue l'expression dans un certain délai.
    Lève un TimeoutError à l'expiration du délai
    DIRO pour eval.
    """
    return (safe_eval if safe else eval)(__source, __globals, __locals)


def timeout_eval(__source: str,
                 __globals: dict = None,
                 __locals: dict = None,
                 safe: bool = True,
                 delai_sec: float = DELAI_SEC) -> Any:
    """
    Évalue l'expression dans un certain délai fourni en argument.
    Lève un TimeoutError à l'expiration du délai
    DIRO pour eval.
    """
    return capped_eval(__source, __globals, __locals, safe, dec_timeout=delai_sec)
