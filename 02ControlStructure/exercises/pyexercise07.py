#!/usr/bin/env python3
"""
Application:
Written by:
Purpose: Program that simulate a fortune cookies. Display a random message 
"""
from random import randint
cookies = ["Whe one door close, another opens.",
           "Luky is comimg your way",
           "you will overcome difficult time",
           "Come to the dark side we have cookies",
           "Your pet is planing to eat you"]
guess = randint(0,4)
print("\n\t\tWelcome to the fortune cokkies simulate program")
print("The message for you is:")

if guess == 0:
    print(cookies[guess])
if guess == 1:
    print(cookies[guess])
if guess == 2:
    print(cookies[guess])
if guess == 3:
    print(cookies[guess])
if guess == 4:
    print(cookies[guess])
input("\nPress the Enter key to exit...")