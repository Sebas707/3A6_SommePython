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
import os
import webbrowser
import pprint
from tabulate import tabulate
import pyinputplus as pyip
import datetime
import os.path
from colorama import Fore, Style

colorama.init()

parser = argparse.ArgumentParser(description='Commande pour journaliser un message -- @2020, par Sébastien Fortier',
                                 epilog="Ps si aucun argument n'est fourni, il vous seront demandés.")


def parse_args() -> argparse.Namespace:
    """Gère le arguments passé à la ligne de commande"""

    parser.add_argument('message', type=str, nargs="*", help="Message à journaliser")
    parser.add_argument('-t', metavar='{n,a,e}', type=str, help='Type de log')
    parser.add_argument('-l', '--list', action='store_true', help='Afficher les logs')
    parser.add_argument('-b', '--browse', action='store_true', help='Afficher les logs dans le navigateur')
    parser.add_argument('--type', metavar='{notification, avertissement, erreur}', type=str, help="Type de log")
    parser.add_argument('-u', '--user', type=str, metavar='USER', help="Nom de l'utilisateur")
    return parser.parse_args()


def main() -> None:
    """Fonction principale"""

    args = parse_args()
    message = ""
    if args.browse:
        afficher_log_browse()

    if len(sys.argv) == 1:
        print(Style.BRIGHT + Fore.YELLOW + "[SF]" + Fore.WHITE + " Svp, veuillez entrer votre message et "
                                                                 "facultativemenmt son type et votre nom...")

        message = modifier_message()

        message_prompt = Fore.BLUE + "\nType[" + Fore.YELLOW + "1" + Fore.BLUE + "]:\n" + Fore.WHITE
        type_message = pyip.inputMenu(['notification', 'avertissement', "erreur"], prompt=message_prompt, numbered=True,
                                      blank=True)

        nom = pyip.inputStr(blank=True,
                            prompt=Fore.BLUE + "Utilisateur [" + Fore.YELLOW + getpass.getuser() + Fore.BLUE + "]: " +
                                   Fore.WHITE,
                            blockRegexes=[("", Fore.YELLOW + "[SF] " +
                                           Fore.WHITE + "Lettres, chiffres, tirets, espaces et apostrophes seulement "
                                                        "dans le nom svp")], allowRegexes=['^[\w\d_\- \']+$'])

        type_message = transformation_type_message(type_message)

        nom = transformation_nom(nom)

        date_heure = str(datetime.datetime.today())
        data = {'dateheure': date_heure, 'logtype': type_message, 'message': message, 'utilisateur': nom}

        pprint.pprint(data)

        écrire_log(date_heure, type_message, message, nom)

    else:
        if not args.list:
            message = ""
            utilisateur = getpass.getuser()

            # Modifie le message selon l'argument
            for arg in args.message:
                message += " " + arg
            # Modifie le nom d'utilisateur selon l'argument
            if args.user is not None:
                utilisateur = verifie_utilisateur(args)

            # Modifie le type de message selon l'argument
            type_message = verifie_argument(args)

            date_heure = str(datetime.datetime.today())
            data = {'dateheure': date_heure, 'logtype': type_message, 'message': message, 'utilisateur': utilisateur}
            pprint.pprint(data)

            try:
                with open('pylog.tsv', 'a', newline='') as csvFile:
                    nom_champs = ['dateheure', 'logtype', 'message', 'utilisateur']
                    writer = csv.DictWriter(csvFile, nom_champs, delimiter='\t')

                    if os.stat("pylog.tsv").st_size == 0:
                        writer.writeheader()
                        writer.writerow({'dateheure': date_heure, 'logtype': type_message, 'message': message,
                                         'utilisateur': utilisateur})
                    else:
                        writer.writerow({'dateheure': date_heure, 'logtype': type_message, 'message': message,
                                         'utilisateur': utilisateur})

            except Exception as ex:
                print(
                    Fore.YELLOW + "[SF] " + Fore.RED + str(
                        ex.__class__.__name__) + ":" + Fore.YELLOW + str(ex))
                exit(1)
        else:
            if not args.message:
                with open('pylog.tsv', 'r', newline='') as tsvfile:
                    print(tabulate(csv.reader(tsvfile, delimiter='\t'), headers="firstrow"))
            else:
                parser.print_usage()
                print(Fore.YELLOW + "[SF] " + Fore.RED + "ArgumentError" +
                      Fore.YELLOW + ": Il faut spécifier un et un seul argument parmi: -l, message")


def écrire_log(date_heure: str, type_message: str, message: str, nom: str) -> None:
    try:
        with open('pylog.tsv', 'a', newline='') as csvFile:
            nom_champs = ['dateheure', 'logtype', 'message', 'utilisateur']
            writer = csv.DictWriter(csvFile, nom_champs, delimiter='\t')

            if os.stat("pylog.tsv").st_size == 0:
                writer.writeheader()
                writer.writerow({'dateheure': date_heure, 'logtype': type_message, 'message': message,
                                 'utilisateur': nom})
            else:
                writer.writerow({'dateheure': date_heure, 'logtype': type_message, 'message': message,
                                 'utilisateur': nom})

    except Exception as ex:
        print(
            Fore.YELLOW + "[SF] " + Fore.RED + str(
                ex.__class__.__name__) + ":" + Fore.YELLOW + str(ex))
        exit(1)


def modifier_message() -> str:
    message = ""
    try:
        message = pyip.inputStr(limit=5, prompt=Fore.BLUE + "Message: " + Fore.WHITE)
    except Exception as ex:
        print(
            Fore.YELLOW + "[SF] " + Fore.RED + str(
                ex.__class__.__name__) + Fore.YELLOW + ": La limite du nombre d'essais est atteinte.")
        exit(1)

    return message


def verifie_utilisateur(args: argparse.Namespace) -> str:
    utilisateur = getpass.getuser()

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

    return utilisateur


def transformation_nom(nom: str) -> str:
    if nom == "":
        nom = getpass.getuser()

    return nom


def transformation_type_message(type_message: str) -> str:
    if type_message == "":
        type_message = "notification"

    return type_message


def afficher_log_browse() -> None:
    with open('pylog.tsv', 'r', newline='') as tsvfile:
        if os.name == 'posix':
            print(tabulate(csv.reader(tsvfile, delimiter='\t'), headers="firstrow", tablefmt="html"))
        else:
            with open('pylog.html', 'w') as page:
                message = """<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">\n"""
                message += tabulate(csv.reader(tsvfile, delimiter='\t'), headers="firstrow", tablefmt="html")
                message = message.replace('<table>', '<table class="table">')
                page.write(message)
                page.close()
            webbrowser.open_new_tab(f'file:///{os.getcwd()}/pylog.html')
            sys.exit(0)

        exit(0)


def verifie_argument(args: argparse.Namespace) -> str:
    type_message = "notification"
    if args.t is not None or args.type is not None:
        type_message = transformer_argument(args)

    return type_message


def transformer_argument(args: argparse.Namespace) -> str:
    type_message = "notification"

    if args.t == "a" or args.type == "avertissement":
        type_message = "avertissement"
    elif args.t == "n" or args.type == "notification":
        type_message = "notification"
    elif args.t == "e" or args.type == "erreur":
        type_message = "erreur"
    else:
        if args.t is not None:
            parser.error(
                'pylog.py: erreur: argument -t: choix invalide: \'' + args.t + '\' (parmi \'n\',\'a\',\'e\')')
        elif args.type is not None:
            parser.error(
                'pylog.py: erreur: argument -t: choix invalide: \'' + args.type +
                '\' (parmi \'notification\',''\'avertissement\',\'erreur\')')
        exit(1)

    return type_message


if __name__ == '__main__':
    main()
