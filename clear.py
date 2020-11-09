#!/usr/bin/env python3

"""
Programme pour effacer l'écran

Par Sébastien Fortier
"""

import getpass
import os


def main() -> None:
    """Fonction principale"""
    effacer = "cls" if os.name == "nt" else "clear" if os.name == "posix" else ""
    os.system(effacer)
    os.system(f"echo {getpass.getuser()} dit: Écran effacé!")


if __name__ == '__main__':
    main()
