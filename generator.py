import random, model, math
import numpy as np
from PIL import Image, ImageDraw

labels = np.load("archive/labels.npy").flatten()
ds = [x for x in model.make_ds("archive/frames/",labels,False,1).as_numpy_iterator()]
ds_range = (max(labels/(480*640))-min(labels/(480*640))) 
print(ds_range)


# Draws shape based off image given, the x and y parameters, color, and output path
def draw_rect(x1, y1, x2, y2, color):
    image = Image.open("Images/output.jpg")
    draw = ImageDraw.Draw(image, "RGBA")
    draw.rectangle(((x1, y1), (x2, y2)), fill=color)
    draw.rectangle(((x1, y1), (x2, y2)), outline=(0, 0, 0, 0), width=0)
    image.save("Images/output.jpg")


def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    image = Image.open("Images/output.jpg")
    draw = ImageDraw.Draw(image, "RGBA")
    draw.polygon(((x1, y1), (x2, y2), (x3, y3)), fill=color)
    draw.polygon(((x1, y1), (x2, y2), (x3, y3)), outline=(0, 0, 0, 0), width=0)
    image.save("Images/output.jpg")
    
def draw_arc(x1, y1, x2, y2, color):
    image = Image.open("Images/output.jpg")
    draw = ImageDraw.Draw(image, "RGBA")
    draw.arc(((x1, y1), (x2, y2)), fill=color, width = 10, start=180, end=360)
    image.save("Images/output.jpg")

calc_pct = lambda pred: (pred/(480*640))/ds_range

def get_color():
    pred = model.predict(ds[random.randint(0,1999)][0])
    color = (math.ceil(255*calc_pct(pred)),0, 0, 127)
    return color


def run():

    # Opens initial image file and saves a copy and names it output.jpg
    initial_easton_image = Image.open("Images/EastonMall.jpg")
    output_image = initial_easton_image.copy()
    output_image.save("Images/output.jpg")

    draw_rect( 288, 526, 395, 537, get_color())

    # Creates map with first space for New Bond Street Right
    draw_rect(504, 526, 603, 537, get_color())

    # Creates map with space for the strand
    # west
    draw_rect(396, 525, 407, 753, get_color())
    # east
    draw_rect(493, 525, 504, 753, get_color())
    # north
    draw_rect(445, 314, 456, 486, get_color())

    # central park north circle
    draw_arc(398,487,502,562,get_color())
    # Creates central park south
    draw_rect(408, 564, 492, 575,get_color())

    # Creates map with space for regent street
    draw_rect(276, 314, 287, 753, get_color())

    # Creates map with space for worth avenue
    draw_rect(209, 303, 615, 313, get_color())

    # Creates map for indoor top left
    draw_rect(431, 771, 447, 824, get_color())
    # Creates map for indoor top middle left
    draw_rect(425, 825, 447, 890, get_color())
    draw_rect(410, 881, 425, 890, get_color())
    draw_rect(410, 891, 434, 900, get_color())

    # Creates map for indoor top right
    draw_rect(448, 771, 464, 824, get_color())
    # Creates map for indoor middle right
    draw_rect(448, 825, 464, 890, get_color())
    draw_triangle(465, 824, 486, 890, 465, 890, get_color())

    # Creates map for middle left
    draw_rect(315, 908, 409, 925, get_color())
    draw_rect(409, 900, 434, 925,get_color())
    draw_triangle(337, 909, 392, 901, 392, 908, get_color())
    draw_rect(393, 901, 408, 908, get_color())
    draw_triangle(405, 925, 413, 925, 413, 932, get_color())
    draw_rect(413, 925, 433, 932, get_color())
    draw_rect(434, 913, 452, 932, get_color())

    # Creates map for middle right
    draw_rect(553, 911, 586, 932, get_color())
    draw_rect(510, 905, 552, 927, get_color())
    draw_rect(487, 905, 509, 926, get_color())
    draw_rect(487, 900, 509, 904, get_color())
    draw_rect(485, 892, 489, 924, get_color())
    draw_triangle(485, 926, 490, 928, 485, 931, get_color())
    draw_rect(453, 913, 484, 932, get_color())
    draw_rect(468, 891, 484, 912, get_color())

    # Creates map for bottom left
    draw_rect(414, 933, 450, 963, get_color())
    draw_rect(414, 964, 426, 1008, get_color())

    # Creates map for bottom right
    draw_rect(451, 933, 484, 963, get_color())
    draw_rect(475, 964, 484, 1008, get_color())

    # Gremacy Street West
    draw_rect(229, 754, 407, 765, get_color())

    # Gremacy Street East
    draw_rect(493, 754, 752, 765, get_color())

    # Easton Station
    draw_rect(209, 1039, 677, 1050, get_color())

    # Easton Loop West
    draw_rect(197, 955, 208, 1296, get_color())
    draw_rect(197, 303, 208, 753, get_color())

    # Fenlon Street
    draw_rect(604, 314, 615, 753, get_color())

    # Easton Square Place West
    draw_rect(402, 1051, 413, 1164, get_color())

    # Easton Square Place East
    draw_rect(496, 1051, 507, 1164, get_color())

    # Easton Square Place South
    draw_rect(449, 1177, 460, 1311, get_color())

    # Townsfair way West
    draw_rect(132, 1165, 196, 1176, get_color())

    # Townsfair way
    draw_rect(209, 1165, 677, 1176, get_color())

    # Chagrin Drive South
    draw_rect(678, 971, 689, 1303, get_color())

    # Chagrin Drive North
    draw_rect(678, 766, 689, 868, get_color())


run()
