#!/usr/bin/env python3

"""
Echo en Python

Par Sébatien Fortier
"""


import sys

def main() -> None:
    """Fonction principale"""
    message = ""

    sys.argv.pop(0)

    for arg in sys.argv:
        message += str(arg) + " "

    print(message)





if __name__ == '__main__':
    main()