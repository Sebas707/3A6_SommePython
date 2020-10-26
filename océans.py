#!/usr/bin/env python3

"""
Programme pour écrire le nom des océans dans un fichier texte

Par Sébastien Fortier
"""


def main() -> None:
    """Fonction principale"""
    oceans = ["Pacifique", "Atlantique", "Indien", "Austral", "Arctique"]

    with open("océans.txt", "w") as f:
        for ocean in oceans:
            print(ocean, file=f)

    with open("océans.txt", "a") as f:
        print(23 * "=", file=f)
        print("Les cinq océans, par Sébastien Fortier.", file=f)




if __name__ == '__main__':
    main()