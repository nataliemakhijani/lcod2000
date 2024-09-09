score = 28 # set score to 28 <- this is a comment
# variable assigned to value 28
# print(score) # print the value of score

name = "natalie"

print(name)

count = 0

while count < 10: # while loop that runs until count is 10
    count += 1
    print(count)

names = ["natalie", "aanya", "rae"] # initialize array with 3 names
name_count = len(names) # python len() function returns the number of items in a list

print("name count:", name_count) # print w multiple args joins them with space
print(names[0])

for name in names: # for loop iterating over names arr
    print(name) 

for i, name in enumerate(names): # enumerate returns index and value
    print(i, name) # print em both