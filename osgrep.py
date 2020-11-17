#!/usr/bin/env python3

"""
Utilisation de Os grep

Par Sebastien Fortier
"""

import sys
import os
import shlex


def main() -> None:
    """Fonction principale"""
    if os.name == 'posix':
        args = shlex.join(sys.argv[1:]).split(" ")
        commande = "egrep"
    else:
        args = sys.argv[1:]
        commande = "findstr"

    for arg in args:
        commande += " \"" + arg + "\""

    exitcode = os.system(commande)
    if exitcode:
        print("La commande exécutée était: " + commande)

    sys.exit(exitcode)


if __name__ == '__main__':
    main()
