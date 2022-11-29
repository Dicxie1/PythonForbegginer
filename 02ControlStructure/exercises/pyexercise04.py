#!/usr/bin/env python3
"""
Application: pyexercise.04.py
Written by: Dicxie Madrigal <dicxiemadrigal@gmail.com>
Purpose: Example how to use while loop
"""
print("\tWelcome to the 'Three-Year-Old Simulator'\n")
print("This Program simulates a conversation with a three-year-old child.")
print("Try to stop the madnees.\n")

reponse = ""
while reponse != "Because.":
    reponse = input("Why?\n>")

print("Oh. Okay.")
input("\n\nPress the Enter key to exit")