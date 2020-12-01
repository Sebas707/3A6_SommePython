#!/usr/bin/env python3

"""
Programme pour évaluer une expression Python
(version sécuritaire, avec durée limitée, et professionnelle)

2020, Sébastien Fortier
"""

from typing import NoReturn

import colorama
from colorama import Fore, Style
from m_safe_eval import safe_eval as eval  # noqa
from m_timeout_eval import timeout_eval as eval  # noqa
import sys
import argparse
import time

colorama.init()

def parse_args() -> argparse.Namespace:
    """Gère les arguments passés à la ligne de commande"""
    parser = argparse.ArgumentParser(description='Évaluateur d''expression Python -- @2020, par Sébastien Fortier')
    parser.add_argument('code', metavar='code', type=str, nargs="+", help="Expression à évaluer")

    parser.add_argument('-d', '--délai', metavar='DÉLAI', type=float, default=2,
                        help='Délai pour le calcul (défaut 2 sec)')
    parser.add_argument('-m', '--minuté', action="store_true", help='Minuter la durée d''exécution')

    return parser.parse_args()


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapport une erreur et termine le programme"""
    print(Fore.YELLOW, "[SF] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex, Fore.RESET,
          file=sys.stderr, sep='')
    sys.exit(exit_code)


def verifier_erreur(délai_exécution: float) -> None:
    if délai_exécution <= 0:
        print(
            Fore.YELLOW + "[SF] " + Fore.RED + "ValueError" + Fore.YELLOW + ": Le délai doit être supérieur à 0" + Fore.RESET)
        exit(1)
    if délai_exécution > 5:
        print(
            Fore.YELLOW + "[SF] " + Fore.RED + "ValueError" + Fore.YELLOW + ": Le délai doit être au plus 5 secondes" + Fore.RESET)
        exit(1)


def main() -> None:
    """Fonction principale"""
    temps_début = time.time()
    args = parse_args()

    verifier_erreur(args.délai)

    try:
        evaluation = eval(' '.join(args.code) or "None", delai_sec=args.délai)
        print(Fore.CYAN + "Selon Seb Fortier:", Fore.RESET, evaluation)

    except TimeoutError:
        # Pour afficher un message d'erreur personalisé
        exexit(TimeoutError("Le délai de " + str(args.délai) + " secondes est écoulé."))

    except KeyboardInterrupt:
        exexit(KeyboardInterrupt("Interrompu par l'utilisateur"))

    except Exception as ex:
        exexit(ex)



    finally:
        temps_fin = time.time()
        temps = temps_fin - temps_début
        if args.minuté:
            print(Fore.MAGENTA + "Durée: " + str(temps) + " sec")


if __name__ == '__main__':
    main()
