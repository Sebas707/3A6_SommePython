#!/usr/bin/env python3

"""
Programme pour évaluer une expression Python
(version simplifiée)

Par Sébatien Fortier
"""

import sys
import colorama
from colorama import Fore
import math
from math import * # noqa

colorama.init()

GLOBALS = {"__builtins__": {},
           **math.__dict__,
           "abs": abs,
           "min": min,
           "max": max,
           "sum": sum
           }
LOCALS = {}


def main() -> None:
    """Fonction principale"""

    try:
        print(Fore.CYAN + "Selon Sébas Fortier:", Fore.RESET,
              eval(''.join(sys.argv[1:]) or "None", GLOBALS, LOCALS))
    except Exception as ex:
        print(Fore.RED, ex, file=sys.stderr, sep='')
        sys.exit(1)


if __name__ == '__main__':
    main()
