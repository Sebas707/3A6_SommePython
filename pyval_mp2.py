#!/usr/bin/env python3

"""
Programme qui sert à faire l'exercice

Par Sébastien Fortier
"""

import colorama
from colorama import Fore, Style
from typing import NoReturn
import sys
import pyval_safe  # Exercice précédant
from multiprocessing import Process

colorama.init()

DELAI_SEC = 2.0


def main() -> None:
    """Fonction principale"""
    try:
        p = Process(target=pyval_safe.main)
        p.start()

        incrément = 0.1
        temps = 0.0

        while p.is_alive() and temps < DELAI_SEC:
            if temps > 0.2:
                print('.', end='', flush=True)
            p.join(incrément)
            temps += incrément

        if p.is_alive():
            p.terminate()
            print()
            raise TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé")
        else:
            sys.exit(p.exitcode)
    except Exception as ex:
        exexit(ex)

    except KeyboardInterrupt:
        sys.exit(1)

def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapport une erreur et termine le programme"""
    print(Fore.YELLOW, "[SF] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex, Fore.RESET,
          file=sys.stderr, sep='')
    sys.exit(exit_code)


if __name__ == '__main__':
    main()