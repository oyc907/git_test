from PIL import Image, ImageDraw, ImageFont
import time
import random
import cv2 as cv
import numpy as np
from colorsys import hsv_to_rgb
from Enemy import Enemy
from Bullet import Bullet
from Character import Character
from Joystick import Joystick

joystick = Joystick()
#filename="Enemy_3.png"
filename="astronaut_cut(70)_normal_after.png"
subject_filename="subject_1(25).png"


def main():
    joystick = Joystick()
    #my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_image = Image.new("RGBA", (joystick.width, joystick.height))

    #back_im=my_image.copy()    #굳이 copy() 없어도 동작함

    my_draw = ImageDraw.Draw(my_image)
    #my_draw = ImageDraw.Draw(back_im)

    
    Char_1=Image.open(filename) #움직일 character의 그림

    Student= Character(joystick.width, joystick.height)
    
    enemy_1 = Enemy((50, 50))
    enemy_2 = Enemy((200, 200))
    enemy_3 = Enemy((150, 50))

    enemys_list = [enemy_1, enemy_2, enemy_3]
    while True:
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
        
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True

        Student.move(command)

        #back_im.paste(Char_1,tuple((Student.center)))
        my_image.paste(Char_1,tuple((Student.center)))

        #joystick.disp.image(back_im)
        joystick.disp.image(my_image)
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (0xff, 0xff, 0xff, 100))   #흰색
        #my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (0, 0, 0, 100))   #기본 배경은 검정
        
        


        
        

            # for enemy in enemys_list:
            # if enemy.state != 'die':
            #     my_draw.ellipse(tuple(enemy.position), outline = enemy.outline, fill = (255, 0, 0))
if __name__ == '__main__':
    main()