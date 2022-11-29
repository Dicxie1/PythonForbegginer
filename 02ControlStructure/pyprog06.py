#!/usr/bin/env python3
"""
Application:
Written by: Dicxie Madrigal <dicxiemadrigal@gmail.com>
Purpose: Example of key word break and continue
"""
count = 0
while True:
    count += 1
    if count > 10:
        break
    if count == 5:
        continue
    print(count)

input("\n\nPress the Enter Key to exit...\n")