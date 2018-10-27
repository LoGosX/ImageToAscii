import numpy as np
from PIL import Image

ascii_spectrum = ' .:-=+*%@'
bins = np.linspace(0, 256, len(ascii_spectrum))
grim = Image.open('../python-logo.png').resize((64,32)).convert('L')
ascii_data = np.array([ascii_spectrum[x-1] for x in np.digitize(grim.getdata(), bins)]).reshape(grim.size[::-1]) #if because of row - column form of numpy ndarray
with open('result.txt', 'w+') as f:
    f.write('\n'.join([''.join(row) for row in ascii_data]))