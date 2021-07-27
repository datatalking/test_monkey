# PATH ~/sbox/lpthw/mystuff/ex13.py

from sys import argv # imports argv from sys and not the whole sys module

script, first, second, third = argv # sets variables as argv

print("The script is called:", script) # prints str followed by var as argv
print("Your first variable is:", first) # prints str followed by var as argv
print("Your second variable is:", second) # prints str followed by var as argv
print("Your third variable is:", third) # prints str followed by var as argv

# argv requires inputs from the command line at run time
# input requires inputs from the user after run time