#!/usr/bin/env python3

"""
Programme qui sert à faire l'exercice

Par Sébastien Fortier
"""

import colorama
from colorama import Fore, Style
from typing import NoReturn
import sys
import time
import pyval_safe  # Exercice précédant
from multiprocessing import Process
import os
colorama.init()

DELAI_SEC = 500


def main() -> None:
    """Fonction principale"""
    try:
        ps_eval = Process(target=pyval_safe.main)
        ps_eval.start()

        ps_dot = Process(target=print_forever, args=('.', 0.1))
        ps_dot.start()

        print('délai', DELAI_SEC,
              '--', 'main', os.getpid(),
              '--', 'ps_eval', ps_eval.pid,
              '--', 'ps_dot:', ps_dot.pid)

        ps_eval.join(DELAI_SEC)
        ps_dot.terminate()

        if ps_eval.is_alive():
            ps_eval.terminate()
            print()
            raise TimeoutError(f"Le délai de {DELAI_SEC} secondes est écoulé")
        else:
            sys.exit(ps_eval.exitcode)
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

def print_forever(ceci: str, delai_sec: float) -> None:
    """Affiche répétitivement quelque chose, sans arrêt"""

    try:
        while True:
            time.sleep(delai_sec)
            print(ceci, end='', flush=True)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()