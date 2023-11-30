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


import time




joystick = Joystick()
#filename="Enemy_3.png"
filename="astronaut_cut(70)_normal_after.png"
subject_filename="subject_1(25).png"
backg_filename="Earth.png"

def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))

    #back_im=my_image.copy()    #굳이 copy() 없어도 동작함

    my_draw = ImageDraw.Draw(my_image)

    
    Char_1=Image.open(filename) #움직일 character의 그림
    back_g=Image.open(backg_filename)   #배경 이미지

    Student= Character(joystick.width, joystick.height)
    

    enemy_1 = Enemy((50, 50))
    enemy_2 = Enemy((200, 200))
    enemy_3 = Enemy((150, 50))

    enemys_list = [enemy_1, enemy_2, enemy_3]

    bullets = []
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
        Student.collision_check(enemys_list)

        _, _, _, mask = Char_1.split()
        my_image.paste(Char_1,tuple((Student.center)),mask)     #투명부분은 안 보이도록 설정

        #print("Jam")
        print("position: ",Student.position[0],Student.position[1],Student.position[2],Student.position[3])
        print("center: ",Student.center[0],Student.center[1])
        joystick.disp.image(my_image)
        my_image.paste(back_g,(0,0))
        #my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (0xff, 0, 0, 100))   #흰색
        #my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (0, 0, 0, 100))   #기본 배경은 검정
        
        #print("Enemy die\n")
        for enemy in enemys_list:
            if enemy.state != 'die':
                
                my_draw.ellipse(tuple(enemy.position), outline = enemy.outline, fill = (255, 0, 0))
        
if __name__ == '__main__':
    main()