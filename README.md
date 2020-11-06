# Walkthrough of the Pillow Library

## Example 1: Enhancing an Image
1. Suppose we want to enhance the image "smilelaugh.jpg" in the images/ folder. 

![smilelaugh.jpg](/images/smilelaugh.jpg)




## Example 2: Basic Manipulations of the Image
1. First, import the relevant library and modules:

import os, sys

from PIL import Image, ImageEnhance

my_path = os.path.dirname(__file__)
