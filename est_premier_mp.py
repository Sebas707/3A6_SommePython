#!/usr/bin/env python3

"""
Programme multi-processus pour déterminer si un nombre est premier

2020, Sébastien Fortier
"""

import colorama
from colorama import Fore, Style
from typing import NoReturn
import math
from set_proc_title import setproctitle
import os
import sys
from timeit import default_timer as time
from multiprocessing import Process
from typing import List

colorama.init()


def main(argv: List[str]) -> None:
    """Fonction principale"""
    temps_début = time()
    try:
        if len(argv) == 1:
            raise IndexError("La commande doit avoir au moins un argument")

        est_nombre_premier = est_premier_séq(int(argv[1]))

        if est_nombre_premier:
            print(Fore.LIGHTBLUE_EX + "Selon Seb Fortier: Oui")
        else:
            print(Fore.LIGHTBLUE_EX + "Selon Seb Fortier: Non")

    except KeyboardInterrupt as ex:

        exexit(KeyboardInterrupt("Interruption clavier"))

    except BaseException as exception:
        exexit(exception)

    finally:
        temps_fin = time()
        temps = temps_fin - temps_début
        print(Fore.LIGHTMAGENTA_EX + "Durée: " + str(temps) + " sec")


def est_premier_séq(nombre: int) -> bool:
    """Détermine si un nombre est premier"""
    if nombre < 1:
        raise ValueError("Le nombre doit être > 0")

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

    if nombre <= 100:
        for n in range(3, racine + 1, 2):
            if nombre % n == 0:
                return False

        # Sinon le nombre est premier
        return True

    else:
        listeProcess = [1, 2, 3, 4]

        process_1 = Process(target=est_premier_parralèle, args=(nombre, 3, racine))
        process_1.start()
        listeProcess[0] = process_1

        process_2 = Process(target=est_premier_parralèle, args=(nombre, 5, racine))
        process_2.start()
        listeProcess[1] = process_2

        process_3 = Process(target=est_premier_parralèle, args=(nombre, 7, racine))
        process_3.start()
        listeProcess[2] = process_3

        process_4 = Process(target=est_premier_parralèle, args=(nombre, 9, racine))
        process_4.start()
        listeProcess[3] = process_4

        process_1.join()
        process_2.join()
        process_3.join()
        process_4.join()

        return bool(process_1.exitcode) and bool(process_2.exitcode) and \
               bool(process_3.exitcode) and bool(process_4.exitcode)


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapport une erreur et termine le programme"""
    print(Fore.YELLOW, "[SF] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex, Fore.RESET,
          file=sys.stderr, sep='')
    sys.exit(exit_code)


def est_premier_parralèle(chiffre: int, chiffre_début: int, resultat_racine: int) -> None:
    sys.stderr = open(os.devnull, 'w')
    setproctitle("SF range(" + str(chiffre_début) + ", " + str(resultat_racine + 1) +
                 ", 8)\n")
    print("* pid " + str(os.getpid()) + " -- range(" + str(chiffre_début) + ", " + str(resultat_racine + 1) +
          ", 8)\n", end='')
    for n in range(chiffre_début, resultat_racine + 1, 8):
        if chiffre % n == 0:
            sys.exit(0)

    # Sinon le nombre est premier
    sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)