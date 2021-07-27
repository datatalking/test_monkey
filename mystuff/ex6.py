# -*- coding: utf-8 -*-
# filename ~/sbox/LPTHW/mystuff/ex6.py
# First retype from book
# Second comment each line
# Git push to repo

x = "There are %d types of people." % 10 # sets x as a string with decimal value
binary = "binary" # sets binary variable as the word binary str
do_not = "don't" # sets do_not variable as don't contraction str
y = "Those who know %s and those who %s." % (binary, do_not) # y becomes f str 

print(x) # display value for x
print(y) # display value for y

print("I said: %r." %x) # prints python representation of x variable
print("I also said: '%s'." %y) # prints python str of y variable

hilarious = True # set variable hilarious to False value
joke_evaluation = "Isn't that joke so funny?! %r" # sets joke_evaluation variable to a string with python rep

print(joke_evaluation % hilarious) # print joke_evaluation and hilarious values together

w = "This is the left side of ..." # sets w to a string
e = "a string with a right side." # sets e to a string

print(w + e) # print W then e with no space