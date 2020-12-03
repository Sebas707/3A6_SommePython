#!/usr/bin/env python3

"""
Programme qui affiche des informations sur la date et le temps

Par Sébastien Fortier
"""
import colorama
from colorama import Fore, Style
import sys
from queue import Empty
from typing import NoReturn, Optional
from m_safe_eval import safe_eval
import multiprocessing as mp
from multiprocessing import Process, Queue
from multiprocessing.managers import Namespace
from multiprocessing.connection import Connection
import ctypes
import pickle

colorama.init()
DELAI_SEC = 2222.0


def main() -> None:
    """Fonction principale"""
    ps: Optional[Process] = None
    try:
        expr = ' '.join(sys.argv[1:]) or "None"
        man = mp.Manager()
        ns = man.Namespace()
        ps = mp.Process(target=pyval, args=(expr, ns))
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé")
        évaluation = ns.évaluation
        if isinstance(évaluation, BaseException):
            raise évaluation
        print(Fore.CYAN + "Namespace selon Sébastien Fortier:", Fore.RESET, évaluation)
    except Empty:
        exexit(TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé"))

    except BaseException as ex:
        exexit(ex)

    finally:
        ps and ps.terminate()

def pyval(expr: str, ns: Namespace) -> None:
    """
    Évalue une expression.
    Retour (sérialisé) via queue.
    """
    try:
        évaluation = safe_eval(expr)

    except BaseException as ex:
        évaluation = ex

    ns.évaluation = évaluation


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapport une erreur et termine le programme"""
    print(Fore.YELLOW, "[SF] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex, Fore.RESET,
          file=sys.stderr, sep='')
    sys.exit(exit_code)

if __name__ == '__main__':
    main()