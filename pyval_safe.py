#!/usr/bin/env python3

"""
Programme pour évaluer une expression Python
(version non sécuritaire et modulaire)

2020, Sébastien Fortier
"""

from typing import NoReturn
from colorama import Fore, Style
from m_safe_eval import safe_eval as eval  # noqa
import sys


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapport une erreur et termine le programme"""
    print(Fore.YELLOW, "[SF] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex, Fore.RESET,
          file=sys.stderr, sep='')
    sys.exit(exit_code)


def main() -> None:
    """Fonction principale"""
    try:
        evaluation = eval(' '.join(sys.argv[1:]) or "None")
        print(Fore.CYAN + "Selon Sébas Fortier:", Fore.RESET, evaluation)

    except BaseException as ex:
        exexit(ex)


if __name__ == '__main__':
    main()
