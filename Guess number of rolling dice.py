# -*- coding: utf-8 -*-
import random
# Program simuliranja kocke do številke 6
print("Pozdravljeni v simulatorju metanja igralne kocke")

print("I---------I")
print("I  0      I")
print("I    0    I")
print("I      0  I")
print("I---------I")

while True:

    value = random.randint(1, 6)
    guess = int(raw_input("Ugani na katero številko bo padla kocka? : "))

    if guess != value:
        print ("Škoda, narobe ste uganili! Poskusite še enkrat. ")

    else:
        print (" Bravo")

        break
