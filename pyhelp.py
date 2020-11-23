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
            Fore.YELLOW + "[SF]" + Fore.WHITE + "Affichage de l'aide pour: " + Fore.MAGENTA + argument,
            file=sys.stderr)
        if argument.__contains__("."):
            if argument[-1] == '.':
                argument = argument[:-1]
                if argument in sys.builtin_module_names or argument in sys.modules:
                    help(argument)
                else:
                    print(Fore.YELLOW + "[SF] " + Fore.RED + "No module named " + "'" + argument + "'")
            else:
                module_nom = re.search(r'(\w+)', argument)[1]
                if module_nom in sys.modules or module_nom in sys.builtin_module_names:
                    exec("import " + module_nom)
                    if eval("hasattr(" + module_nom + ", argument[len(module_nom) + 1:])"):
                        help(argument)
                    else:
                        print(Fore.YELLOW + "[SF] " + Fore.RED + "module " + "'" + module_nom + "' has no attribute " +
                              "'" + argument[len(module_nom) + 1:] + "'")
                else:
                    print(Fore.YELLOW + "[SF] " + Fore.RED + "module " + "'" + module_nom + "'")

        else:
            if argument in eval("[i for i in dir(builtins) if i.islower()]"):
                help(match.string)
            else:
                print(Fore.YELLOW + "[SF] " + Fore.RED + "name " + "'" + argument + "'" + " is not defined")

    else:
        print(
            Fore.YELLOW + "[SF]" + Fore.RED + "Le sujet de l'aide n'est pas valide: " + Fore.MAGENTA + argument,
            file=sys.stderr)
        exit(1)


if __name__ == '__main__':
    main()
