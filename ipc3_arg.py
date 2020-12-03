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


def main() -> None:
    """Fonction principale"""
    try:
        expr = ' '.join(sys.argv[1:]) or "None"
        retour = [99]
        ps = Process(target=pyval, args=(expr, retour))
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé")
        if not ps.exitcode:
            print(Fore.CYAN + "Arg selon Sébastien Fortier:", Fore.RESET, retour[0])
    except Exception as ex:
        exexit(ex)

    except KeyboardInterrupt:
        pass

def pyval(expr: str, retour: list) -> None:
    """
    Évalue une expression.
    Retour via argument
    """

    try:
        assert retour[0] == 99
        retour[0] = safe_eval(expr)
        print(expr, '=', retour[0])

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