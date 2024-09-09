from unit1lesson2 import *

smallest = number_list[0]

for number in number_list:
    if number < smallest: # if it's smaller than the current smallest, it becomes the new number to compare against
        smallest = number

print("smallest number", smallest) # 175
# true

numbers_above_500 = [num for num in number_list if num > 500]

smallest = numbers_above_500[0]

for number in numbers_above_500:
    if number < smallest: # if it's smaller than the current smallest, it becomes the new number to compare against
        smallest = number

print("smallest number above 500", smallest) # 501

evens = [num for num in number_list if num % 2 == 0]

smallest = evens[0]

for number in evens:
    if number < smallest: # if it's smaller than the current smallest, it becomes the new number to compare against
        smallest = number

print("smallest even", smallest) #176

last_word = sorted(word_list)[-1]

print(last_word) # violation

longest = ""

for word in word_list:
    if len(word) > len(longest):
        longest = word

print("longest word is", longest) # rehabilitation
