# 2024-09-09
# Natalie Makhijani
import sys # builtin
from PIL import Image

args = sys.argv
args.pop(0) # remove first arg

image = Image.open(args[0])

print(image.format_description)
