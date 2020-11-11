#!/usr/bin/env python3

"""
Programme pour évaluer une expression Python
(version simplifiée)

Par Sébatien Fortier
"""

import sys
import getpass
import colorama
from colorama import Fore, Style

from math import * # noqa

colorama.init()


def main() -> None:
    """Fonction principale"""

    try:
        print(Fore.CYAN + "Selon Sébas Fortier:", Fore.RESET,
              eval(''.join(sys.argv[1:]) or "None"))
    except Exception as ex:
        print(Fore.RED, ex, file=sys.stderr, sep='')
        sys.exit(1)

if __name__ == '__main__':
    main()
