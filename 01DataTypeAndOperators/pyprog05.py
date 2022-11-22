#!/usr/bin/env python3

"""
@description practicing bitwise Operators
@version 1.0
& binary and
| binary or
^ binary xor
~ binary one complement
<< binary left shift
>> binary right shift
"""

# Basic six  bitwise operators
# let x = 10 (in binary 1010) and  y = 4 (in binary 01000)
x = 10 
y = 4
print(x >> y)
print(x << y)
print(x & y)
print(x | y)
print(x ^ y)
print( ~x )