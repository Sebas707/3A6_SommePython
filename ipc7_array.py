#!/usr/bin/env python3

"""
Programme qui affiche des informations sur la date et le temps

Par Sébastien Fortier
"""
import colorama
from colorama import Fore, Style
import sys
from typing import NoReturn
from m_safe_eval import safe_eval
from multiprocessing import Process, Value
import multiprocessing as mp
import ctypes
import pickle

colorama.init()

DELAI_SEC = 2.0
ARRAY_SIZE = 2048


def main() -> None:
    """Fonction principale"""
    try:
        expr = ' '.join(sys.argv[1:]) or "None"
        retour = mp.Array(ctypes.c_char, ARRAY_SIZE)
        ps = mp.Process(target=pyval, args=(expr, retour))
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé")
        évaluation = pickle.loads(bytes(retour[:]))
        if isinstance(évaluation, BaseException):
            raise évaluation
        print(Fore.CYAN + "Array selon Sébastien Fortier:", Fore.RESET, évaluation)


    except KeyboardInterrupt as ex:
        exexit(ex)

    except Exception as ex:
        exexit(ex)


def pyval(expr: str, retour: mp.Array) -> None:
    """
    Évalue une expression.
    Retour sérialisé via shared memory (array).
    Les exceptions sont aussi retournées
    """
    try:
        évaluation = safe_eval(expr)

    except BaseException as ex:
        évaluation = ex


    sérialisation: bytes = pickle.dumps(évaluation)
    retour[:len(sérialisation)] = sérialisation


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapport une erreur et termine le programme"""
    print(Fore.YELLOW, "[SF] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex, Fore.RESET,
          file=sys.stderr, sep='')
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
