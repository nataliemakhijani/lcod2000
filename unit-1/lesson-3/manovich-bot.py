# py stuff
import sys
import random

from manovichdata import numerical, modularity, automation, variability, transcoding # my stuff

shit_dudes_say = { # create a dictionary of all our lists (imported above)
    'numerical': numerical,
    'modularity': modularity,
    'automation': automation,
    'variability': variability,
    'transcoding': transcoding
}

if len(sys.argv) < 2: # if there isn't a second argument
    print("not enough args") # error
    exit(1) # and exit
elif not sys.argv[1] in shit_dudes_say.keys(): # if the second argument isn't one of the principles
    print("not a valid theme") # error
    exit(1) # and exit
else: # otherwise
    theme = shit_dudes_say.get(sys.argv[1]) # set 'theme' to equal the correct list from the dictionary

    item = random.randrange(len(theme)) # generate a pseudorandom number between 0 and the length of the list from the dictionary

    print(theme[item]) # print the item from the list at the random index



# theme = sys.argv[1]

# if theme == 'numerical':
#     print(numerical)
# elif theme == 'modularity':
#     print(modularity)
# elif theme == 'automation':
#     print(automation)
# elif theme == 'variability':
#     print(variability)
# elif theme == 'transcoding':
#     print(variability)