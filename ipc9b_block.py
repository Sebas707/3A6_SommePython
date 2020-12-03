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
from multiprocessing import Process, Queue
from multiprocessing.connection import Connection
import ctypes
import pickle

colorama.init()
DELAI_SEC = 2.0


def main() -> None:
    """Fonction principale"""
    ps: Optional[Process] = None
    try:
        expr = ' '.join(sys.argv[1:]) or "None"
        queue = Queue()
        ps = Process(target=pyval, args=(expr, queue))
        ps.start()
        évaluation = queue.get(block=True, timeout=DELAI_SEC)
        if isinstance(évaluation, BaseException):
            raise évaluation
        print(Fore.CYAN + "Block selon Sébastien Fortier:", Fore.RESET, évaluation)
    except Empty:
        exexit(TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé"))

    except BaseException as ex:
        exexit(ex)

    finally:
        ps and ps.terminate()

def pyval(expr: str, queue: Queue) -> None:
    """
    Évalue une expression.
    Retour (sérialisé) via queue.
    """
    try:
        évaluation = safe_eval(expr)

    except BaseException as ex:
        évaluation = ex

    queue.put(évaluation)


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapport une erreur et termine le programme"""
    print(Fore.YELLOW, "[SF] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex, Fore.RESET,
          file=sys.stderr, sep='')
    sys.exit(exit_code)

if __name__ == '__main__':
    main()