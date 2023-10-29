from PIL import Image, ImageDraw
from get_coordinates import *

exec(open("generator.py").read())

image = Image.open("Images/output.jpg")
draw = ImageDraw.Draw(image)

print("\nWhere are you closest to?\n")
first_coord = get_coordinates()

print("\nWhere do you wish to go?\n")
second_coord = get_coordinates()

draw.rectangle((first_coord[0]-5, first_coord[1]-5, first_coord[0]+5, first_coord[1]+5), fill="blue")
draw.rectangle((second_coord[0]-5, second_coord[1]-5, second_coord[0]+5, second_coord[1]+5), fill="red")
draw.line((first_coord[0],first_coord[1],second_coord[0],second_coord[1]), fill="blue")

image.save("Images/output.jpg")
