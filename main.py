from PIL import Image, ImageDraw, ImageFont
import time
import random
import cv2 as cv
import numpy as np

import threading

from colorsys import hsv_to_rgb
from Enemy import Enemy
from Bullet import Bullet
from Character import Character
from Joystick import Joystick

count=0
sign_regen=0
def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
    joystick.disp.image(my_image)
    # 잔상이 남지 않는 코드 & 대각선 이동 가능
    my_circle = Character(joystick.width, joystick.height)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
    enemy_1 = Enemy((50, 50))
    enemy_2 = Enemy((200, 200))
    enemy_3 = Enemy((150, 50))

    enemys_list = [enemy_1, enemy_2, enemy_3]

    bullets = []

    die_flag=0
    global sign_regen   # 전역 변수 sign_regen을 
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

        if not joystick.button_A.value: # A pressed
            bullet = Bullet(my_circle.center, command)
            bullets.append(bullet)

        my_circle.move(command)
        for bullet in bullets:
            bullet.collision_check(enemys_list)
            bullet.move()
            
        my_circle.collision_check(enemys_list)
        #그리는 순서가 중요합니다. 배경을 먼저 깔고 위에 그림을 그리고 싶었는데 그림을 그려놓고 배경으로 덮는 결과로 될 수 있습니다.
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
        my_draw.ellipse(tuple(my_circle.position), outline = my_circle.outline, fill = (0, 0, 0))
        #print("position: ",my_circle.position[0],my_circle.position[1],my_circle.position[2],my_circle.position[3])
        #print("center: ",my_circle.center[0],my_circle.center[1])
        
        for enemy in enemys_list:
            if enemy.state != 'die':
                my_draw.ellipse(tuple(enemy.position), outline = enemy.outline, fill = (255, 0, 0))
                print("jam enemy_3.state: ",enemy_3.state)
                
            
            

        for bullet in bullets:
            if bullet.state != 'hit':
                my_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (0, 0, 255))

    
        if die_flag==0 and enemy_3.state == 'die':
            print("enemy_3.state: ",enemy_3.state)
            timer()     # timer ISR을 실행시켜 일정 시간 이후 sign_regen값을 주도록하기 위함
            die_flag=1  # enemy_3.state == 'die' 의 판단을 한번만 하도록 하기위함(timer ISR 여러번 실행 방지)
        if sign_regen==1:
            sign_regen=0
            die_flag=0
            #enemy_3 = Enemy((50, 150)) # 해당 위치에 나오지 않는다.
            enemy_3.regen((50, 150))  
            

        #좌표는 동그라미의 왼쪽 위, 오른쪽 아래 점 (x1, y1, x2, y2)
        joystick.disp.image(my_image)
        

def timer():
    global count
    global sign_regen
    count+=1
    print(count)
    t=threading.Timer(1,timer)
    t.start()
    if count ==5:
        count=0
        sign_regen=1    # regen함수를 실행 시키기 위함
        print("타이머를 멈춥니다")
        t.cancel()
if __name__ == '__main__':
    main()