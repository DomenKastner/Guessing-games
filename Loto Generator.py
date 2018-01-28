# -*- coding: utf-8 -*-

#  Loto Genereator Številk

import random


def stevilke():

    list_st = []

  # for number in range(0, 7):
    for number in range(1):
      # list_st.append(random.sample(0, 40))
        list_st.append(random.sample(xrange(1, 40), 7))  # Če prav zastopim xrange ne ponavlja sekvence x števil?
    return list_st


print "Generirane številke so naslednje: {} ". format(stevilke())

if __name__ == '__stevilke__':
  stevilke()
