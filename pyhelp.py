#!/usr/bin/env python3

"""
Programme pour afficher la documentation python

Par Sébatien Fortier
"""

import re
import sys
import types
import builtins
import colorama

from colorama import Fore, Style

colorama.init()


def main() -> None:
    """Fonction principale"""
    if len(sys.argv) == 1:
        print(Fore.YELLOW + "[SF]" + Fore.RED + " Le script s'attend à recevoir 1 argument, mais vous en avez fourni 0")
        print(Fore.YELLOW + "USAGE: ./pyhelp.py sujet")
        exit(1)

    if len(sys.argv) > 2:
        print(Fore.YELLOW + "[SF]" + Fore.RED + " Le script s'attend à recevoir 1 argument, mais vous en avez fourni 2")
        print(Fore.YELLOW + "USAGE: ./pyhelp.py sujet")
        exit(1)

    argument = sys.argv[1]

    match = re.search(r'^([a-zA-Z0-9-]+.?)$|^([a-zA-Z0-9-]+.?)*[^.\W]$', argument)

    if match:
        print(
            Style.BRIGHT + Fore.YELLOW + "[SF]" + Fore.WHITE + "Affichage de l'aide pour: " + Fore.MAGENTA + argument,
            file=sys.stderr)
        if argument in eval("[i for i in dir(builtins) if i.islower()]"):
            help(match.string)
        else:
            print(Fore.YELLOW + "[SF] " + Fore.RED + "name " + "'" + match.string + "'" + " is not defined")

    else:
        print(
            Style.BRIGHT + Fore.YELLOW + "[SF]" + Fore.RED + "Le sujet de l'aide n'est pas valide: " + Fore.MAGENTA + argument,
            file=sys.stderr)
        exit(1)


if __name__ == '__main__':
    main()
