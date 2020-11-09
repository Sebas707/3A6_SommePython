#!/usr/bin/env python3

"""
Programme pour afficher le texte d'un fichier

Par Sébastien Fortier
"""

import colorama
from colorama import Fore, Style

colorama.init()


def main() -> None:
    """Fonction principale"""
    try:
        with open("océans.txt") as f:
            text = Style.BRIGHT + Fore.CYAN + f.read()
    except FileNotFoundError:
        text = Style.BRIGHT + Fore.RED + f"Le fichier 'océans.txt' n'existe pas\n"

    print(text)


if __name__ == '__main__':
    main()
