from PIL import Image
from PIL import ImageDraw
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

ranks = [1,2,3,4,5,6,7,8]
files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
board_width = 360
board_height = 360
top_padding = 10
right_padding = 10
left_label = 15
bottom_label = 15
gride_side = 45

def create_board():
    img_width = board_width + right_padding + left_label
    img_height = board_height + top_padding + bottom_label

    full_array = np.zeros([img_height, img_width, 3], dtype=np.uint8) + 155

    top = top_padding
    left = left_label

    board_array = full_array[top:board_height+top, left:board_width+left, :]

    for x in range(board_height):
        for y in range(board_width):
            if (x % 90) // 45 == (y % 90) // 45:
                board_array[y, x, :] = [255, 255, 255]
            else:
                board_array[y, x, :] = [100, 100, 100]


    img = Image.fromarray(full_array)

    I1 = ImageDraw.Draw(img)
    font_size = 10

    rank_label_left_padding = 5
    for i,rank in enumerate(ranks[::-1]):
        x = rank_label_left_padding
        y = int((gride_side * i) + (gride_side / 2) - (font_size / 2) + top_padding)
        I1.text((x, y), str(rank), fill=(0, 0, 0))
    file_label_top_padding = 2
    for i,rank in enumerate(files):
        x = int((gride_side * i) + (gride_side / 2) - (font_size / 2) + left_label)
        y = board_height + top_padding + file_label_top_padding
        I1.text((x, y), str(rank), fill=(0, 0, 0))
    # myFont = ImageFont.truetype('FreeMono.ttf', 65)
    # I1.text((10, 10), "Nice Car", font=myFont, fill =(255, 0, 0))
    
    return img

# create_board().show() 
