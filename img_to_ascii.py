import numpy as np
from PIL import Image

IMAGES_FOLDER = 'Images/'
IMAGE_FILE = 'sunflower.png'
ASCII_FILE = 'ascii.txt'
ASCII_IMAGE_SIZE = (3 * 64, 64)

#from most black to most white
inversed_spectrum = '$@B%8&WM#\*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
#from most white to most black
full_spectrum = inversed_spectrum[::-1]
small_spectrum = " .:-=+*#%@" #10 levels 

ascii_spectrum = small_spectrum 
bins = np.linspace(0, 256, len(ascii_spectrum))

image = Image.open(IMAGES_FOLDER + IMAGE_FILE)
#greyscale image
grim = image.resize(ASCII_IMAGE_SIZE).convert('L') #(8-bit pixels, black and white)
ascii_data = np.array([ascii_spectrum[x] for x in np.digitize(grim.getdata(), bins)]).reshape(grim.size[::-1])

with open(ASCII_FILE, 'w+') as f:
    f.write('\n'.join([''.join(row) for row in ascii_data]))