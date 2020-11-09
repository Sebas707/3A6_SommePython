#!/usr/bin/env python3

"""
Programme pour accéder aux variables d'environnement

Par Sébastien Fortier
"""

import os
import getpass


def main() -> None:
    """Fonction principale"""
    print(f"Il y a {len(os.environ)} variables d'environnement")
    print(f" - OS: {os.getenv('OS', 'Non défini')}")
    print(f" - HOME: {os.getenv('HOMEPATH', os.getenv('HOME', 'Non défini'))}")

    print()
    print("Code portable:")
    print(f" - {os.name}")
    print(f" - user: {getpass.getuser()}")
    print(f" - home: {os.path.expanduser('~')}")
    # print()
    # pprint.pprint(dict(os.environ), width=40)
    pass


if __name__ == '__main__':
    main()
