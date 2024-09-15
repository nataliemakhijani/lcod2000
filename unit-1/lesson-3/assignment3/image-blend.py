# imports
import sys
from PIL import Image


# Argument parsing
args = sys.argv[1:] # args starting at index = 1
if len(args) < 2: # if there aren't enough args
    print("Not enough arguments") # tell them
    exit(1) # and error

# PIL instance initialization
primary_image = Image.open(args[0])
secondary_image = Image.open(args[1])
blended_image = Image.blend(primary_image, secondary_image, .5) # images don't match error. tried different formats, matching sizes, ez
blended_image.image('blended.jpg')