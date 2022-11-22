#!/uisr/bin/env python3 

"""
Write a python program to multiplies all the items in a list
"""
sum  = 1 # inicialize the variable in 1
items = [10, 20, 2, 4]
for item in items:
    sum *= item
print(f"the result is: {sum}")