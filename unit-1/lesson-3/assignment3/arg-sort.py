# imports
import sys

# 
# Problem 1
# python3 arg-sort.py aaa ccc bbb 
# 
word_list = sorted(sys.argv[1:4]) # use 1: to select subset of list starting at index = 1 to index = 4 to exclude filename passed to python3, then sort it

print("alphabetically organized word list:", word_list)

