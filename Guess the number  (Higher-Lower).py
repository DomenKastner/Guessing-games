# -*- coding: utf-8 -*-

print("Welcome to Guess the number")

skritostevilo = 69
guess = 0

while guess != "skritostevilo":
    skritostevilo = int(raw_input("Ugani številko od 1 do 99: "))

    if skritostevilo < 69:
        print "Vpisal si prenizko številko"
    elif skritostevilo > 69:
        print " Vpisal si previsoko številko"

    else:
        print "Čestitke! Uganil si pravo številko"
        break