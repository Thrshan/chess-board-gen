from PIL import Image
import numpy as np
'''
width = 100
height = 200

array = np.zeros([height, width, 3], dtype=np.uint8)

array[:,:] = [255, 128, 0]

array = np.zeros([100, 200, 3], dtype=np.uint8)
array[:,:100] = [255, 128, 0] #Orange left side
array[:,100:] = [0, 0, 255]   #Blue right side

img = Image.fromarray(array)
img.show()



array = np.zeros([100, 200, 4], dtype=np.uint8)
array[:,:100] = [255, 128, 0, 255] #Orange left side
array[:,100:] = [0, 0, 255, 255]   #Blue right side

# Set transparency based on x position
array[:, :, 3] = np.linspace(0, 255, 200)

img = Image.fromarray(array)
img.show()


array = np.zeros([100, 200], dtype=np.uint8)

# Set grey value to black or white depending on x position
for x in range(200):
    for y in range(100):
        if (x % 16) // 8 == (y % 16) // 8:
            array[y, x] = 0
        else:
            array[y, x] = 255

img = Image.fromarray(array)
img.show()
'''

width = 360
height = 360

array = np.zeros([height, width, 3], dtype=np.uint8)

for x in range(height):
    for y in range(width):
        if (x % 90) // 45 == (y % 90) // 45:
            array[y, x, :] = [100, 100, 100]
        else:
            array[y, x, :] = [255, 255, 255]

img = Image.fromarray(array)
img.show()