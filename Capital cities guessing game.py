# -*- coding: utf-8 -*-

#Program, ki omogoča ugibanje glavnega mesta evropskih držav

import random

def preveri_drzavo(ugibano, drzave_mesta_dict, ugibana_drzava):
    if ugibano.lower() == drzave_mesta_dict[ugibana_drzava]:   # Preveri ali je odgovor pravi
        print("Bravo uganili ste")
    else:
        print("Narobe")

def izberi_nakljucno_drzavo(drzave_mesta_dict):
    cifra_drzave = random.randint(0, len(drzave_mesta_dict) -1)
    return drzave_mesta_dict.keys()[cifra_drzave]

def main():

    drzave_mesta_dict = {
        "Slovenije": "ljubljana",
        "Avstrije": "dunaj",
        "Nemčije": "berlin",
        "Hrvaske": "zagreb",
    }

    print("pozdravljen v igrici: Glavna mesta držav")

    while True:

        drzava = izberi_nakljucno_drzavo(drzave_mesta_dict)

        ugibano = raw_input("Ugani glavno mesto " + drzava)

        preveri_drzavo(ugibano, drzave_mesta_dict, drzava)

        cont = raw_input("Želiš nadaljevati y/n?")
        if cont == "n":
            break

    print("Adijo")

if __name__ == '__main__':
    main()