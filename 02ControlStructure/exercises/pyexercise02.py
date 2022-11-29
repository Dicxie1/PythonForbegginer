#¡/usr/bin/env python3
# mood computer program
"""
Application: pyexercise02.py
Written by: Dicxie Madrigal <dicxiemadrigal@gmail.com>
Purpose: Exercises describe how to use if sentences
"""
from random import randint

print("I sense your energy. Your true emotion are coming across my screen.")
print("You are ....")

mood = randint(1, 3) # generate random number between 1 to 3
if mood == 1:
    # happy
    print(
        """
        ___________
        |         |
        | 0     0 |
        |    <    |
        |         |
        | .     . |
        |  ´    ´ |
        |   ...   |
        |_________|
        """)
elif mood == 2:
    # neutral
    print(
        """
        ___________
        |         |
        | 0     0 |
        |    <    |
        |         |
        |         |
        | ....... |
        |         |
        |_________|  
        """)
elif mood == 3:
    # sad
    print(
        """
        ___________
        |         |
        | 0     0 |
        |    <    |
        |         |
        |    .    |
        |  ´   `  |
        | ´    `  |
        |_________|
        """) 
else: 
    print("Illegal mood value! (you must be in a really bad mood)")
print("....today")
input("\n\nPress the Enter key to exit")