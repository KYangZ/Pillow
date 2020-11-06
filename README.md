# Walkthrough of the Pillow Library

## Example 1: Enhancing an Image
1. Suppose we want to enhance the image "smilelaugh.jpg" in the images/ folder. 

![smilelaugh.jpg](/images/smilelaugh.jpg)




## Example 2: Basic Manipulations of the Image

1. Import the relevant library and modules:

  import os, sys

  from PIL import Image, ImageEnhance
1b. (Optional) Set the path for the working directory

  my_path = os.path.dirname(__file__)
  
2. Open the image

  im = Image.open(my_path + "images/left_facing_dog.png")
  im.show() # show the initial image
  
  ![left_facing_dog.png](/images/left_facing_dog.png)
  
3. Begin some basic manipulations. Start with rotating it.

  im = im.rotate(45)
  im.show() # show the rotated image
  ![dog_rotated.PNG](/images/dog_rotated.PNG)

im = im.transpose(Image.FLIP_TOP_BOTTOM)
im.show() # show the flipped image

# save the image with Image.save(outfile) as .png
im.save(my_path + "images/dog_modified.png")
