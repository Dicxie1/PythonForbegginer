#!/usr/bin/env python3

score = int(input("Score (100-0):"))
if score >= 99:
    print("your score is A")
elif score >= 75:
    print("your score is B")
elif score >= 60:
    print("your score is C")
elif score >= 35:
    print("your score is D")
else: 
    print("your score is F")