#!/usr/bin/env python3
"""
Application:
Written by: Dicxie Madrigal <dicxiemadrigal@gmail.com>
Purpose: Guess number program
"""
from random import randint
print("\t\tWelcome to 'Guess my number'")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")
theNumber = randint(1,100)
guess =int(input("Take a guess: "))
tries = 1
#guess loop
while guess != theNumber:
    if guess > theNumber:
        print("Lower...")
    else:
        print("Higher...")
    
    guess =int(input("Take a guess: "))
    tries += 1

print("You guessed it! The number was", theNumber)
print("And it only took you", tries, "tries!\n")
input("\n\nPress the enter key to exit.")