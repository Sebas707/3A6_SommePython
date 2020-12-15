#!/usr/bin/env python3

"""
Programme séquentile pour détmemriner si un nombre est premier

2020, Sébastie Fortier
"""

import colorama
from colorama import Fore, Style
from typing import NoReturn
import math
import sys
from timeit import default_timer as time
from typing import List
colorama.init()


def main(argv: List[str]) -> None:
    """Fonction principale"""
    temps_début = time()
    try:
        if len(sys.argv) == 1:
            raise IndexError("La commande doit avoir au moins un argument")

        est_nombre_premier = est_premier_séq(int(sys.argv[1]))
        temps_fin = time()
        temps = temps_fin - temps_début
        if est_nombre_premier:
            print(Fore.LIGHTBLUE_EX + "Selon Seb Fortier: Oui")
            print(Fore.LIGHTMAGENTA_EX + "Durée: " + str(temps) + " sec")
        else:
            print(Fore.LIGHTBLUE_EX + "Selon Seb Fortier: Non")
            print(Fore.LIGHTMAGENTA_EX + "Durée: " + str(temps) + " sec")

    except KeyboardInterrupt as ex:
        temps_fin = time()
        temps = temps_fin - temps_début
        print(Fore.LIGHTMAGENTA_EX + "Durée: " + str(temps) + " sec")
        exexit(KeyboardInterrupt("Interruption clavier"))


    except BaseException as exception:
        exexit(exception)


def est_premier_séq(nombre: int) -> bool:
    """Détermine si un nombre est premier"""
    if nombre < 1:
        raise ValueError("Le nombre doit être positif")

    # 1 n'est pas premier
    if nombre == 1:
        return False

    # 2 et 3 sont premiers
    if nombre <= 3:
        return True

    # Le nombres paires ne sont pas premiers (sauf 2)
    if nombre % 2 == 0:
        return False

    racine = math.isqrt(nombre)  # racine entière

    # Si on trouve un diviseur parmi 3, 5, 7, ..., racine
    # alors le nombre n'est pas premier

    for n in range(3, racine + 1, 2):
        if nombre % n == 0:
            return False

    # Sinon le nombre est premier
    return True


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapport une erreur et termine le programme"""
    print(Fore.YELLOW, "[SF] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex, Fore.RESET,
          file=sys.stderr, sep='')
    sys.exit(exit_code)


if __name__ == '__main__':
    main(sys.argv)
