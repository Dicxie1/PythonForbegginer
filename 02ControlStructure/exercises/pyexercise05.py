#!/usr/bin/env python3
"""
Application: pyexercise05.py
Written by: Dicxie Madrigal <dicxiemadrigal@gmail.com>
Purpose: Demostration of infinite loop
"""
print("You lone hero is surrounded by a massive army of trolls")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sword fon the last fight of his life.\n")

health = 10
trolls = 0
damage = 0

while health != 0:
    trolls += 1
    health -= damage
    print(f"Your hero swings and defeats an evil troll but takes, {damage} damage points")

print(f"Your hero fought valiantly and defeated {trolls} trolls")
print(f"But alas, your hero")

input("\n\nPress the Enter key to exit")