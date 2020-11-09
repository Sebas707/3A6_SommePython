#!/usr/bin/env python3

"""
Programme reproduit l'action de la commande touch dans linux

Par Sébastien Fortier
"""

import math
import argparse
import colorama

from colorama import init, Fore, Style

init(convert=True)

def parse_args() -> argparse.Namespace:
    """Gère les arguments passés à la ligne de commande"""
    parser = argparse.ArgumentParser(description='Commande pour créer des fichiers -- @2020, par Sébastien Fortier')
    parser.add_argument('fichier', metavar='FILE', type=str, nargs="+", help="Fichiers à créer")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action='store_true', help='Ne pas notifier si existe déjà')
    group.add_argument('-v', '--verbeux', action='store_true', help='Notifier les créations')
    parser.add_argument('-t', '--texte', type=str, metavar='TXT', help='Texte à stocker dans les fichiers crées')
    return parser.parse_args()


def main() -> None:
    """Fonction principale"""
    args = parse_args()

    for fichier in args.fichier:
        try:
            f = open(fichier, "x")
            if args.texte is not None:
                f.write(args.texte)
            if args.verbeux:
                print(Fore.WHITE + "Fichier créé: " + Fore.CYAN + fichier)

        except FileExistsError:
            if args.quiet:
                print("", end='')
            else:
                print(Style.BRIGHT + Fore.YELLOW +"Le fichier existe déjà: " + Style.BRIGHT + Fore.CYAN + fichier)
        except OSError as ex:
            print(Fore.RED + str(type(ex).__name__ + ": ") + Fore.YELLOW + str(ex))
            exit(1)


if __name__ == '__main__':
    main()
