# PATH ~/sbox/lpthw/mystuff/ex16.py

from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^c).")
print("If you do want that, hit RETURN.")