#!/usr/bin/env python3

"""
Script qui permet d'afficher les lignes matchant un pattern regex d'un texte

Par Sébatien Fortier
"""

import sys
import re
from colorama import Fore


def main() -> None:
    """Fonction principale"""
    sys.argv.pop(0)

    if len(sys.argv) < 1:
        print(Fore.RED + "Le script s'atend à recevoir 1 argument, mais vous en avez fourni 0", file=sys.stderr)
        print(Fore.YELLOW + "USAGE: ./pygrep.py pattern", file=sys.stderr)
        exit(1)

    compteur_de_match = 0
    textes = sys.stdin.readlines()
    for ligne in textes:
        match = re.search(sys.argv[0], ligne)

        if match is not None:
            print(ligne, end='', file=sys.stdout)
            compteur_de_match += 1

    if compteur_de_match == 1:
        print(Fore.YELLOW + "[ " + str(compteur_de_match) + " correspondance ]", file=sys.stderr)
    elif compteur_de_match > 0:
        print(Fore.YELLOW + "[ " + str(compteur_de_match) + " correspondances ]", file=sys.stderr)
    else:
        print(Fore.YELLOW + "[ aucune correspondance ]", file=sys.stderr)


if __name__ == '__main__':
    main()
