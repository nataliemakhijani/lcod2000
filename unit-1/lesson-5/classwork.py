# should set up a jupyter notebook for this class
import random
from os import listdir, path
from PIL import Image

width = 100
height = 100

#
# Generate some RGB static
#
img = Image.new("RGB", (width, height), (0,0,0)) # init new image w black fill

for y in range(height):
    for x in range(width):
        red = random.randrange(0, 255)
        green = random.randrange(0, 255)
        blue = random.randrange(0, 255)

        img.putpixel((x,y), (red, green, blue))

img.save('./img-rgb-static.png')

#
# random image choice
#

files = listdir("images")
# files.remove(".DS_Store")

random_file = random.choice(files)

img = Image.open( path.join("images",random_file) )
