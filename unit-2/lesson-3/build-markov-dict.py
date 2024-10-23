input_raw = open("decorative-gourd-season-motherfucker.txt", "r")

input_text = input_raw.read().split(" ")

probability_dict = {}

for i, word in enumerate(input_text[1:]):
    # make sure word exists in prob dict
    if not word in probability_dict:
        probability_dict[word] = {}

    if not input_text[i] in probability_dict[word]:
        probability_dict[word][input_text] = 1
    else:
        probability_dict[word][input_text] = probability_dict[word][input_text]+1

print(probability_dict)

# currently doesnt work