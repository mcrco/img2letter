import cv2
import numpy as np
from math import ceil

file_name = input('Enter image file name: ')
dpi = int(input('Enter image dpi: '))

img = cv2.imread(file_name)
print('Image shape:', img.shape)

img_w = img.shape[1]
img_h = img.shape[0]
width = int(dpi * 11)
height = int(dpi * 8.5)

def name(r, c):
    return '_'.join([file_name[:-4], str(r), str(c)]) + file_name[-4:]

num_rows = ceil(img_h / height)
num_cols = ceil(img_w / width)

print('Grid shape:', num_rows, 'by', num_cols)

for r in range(num_rows):
    for c in range(num_cols):
        c_start = c * width
        c_end = min(img_w, c_start + width)
        r_start = r * height
        r_end = min(img_h, r_start + height)

        div = img[r_start:r_end, c_start:c_end]
        cv2.imwrite(name(r, c), div)
