#!/usr/bin/env python3
# Gues my number Game 
from random import randint, randrange

#generate random numbers 1 - 6
die1 = randint(1, 6)
die2 = randrange(6) +1
total = die1 +die2

print(f"yuor rolled a {die1} and a {die2} for a total {total} ")
input("\n\nPress the enter to exit")
