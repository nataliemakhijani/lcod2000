# imports
import sys
import PIL
import PIL.Image

# Argument parsing
args = sys.argv[1:] # args starting at index = 1
if len(args) < 2: # if there aren't enough args
    print("Not enough arguments") # tell them
    exit(1) # and error
image_name = args[0]
rotation = int(args[1])

# PIL instance initialization
source_image = PIL.Image.open(args[0])
rotated_image = source_image.rotate(rotation)
rotated_image.save("rotated-" + image_name)
