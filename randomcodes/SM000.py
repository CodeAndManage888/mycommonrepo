# Code from social media - YouTube
# Image Editor | Status: Working
# How to Use: 
# a. Ensure the source and destination path are correct and files are 
#    available. Execute the code using IDE or terminal.
# ---------------------------------------------------------------------

from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"
pathOut = "./editedImgs"

for filename in os.listdir(path):
	img = Image.open(f"{path}/{filename}")
	
	# sharpening, BW
	# edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
	edit = img.filter(ImageFilter.SHARPEN).convert('L')
	
	# contrast
	factor = 1.5
	enhancer = ImageEnhance.Contrast(edit)
	edit = enhancer.enhance(factor)
	
	# saving edited photo
	clean_name = os.path.splitext(filename)[0]
	# edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
	# -- the above line of code is the original code from github
	#    however this produces error. after removing the "." before 
	#    the destination path it worked.
	edit.save(f'{pathOut}/{clean_name}_fordel.jpg')
# ---------------------------------------------------------------------
# Other Use Cases:
# ---------------------------------------------------------------------
# a. 
