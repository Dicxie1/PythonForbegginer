#!/usr/bin/env python3
course = "Python"
name = "Dicxie"
age = 26
print("Welcome to programming in Python my name ") 
# string interopate
print("Welcome to programming in " + course + " my name is " + name + " i'm " + str(age) + " years old") 
print("Welcome to programming in {} my name is {} i'm {} years old ".format(course, name, age))
print(F"Welcome to programming in {course} my name is {name} i'm {age} years old")

type_of_people = 10
x =f"There are {type_of_people} type of people."
binary = "binary"
do_not = "don't"
y =f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

print('.' * 10) # display: ..........
print("example", "\N{ASTERISK}"*20, "\N{CAPITULUM}")

