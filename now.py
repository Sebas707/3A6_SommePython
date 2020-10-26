#!/usr/bin/env python3

"""
Programme qui affiche des informations sur la date et le temps

Par Sébastien Fortier
"""

import datetime



def main() -> None:
    """Fonction principale"""

    date_noel = datetime.datetime(datetime.datetime.today().year, 12, 25)
    nb_jours_avant_noel = date_noel - datetime.datetime.today()

    print("maintenant: " + str(datetime.datetime.today()))
    print("aujourd'hui: " + str(datetime.datetime.today().date()))
    print("demain: " + str(datetime.datetime.today().date() + datetime.timedelta(days=1)))
    print("avant-hier: " + str(datetime.datetime.today().date() + datetime.timedelta(days=-2)))
    print("noel: " + str(datetime.date.today().year) + "-12-25")
    print("noel dans: " + str(nb_jours_avant_noel.days) + " jours")




if __name__ == '__main__':
    main()