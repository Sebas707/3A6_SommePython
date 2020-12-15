#!/usr/bin/env python3

"""
Programme multi-processus pour déterminer si un nombre est premier

2020, Sébastien Fortier
"""

import argparse
import multiprocessing

import colorama
from colorama import Fore, Style
from typing import NoReturn
import math
from set_proc_title import setproctitle
import os
import sys
from timeit import default_timer as time
from multiprocessing import Process
import multiprocessing as mp
from typing import List

colorama.init()



def parse_args(arg: List[str]) -> argparse.Namespace:
    """Gère le arguments passé à la ligne de commande"""
    parser = argparse.ArgumentParser(description='Détecteur de nombres premier -- 2020, par Sébastien Fortier')

    parser.add_argument('nombre', type=int, nargs=1, help="Nombre à traiter pour connaître sa primalité")
    parser.add_argument('-d', '--délai', metavar='DÉLAI', type=float, help='Délai pour le calcul (défaut 10 sec)')
    parser.add_argument('-e', '--explication', action='store_true', help='Expliquer pourquoi non premier')
    parser.add_argument('-p', '--processus', metavar='PROCESSUS', type=int, help='Nombre de processus à utiliser'
                                                                                   '(défaut 4)', default=4)
    parser.add_argument('-t', '--trace', action='store_true', help='Activer la trace d''exécution')
    parser.add_argument('-q', '--quiet', action='store_true', help='Ne pas afficher les processus')

    return parser.parse_args(arg)


def main(argv: List[str]) -> None:
    """Fonction principale"""
    temps_début = time()
    args = parse_args(argv[1:])


    try:
        if len(argv) == 1:
            raise IndexError("La commande doit avoir au moins un argument")

        est_nombre_premier = est_premier_séq(args.nombre[0], args)

        if est_nombre_premier:
            print(Fore.LIGHTBLUE_EX + "Selon Seb Fortier: Oui")
        else:
            print(Fore.LIGHTBLUE_EX + "Selon Seb Fortier: Non")
        temps_fin = time()
        temps = temps_fin - temps_début
        print(Fore.LIGHTMAGENTA_EX + "Durée: " + str(temps) + " sec")

    except KeyboardInterrupt as ex:
        temps_fin = time()
        temps = temps_fin - temps_début
        print(Fore.YELLOW, "[SF] ",
              Fore.RED, KeyboardInterrupt.__class__.__name__,
              Fore.YELLOW, ": ", KeyboardInterrupt, Fore.RESET,
              file=sys.stdout, sep='')
        print(Fore.LIGHTMAGENTA_EX + "Durée: " + str(temps) + " sec")
        sys.exit(1)

    except BaseException as exception:
        exexit(exception)


def est_premier_séq(nombre: int, arg: argparse.Namespace) -> bool:
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
        nombre_processus = arg.processus

        if arg.processus == 0:
            nombre_processus = mp.cpu_count()
        elif arg.processus < 0:
            nombre_processus = mp.cpu_count() + arg.processus

        listeProcess = list(range(0, nombre_processus))



        if arg.quiet:

            for i in range(1, nombre_processus + 1):
                listeProcess[i - 1] = Process(target=est_premier_parralèle, args=(nombre, i * 2 + 1, racine, nombre_processus))

                listeProcess[i - 1].start()

            for process in listeProcess:
                process.join()

            for process in listeProcess:
                if not bool(process.exitcode):
                    return False
            return True
        else:

            for i in range(1, nombre_processus + 1):
                listeProcess[i - 1] = Process(target=est_premier_parralèle, args=(nombre, i * 2 + 1, racine, nombre_processus))

                listeProcess[i - 1].start()

                print("* pid " + str(listeProcess[i - 1].pid) + " -- range(" + str(i * 2 + 1) + ", " + str(racine + 1) +
                      "," + str(nombre_processus * 2) + ")")



            for process in listeProcess:
                process.join()

            for process in listeProcess:
                if not bool(process.exitcode):
                    return False
            return True





def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapport une erreur et termine le programme"""
    print(Fore.YELLOW, "[SF] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex, Fore.RESET,
          file=sys.stderr, sep='')
    sys.exit(exit_code)


def est_premier_parralèle(chiffre: int, chiffre_début: int, resultat_racine: int, nb_proce: int) -> None:
    sys.stderr = open(os.devnull, 'w')
    setproctitle("SF range(" + str(chiffre_début) + ", " + str(resultat_racine + 1) +
                 ", 8)\n")

    for n in range(chiffre_début, resultat_racine + 1, nb_proce * 2):
        if chiffre % n == 0:
            sys.exit(0)

    # Sinon le nombre est premier
    sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
