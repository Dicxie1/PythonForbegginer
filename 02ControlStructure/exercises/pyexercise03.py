#!/usr/bin/env python3

# python program what determinate if a word us isogram 
# Definition: An isogram is a word that has no repeating letters
# Execise:
# Implement a function that determines whether a string that contains 
# only letters is an isogram.

def is_isogram(text = ""):
    text = text.lower()
    for character in text:
        if text.count(character) > 1:
            return False
    return True


print(f"the word All is isogram? = {is_isogram('aba')}")

print(f"{len(set('ALL'.lower()))} is equal to {len('ALL')}")           
