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
import ctypes
import pickle

colorama.init()
DELAI_SEC = 2.0


def main() -> None:
    """Fonction principale"""
    try:
        expr = ' '.join(sys.argv[1:]) or "None"
        filename = "ipc5.bin"
        ps = Process(target=pyval, args=(expr, filename))
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé")
        with open(filename, "r+b") as f:
            évaluation = pickle.load(f)
        if isinstance(évaluation, BaseException):
            raise évaluation
        print(Fore.CYAN + "Selon Sébastien Fortier:", Fore.RESET, évaluation)

    except KeyboardInterrupt:
        pass

    except Exception as ex:
        exexit(ex)


def pyval(expr: str, filename: str) -> None:
    """
    Évalue une expression.
    Retour via sérialisation dans un fichier.
    Même l'exception est retournée!
    """
    try:
        évaluation = safe_eval(expr)
        print(expr, '=', évaluation)

    except BaseException as ex:
        évaluation = ex

    with open(filename, 'w+b') as f:
        pickle.dump(évaluation, f)


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapport une erreur et termine le programme"""
    print(Fore.YELLOW, "[SF] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex, Fore.RESET,
          file=sys.stderr, sep='')
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
