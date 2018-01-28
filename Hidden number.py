# -*- coding: utf-8 -*-

import random


def main():

    x = random.randint(1, 10)
    # print x

    while True:

        guess = int(raw_input("Ugani skrito število med 1 in 10 :"))

        if guess == x:
            print "Bravo"
            break
        elif guess == 0:
            print "Nč v tej igri ne velja. Ugibaj ponovno"
        elif guess >= 11:
            print "Vpisal si previsoko številko. Ugibaš samo od 1 do 10!"


main()
