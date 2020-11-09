#!/usr/bin/env python3

"""
Évalue l'argument passé en paramètre

Par Sébatien Fortier
"""

import sys
import getpass
import colorama

from colorama import Fore, Style

colorama.init()


def main() -> None:
    """Fonction principale"""

    argument = ""

    sys.argv.pop(0)

    for arg in sys.argv:
        argument += arg

    try:
        texte = Style.BRIGHT + Fore.CYAN + f"Selon {getpass.getuser()} : " + str(eval(argument))
        print(texte)
    except Exception as ex:
        print(Style.BRIGHT + Fore.RED + str(ex), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
