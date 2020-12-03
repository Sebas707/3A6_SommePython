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
from multiprocessing import Process
from threading import Thread

colorama.init()
DELAI_SEC = 2.0

ÉVALUATION = None
"""Variable gloable utilisée pour récupérer le résultat"""

def main() -> None:
    """Fonction principale"""
    try:
        expr = ' '.join(sys.argv[1:]) or "None"
        th = Thread(target=pyval, args=(expr,))
        th.start()
        th.join(DELAI_SEC)
        if th.is_alive():
            raise TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé")

        print(Fore.CYAN + "Selon Sébastien Fortier:", Fore.RESET, ÉVALUATION)
    except Exception as ex:
        exexit(ex)

    except KeyboardInterrupt:
        pass

def pyval(expr: str) -> None:
    """
    Évalue une expression.
    Retour via variable globale
    """

    global ÉVALUATION
    try:
        ÉVALUATION = safe_eval(expr)
        print(expr, '=', ÉVALUATION)

    except BaseException as ex:
        exexit(ex)


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapport une erreur et termine le programme"""
    print(Fore.YELLOW, "[SF] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex, Fore.RESET,
          file=sys.stderr, sep='')
    sys.exit(exit_code)

if __name__ == '__main__':
    main()