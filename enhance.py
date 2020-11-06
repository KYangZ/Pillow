import os, sys
from PIL import Image, ImageEnhance

# set the path so we can reference things in the current directory
my_path = os.path.dirname(__file__)

# open the image with Image.open()
im = Image.open(my_path + "images/smilelaugh.jpg")
print(im.format, im.size, im.mode)
im.show()

# sharpen the image
enh = ImageEnhance.Sharpness(im)
im = enh.enhance(10)

# increase the contrast of the overall image
enh = ImageEnhance.Contrast(im)
im = enh.enhance(10)
im.show()

# zoom in


# save the image with Image.save(outfile)
im.save(my_path + "images/smilelaugh_enhanced.jpg")
