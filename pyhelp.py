#!/usr/bin/env python3

"""
Programme pour afficher la documentation python

Par Sébatien Fortier
"""

import re
import sys
import colorama

from colorama import Fore

colorama.init()


def main() -> None:
    """Fonction principale"""
    if len(sys.argv) == 1:
        print(Fore.RED + "[SF] Le script s'attend à recevoir 1 argument, mais vous en avez fourni 0")
        print(Fore.YELLOW + "USAGE: ./pyhelp.py sujet")
        exit(1)

    if len(sys.argv) > 2:
        print(Fore.RED + "[SF] Le script s'attend à recevoir 1 argument, mais vous en avez fourni 2")
        print( Fore.YELLOW + "USAGE: ./pyhelp.py sujet")
        exit(1)

    argument = sys.argv[1]

    match = re.search('.*', argument)

    print(match[0])


if __name__ == '__main__':
    main()
