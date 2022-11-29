#!/usr/bin/env python3
"""
Application: pyprog10.py
Written by: Dicxie Madrigal <dicxiemadrigal@gmail.com>
Purpose: Show how to use Date and Time
"""
from datetime import datetime
print(datetime.now())   #Get the current date and time by using the now() fuction

print(str(datetime.now().date())) # get the current date use the method date()
print(str(datetime.now().time()))