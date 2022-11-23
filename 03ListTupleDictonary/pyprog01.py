#!/usr/bin/env python3
from operator import eq
# creating list
list_1 = ["Statistics", "Programming", 2016, 2017, 2018]
list_2 = ['a', 'b', 1, 2, 3, 4, 5, 6, 7 ]

#Accessing values in list
print(f"list_1[0]: {list_1[0]}")
print(f"list_1[0]: {list_2[1:5]}")  

# Updating existing values of list
print(f"Value of list_1: {list_2}")
print(f"Index 2 Value : {list_1[2]}")
list_1[2] = 2015
print(f"Index 2's new value: {list_1[2]}")

# Deleting item from list 
del list_1[2];
print(f"Afther deleting at index 5 : {list_1}")

# Operation on list
print(f"Length: {len(list_1)}")
print(f"Concatenation: {[1,2,3] + [4,5,6]}")
print(f"Repetition: {['Hello'] * 4}")
print(f"Iteration:")
for x in [1,2,3]: print(x)
# negative sign will count from the right 
print(f"slicing : {list_1[-1]}")

# slicing fetches sections
print(f"Slicing range {list_1[2:]}")

# comparing elements of list
print(f"compare two list : [1, 2, 3, ,4] = [1, 2, 3] : {eq([1,2,3, 4 ], [1,2,3])}")

# get max item
print(f"the max item from [1,2,3,4,5] = {max([1,2,3,4,5])}")

# the min item 
print(f"the min item from [1,2,3,4,5] = {min([1,2,3,4,5])}")

# append item to the list 
list_1.append(10)
print(list_1)
