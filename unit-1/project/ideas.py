# using images as seeds to modify other images

# import fs, pil, random, sys
from os import listdir, path
from PIL import Image
import random
import sys

# from args choose one image from seeds
seeds = listdir(sys.argv[1])
seed = seeds[random.randrange(len(seeds))]
seed_path = path.join(sys.argv[1], seed)

print("using " + seed_path + " as seed")

# crunch numbers, turn image into a seedable value
# seed_image = Image.open(seed_path)

# seed_image_data = list(seed_image.histogram())

# print(type(seed_image_data))

# seed_number = reduce(lambda a,b: int(a*b), seed_image_data)

# print("seed from " + seed_path + " is " + str(seed_number))

# random.seed(int(seed_number))

# choose a random image from each other folder
candidates = listdir(sys.argv[2])
first_subject = Image.open(path.join(sys.argv[2], candidates[random.randrange(len(candidates))]))

candidates = listdir(sys.argv[3])
second_subject = Image.open(path.join(sys.argv[3], candidates[random.randrange(len(candidates))]))

print("Subjects: " + first_subject.filename + ", " + second_subject.filename)

# do something (seeded) random to them
operation = random.randrange(0, 1)
print(operation)

if operation == 0: # blend em
    print("blending")
    opacity = random.randint(0, 255)
    output = Image.blend(first_subject.resize((300, 300)), second_subject.resize((300, 300)), opacity)
elif operation == 1: # swap palettes
    print("spreading")
    first_subject.effect_spread(25)

output.save("output.jpg")


# blend them?