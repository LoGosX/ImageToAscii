import numpy as np
from PIL import Image
import sys

INVERSED_SPECTRUM = '$@B%8&WM#\*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. ' #from most black to most white
FULL_SPECTRUM = inversed_spectrum[::-1] #same as above but from most white to most black
SMALL_SPECTRUM = " .:-=+*#%@" #10 levels from most white to most black


def image_to_ascii(image_file_path, width, height, ascii_spectrum):
    #np.linspace(0,16,5) -> [0, 4, 8, 12, 16] 5 elements from 0 to 16 arranged linearly. You got the idea
    bins = np.linspace(0, 256, len(ascii_spectrum)) 
    #greyscale image (8-bit pixels, only black and white)
    if (width,height) != (None, None):
        grim = Image.open(image_file_path).resize((width,height)).convert('L')
    else:
        grim = Image.open(image_file_path).convert('L')
    ascii_data = np.array([ascii_spectrum[x] for x in np.digitize(grim.getdata(), bins)]).reshape(grim.size[::-1]) #if because of row - column form of numpy ndarray
    return '\n'.join([''.join(row) for row in ascii_data])


def main():
    try:
        _, image_file, width, height, *_ = *sys.argv, None, None
    except ValueError:
        print('Not enough arguments. Did you forget name of the file?\nTry: python image_to_ascii.py <path_to_image>')
        raise SystemExit
    output_file = image_file.split('.')[0] + '.txt'
    result = image_to_ascii(image_file, width, height, SMALL_SPECTRUM) #You can choose one of spectrum above for different results. 'small_spectrum' looks the best in my opinion
    with open(output_file, 'w+') as f:
        f.write(result)
        print('Saved in', image_file)

if __name__ == '__main__':
    main()