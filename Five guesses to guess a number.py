# -*- coding: utf-8 -*-

print ("Ugani skrito številko v petih poskusih")

secret = 22
max_ugibanj = 5

# for st_ugibanj in range(max_ugibanj):
for st_ugibanja in range(1, max_ugibanj + 1):

    guess = int(raw_input("Enter number :"))
    if guess == secret:
        print("Jackpot! Uganil si pravo številko")
        break

    else:
        print("Wroooong!")

if guess != secret:
    print("Porabil si vse možnosti ugibanj. Na voljo ste jih imeli " + str(max_ugibanj) + ".")
