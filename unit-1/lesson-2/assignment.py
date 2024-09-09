from unit1lesson2 import *

# smallest number
smallest = number_list[0] # set smallest to first number, will compare against this
for number in number_list:
    if number < smallest: # if it's smaller than the current smallest, 
        smallest = number # it becomes the new number to compare against
print("smallest number", smallest) # 175
# can this be done as a one-liner? probably.
# could also be done recursively

# smallest number above 500
numbers_above_500 = [num for num in number_list if num > 500] # filter out all numbers < 500, not very legible though
smallest = numbers_above_500[0]
for number in numbers_above_500:
    if number < smallest: # if it's smaller than the current smallest, it becomes the new number to compare against
        smallest = number
print("smallest number above 500", smallest) # 501

# smallest even
evens = [num for num in number_list if num % 2 == 0]
smallest = evens[0]
for number in evens:
    if number < smallest: # if it's smaller than the current smallest, it becomes the new number to compare against
        smallest = number
print("smallest even", smallest) #176

# find last word (alpha) in list
last_word = sorted(word_list)[-1]
print("last_word:", last_word) # violation

# if we do it without sorted
last_word = word_list[0]
for word in word_list:
    if word > last_word:
        last_word = word
print("last (w/o sorted):", last_word)

# longest word
longest = ""
for word in word_list:
    if len(word) > len(longest):
        longest = word
print("longest word is", longest) # rehabilitation
