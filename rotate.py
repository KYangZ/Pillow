import os, sys
from PIL import Image, ImageEnhance

# set the path so we can reference things in the current directory
my_path = os.path.dirname(__file__)

# open the image with Image.open()
im = Image.open(my_path + "images/left_facing_dog.png")
print(im.format, im.size, im.mode)
im.show() # show the initial image

im = im.rotate(45)
im.show() # show the rotated image

im = im.transpose(Image.FLIP_TOP_BOTTOM)
im.show() # show the flipped image

# save the image with Image.save(outfile) as .png
im.save(my_path + "images/dog_modified.png")
