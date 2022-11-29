#!/usr/bin/env python3
"""
Application:
Written by: Dicxie Madrigal <dicxiemadrigal@gmail.com>
Purpose: Example of not sentences
"""

security = 0
username = ""
password = ""

while not username:
    username = input("Username: ")

while not password:
    password = input("Password: ")

if username == "M. Dicxie" and password == "secret":
    print("Hi, Dicxie")
    security = 5
elif username == "C. Jose" and password == "secret1":
    print("Hey, Carlos.")
    security = 3
elif username == "P. Morales" and password == "secret":
    print("Hey, Pedro")
    security = 3
elif username == "guest" and password == "guest":
    print("Welcome, Guest")
    security = 1
else: 
    print("Login failed. You're not so exclusive.\n")

input("\n\nPress the Enter key to exit...\n")
