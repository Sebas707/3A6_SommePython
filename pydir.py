#!/usr/bin/env python3

"""
Affiche la liste deds fichiers passés en arguments

Par Sébatien Fortier
"""


import glob
import sys

def main() -> None:
    """Fonction principale"""
    sys.argv.pop(0)
    try:
        liste = glob.glob(sys.argv[1])
        for arg in sys.argv:
            if arg not in liste:
                liste += glob.glob(arg)
    except IndexError:
        liste = glob.glob("*")

    liste = list(dict.fromkeys(liste))

    for file in liste:
        print(file)




if __name__ == '__main__':
    main()