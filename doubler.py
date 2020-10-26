#!/usr/bin/env python3

"""
Programme pour doubler un nombre

Par Sébastien Fortier
"""

import colorama
from colorama import Fore, Style
colorama.init()

import getpass
import sys
import os

def main() -> None:
    """Fonction principale"""
    vérifier_usage()
    try:
        nombre = float(sys.argv[1])
        print(Style.BRIGHT + Fore.CYAN + 'Selon', getpass.getuser(), ':', nombre * 2)

    except ValueError:
        print(Style.BRIGHT + Fore.RED + f"L'argument '{sys.argv[1]}' n'est pas un nombre.", file=sys.stderr)




def erreur(msg: str) -> None:
    """Affiche un message d'erreur, puis termine le script"""
    print(msg, file=sys.stderr)
    sys.exit(1)


def vérifier_usage() -> None:
    """
    Vérifie l'usage du programme et en cas d'erreur,
    affiche un message d'erreur et un usage, puis termine le script
    """

    nbargs = len(sys.argv) - 1
    if nbargs != 1:
        nom_script = os.path.join('.', os.path.basename(sys.argv[0]))
        erreur(
            Style.BRIGHT + Fore.RED + f"Le script s'attend à recevoir 1 argument, mais vous en avez fourni {nbargs}\n" +
            Style.BRIGHT + Fore.YELLOW + f"USAGEL {nom_script} nombre"
        )
if __name__ == '__main__':
    main()


