#!/usr/bin/env python3

"""
Utilisation du module pyInput

Par Sébatien Fortier
"""

import csv
import getpass
import re
import colorama
import argparse
import sys
import pprint
import pyinputplus as pyip
import datetime
from colorama import Fore, Style

colorama.init()

parser = argparse.ArgumentParser(description='Commande pour journaliser un message -- @2020, par Sébastien Fortier',
                                 epilog="Ps si aucun argument n'est fourni, il vous seront demandés.")


def parse_args() -> argparse.Namespace:
    """Gère le arguments passé à la ligne de commande"""

    parser.add_argument('message', type=str, nargs="*", help="Message à journaliser")
    parser.add_argument('-t', metavar='{n,a,e}', type=str, help='Type de log')
    parser.add_argument('--type', metavar='{notification, avertissement, erreur}', type=str, help="Type de log")
    parser.add_argument('-u', '--user', type=str, metavar='USER', help="Nom de l'utilisateur")
    return parser.parse_args()


def main() -> None:
    """Fonction principale"""

    args = parse_args()
    message = ""
    if len(sys.argv) == 1:
        print(Style.BRIGHT + Fore.YELLOW + "[SF]" + Fore.WHITE + " Svp, veuillez entrer votre message et "
                                                                 "facultativemenmt son type et votre nom...")
        try:
            message = pyip.inputStr(limit=5, prompt=Fore.BLUE + "Message: " + Fore.WHITE)
        except Exception as ex:
            print(
                Fore.YELLOW + "[SF] " + Fore.RED + str(
                    ex.__class__.__name__) + Fore.YELLOW + ": La limite du nombre d'essais est atteinte.")
            exit(1)

        message_prompt = Fore.BLUE + "\nType[" + Fore.YELLOW + "1" + Fore.BLUE + "]:\n" + Fore.WHITE
        type_message = pyip.inputMenu(['notification', 'avertissement', "erreur"], prompt=message_prompt, numbered=True,
                                      blank=True)

        nom = pyip.inputStr(blank=True,
                            prompt=Fore.BLUE + "Utilisateur [" + Fore.YELLOW + getpass.getuser() + Fore.BLUE + "]: " +
                                   Fore.WHITE,
                            blockRegexes=[("", Fore.YELLOW + "[SF] " +
                                           Fore.WHITE + "Lettres, chiffres, tirets, espaces et apostrophes seulement "
                                                        "dans le nom svp")], allowRegexes=['^[\w\d_\- \']+$'])

        if type_message == "":
            type_message = "notification"

        if nom == "":
            nom = getpass.getuser()
        # datetime.datetime.today().date()
        date_heure = str(datetime.datetime.today())
        data = {'dateheure': date_heure, 'logtype': type_message, 'message': message, 'utilisateur': nom}

        pprint.pprint(data)

        with open('pylog.tsv', 'a', newline='') as csvFile:
            nom_champs = ['dateheure', 'logtype', 'message', 'utilisateur']
            writer = csv.DictWriter(csvFile, nom_champs, delimiter='\t')

            writer.writeheader()
            writer.writerow({'dateheure': date_heure, 'logtype': type_message, 'message': message,
                             'utilisateur': nom})
    else:
        message = ""
        utilisateur = getpass.getuser()
        type_message = "notification"
        # Modifie le message selon l'argument
        for arg in args.message:
            message += " " + arg
        # Modifie le nom d'utilisateur selon l'argument
        if args.user is not None:
            match = re.search(r'^[\w\d_\- \']+$', args.user)

            if match[0] == args.user:
                utilisateur = args.user
            else:
                print(
                    Fore.YELLOW + "[SF] " + Fore.RED + "ValueError: " + Fore.YELLOW +
                    "Lettres, chiffres, tirets, espaces "
                    "et apostrophes seulement "
                    "dans le nom svp")
                exit(1)
        # Modifie le type de message selon l'argument
        if args.t is not None or args.type is not None:
            if args.t == "a" or args.type == "avertissement":
                type_message = "avertissement"
            elif args.t == "n" or args.type == "notification":
                type_message = "notification"
            elif args.t == "e" or args.type == "erreur":
                type_message = "erreur"
            else:
                # parser.print_usage()
                if args.t is not None:
                    parser.error(
                        'pylog.py: erreur: argument -t: choix invalide: \'' + args.t + '\' (parmi \'n\',\'a\',\'e\')')
                elif args.type is not None:
                    parser.error(
                        'pylog.py: erreur: argument -t: choix invalide: \'' + args.type +
                        '\' (parmi \'notification\',''\'avertissement\',\'erreur\')')

                exit(1)

        date_heure = str(datetime.datetime.today())
        data = {'dateheure': date_heure, 'logtype': type_message, 'message': message, 'utilisateur': utilisateur}
        pprint.pprint(data)

        try:
            with open('pylog.tsv', 'a', newline='') as csvFile:
                nom_champs = ['dateheure', 'logtype', 'message', 'utilisateur']
                writer = csv.DictWriter(csvFile, nom_champs, delimiter='\t')

                writer.writeheader()
                writer.writerow({'dateheure': date_heure, 'logtype': type_message, 'message': message,
                                 'utilisateur': utilisateur})
        except Exception as ex:
            print(
                Fore.YELLOW + "[SF] " + Fore.RED + str(
                    ex.__class__.__name__) + ":" + Fore.YELLOW + str(ex))
            exit(1)






if __name__ == '__main__':
    main()
