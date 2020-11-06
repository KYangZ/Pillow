# Walkthrough of the Pillow Library
## Kory Yang and Isaac Lee

## Example 1: Enhancing an Image
### 1. Suppose we want to enhance the image "smilelaugh.jpg" in the images/ folder. 
<img src="/images/smilelaugh.jpg" width="250">

### 2. Let's modify this image using the ImageEnhance module in Pillow (the code is in enhance.py). First, install Pillow:
`python3 -m pip install pillow`

### 3. Now import the proper libraries:
```
import os, sys
from PIL import Image, ImageEnhance
```
### 4. Let's get the path to the current directory so we can reference files in the current directory, and then open the image, printing some information alongside it:
```
# set the path so we can reference things in the current directory
my_path = os.path.dirname(__file__)

# open the image with Image.open()
im = Image.open(my_path + "images/smilelaugh.jpg")
print(im.format, im.size, im.mode)
```

### 5. You can also call `im.show()` to see the image currently.
### 6. To sharpen an image, we can call the ImageEnhance.Sharpness module, which will sharpen an image by a factor we pass in (we can even pass in a value less than 1). 
```
enh = ImageEnhance.Sharpness(im)
im = enh.enhance(10)
```
### 7. We can increase the contrast of the image in the same fashion. Don't forget to set `im` equal to the result of the enhancement, or else the image will be unchanged.
```
enh = ImageEnhance.Contrast(im)
im = enh.enhance(10)
```
### 8. Call `im.show()` to see what the result looks like:
<img src="/images/smilelaugh_enhanced.jpg" width="250">

### 9. Great! Now we can save the image, using `Image.save(outfile)`
```
im.save(my_path + "images/smilelaugh_enhanced.jpg")
```

## Example 2: Basic Manipulations of the Image

### 1. Import the relevant library and modules:
```
from PIL import Image, ImageEnhance
```
### 1b. (Optional) Set the path for the working directory
```
import os, sys

my_path = os.path.dirname(__file__)
```
### 2. Open the image
```
im = Image.open(my_path + "images/left_facing_dog.png")
im.show()
```  
![left_facing_dog.png](/images/left_facing_dog.png)
  
### 3. Begin some basic manipulations. Start with rotating it.
```
im = im.rotate(45)
im.show()
```
![dog_rotated.PNG](/images/dog_rotated.PNG)

### 4. Try flipping the image. In this case, flip image with respect to the horizontal axis.
```
im = im.transpose(Image.FLIP_TOP_BOTTOM)
im.show()
```
![dog_modified.png](/images/dog_modified.png)

### 5. Save the image as "dog_modified.png"
```
im.save(my_path + "images/dog_modified.png")
```
