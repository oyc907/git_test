from PIL import Image, ImageDraw, ImageFont
import cv2 as cv
from Joystick import Joystick

joystick = Joystick()
filename="Enemy_3.png"

my_image = Image.new("RGB", (joystick.width, joystick.height))  #LCD 배경을 도화지로 설정
my_draw = ImageDraw.Draw(my_image)


#my_draw.open("Enemy_3.png")

my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
#my_draw.ellipse((100, 50, 140, 90), outline = "#FFFFFF", fill = (0, 0, 0))
my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))

#my_draw.open("Enemy_3.png")((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
#image = Image.open("Enemy_3.png")


joystick.disp.image(my_image)

