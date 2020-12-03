#!/usr/bin/env python3

"""
Programme qui affiche des informations sur la date et le temps

Par Sébastien Fortier
"""
import colorama
from colorama import Fore, Style
import sys
from typing import NoReturn, Optional
from m_safe_eval import safe_eval
from multiprocessing import Process, Pipe
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
        parent_conn, child_conn = Pipe()
        ps = Process(target=pyval, args=(expr, child_conn))
        ps.start()
        if not parent_conn.poll(DELAI_SEC):
            raise TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé")
        évaluation = parent_conn.recv()
        if isinstance(évaluation, BaseException):
            raise évaluation
        print(Fore.CYAN + "Fichier selon Sébastien Fortier:", Fore.RESET, évaluation)

    except KeyboardInterrupt as ex:
        exexit(ex)
    except BaseException as ex:
        exexit(ex)

    finally:
        ps and ps.terminate()

def pyval(expr: str, pipe: Connection) -> None:
    """
    Évalue une expression.
    Retour (sérialisé) via pipe.
    """
    try:
        évaluation = safe_eval(expr)

    except BaseException as ex:
        évaluation = ex

    pipe.send(évaluation)
    pipe.close()


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapport une erreur et termine le programme"""
    print(Fore.YELLOW, "[SF] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex, Fore.RESET,
          file=sys.stderr, sep='')
    sys.exit(exit_code)

if __name__ == '__main__':
    main()