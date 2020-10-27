#!/usr/bin/env python3

"""
Scrip démontrant l'utilisation de isatty et readlines

Par Sébatien Fortier
"""

import sys

def main() -> None:
    """Fonction principale"""

    if sys.stdin.isatty():
        print("Aucune redirection d'entrée à traiter")
        return

    lignes = sys.stdin.readlines()

    if not lignes:
        return
    sys.argv.pop(0)

    for ligne in lignes[:-1]:
        print(ligne, end="")
        for arg in sys.argv:
            print(arg)

    print(lignes[-1], end="")





if __name__ == '__main__':
    main()