#!/usr/bin/env python3
"""
Application:
Written by: Dicxie Madrigal <dicxiemadrigal@gmail.com>
Purpose: Demostrates the range() function
"""
print("Counting")
for i in range(10):
    print(i, end= " ")
print("\n\nCounting by fives:")
for i in range(0, 50, 5):
    print(i, end= " ")
print("\n\nCounting backwards:")
for i in range(10, 0 , -1):
    print(i, end= " ")
print("\n\nPress Enter key to exit...")