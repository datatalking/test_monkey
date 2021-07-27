# PATH ~/sbox/lpthw/mystuff/ex15.py

# imports sys module from argv
from sys import argv

# creates a script at position 0 and 1 as argument variables
# the script becomes the filename of the python script in this case ex15.py
script, filename = argv

# sets the txt as variable to open the filename as an object
txt = open(filename)

# prints a string and includes filename as f string
print("Here's your file %r:" % filename)

# prints txt, calls read method to filename
print(txt.read())

# prompts user to type filename again string
print("Type the filename again:")

# creates file_again object to collect input of a string symbol
file_again = input("> ")

# creates txt_again object that holds the open method of file_again
txt_again = open(file_again)

# prints txt_again with read method of whats inside it
print(txt_again.read())

# prints the script we typed out here 
print(script)

