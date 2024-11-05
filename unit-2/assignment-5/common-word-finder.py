import re


input_raw = open("decorative-gourd-season-motherfucker.txt", "r")

# input_text = re.sub(r'[^\w\s]', '', input_raw)

ignore_words = ["the", "a"]
counter = {}

for word in input_text.split(' '):
    if word not in ignore_words:
        counter[word] += 1

