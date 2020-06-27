import sys
import os
from PIL import Image

#grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2] 

print(image_folder, output_folder)
#check if new/ existsf not create one

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}') #loop through the Pokedex folder and open each image
    clean_name = os.path.splitext(filename)[0] #split the filename into a tuple and only grab the name and not the .jpg
    img.save(f'{output_folder}{clean_name}.png', 'png') # convert the images from jpg to png
#loop through Pokedex,
# convert images to png