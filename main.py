from PIL import Image, ImageDraw, ImageFont, ImageOps
import time
import random
import cv2 as cv
import numpy as np

import threading
import random

from colorsys import hsv_to_rgb
from Enemy import Enemy
from Bullet import Bullet
from Character import Character
from Joystick import Joystick

#count=0

#filename_right_basic="Student_40_right.png"
filename_right_1="Student_40_right_1.png"
filename_right_4="Student_40_right_4.png"


filename_left_1="Student_40_left_1.png"
filename_left_2="Student_40_left_2.png"


filename_up="Student_up_40.png"
filename_down="Student_down_40.png"

subject_filename="Subject_50.png"
backg_filename="Earth.png"

explode_1_flename="prac_Explode_1(50).png"
explode_2_flename="prac_Explode_2(50).png"
explode_3_flename="prac_Explode_3(50).png"
explode_4_flename="prac_Explode_4(50).png"



def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    #my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
    

    # joystick.disp.image(my_image)
    # # 잔상이 남지 않는 코드 & 대각선 이동 가능
    my_circle = Character(joystick.width, joystick.height)
    # my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
    
     
    Char_r_1=Image.open(filename_right_1) #움직일 character의 그림(오른쪽)
    Char_r_4=Image.open(filename_right_4)



    Char_l_1=Image.open(filename_left_1) #움직일 character의 그림(왼쪽)
    Char_l_2=Image.open(filename_left_2) #움직일 character의 그림(왼쪽)


    Char_3=Image.open(filename_up) #움직일 character의 그림(위쪽)
    Char_4=Image.open(filename_down) #움직일 character의 그림(아래쪽)
    
    #Char=ImageOps.expand(Char_1, border=1, fill='red')   #image의 경계선(border)를 그림
    Char=ImageOps.expand(Char_r_1, border=1, fill='red')   #image의 경계선(border)를 그림

    

    Subject_img=Image.open(subject_filename) #Enemy(과목)의 그림
    Subject_img_border = ImageOps.expand(Subject_img, border=1, fill='blue')

    back_g=Image.open(backg_filename)   #배경 이미지

    explode_1=Image.open(explode_1_flename) #터지는 이미지
    explode_2=Image.open(explode_2_flename)
    explode_3=Image.open(explode_3_flename)
    explode_4=Image.open(explode_4_flename)
    
    explode_img_list=[explode_1,explode_2,explode_3,explode_4]


    Student= Character(joystick.width, joystick.height)
    
    enemy_1 = Enemy((50, 50),0,0)
    enemy_2 = Enemy((200, 200),0,0)
    enemy_3 = Enemy((150, 50),0,0)

    enemys_list = [enemy_1, enemy_2, enemy_3]


    bullets = []

    flag=0    #움직일 때, 걷는 것처럼 구현하기 위한 flag
    global sign_regen   # 전역 변수 sign_regen을 사용
    while True:
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
        
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True
            #Char=ImageOps.expand(Char_3, border=1, fill='red')   #image의 경계선(border)를 그림 

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True
            #Char=ImageOps.expand(Char_4, border=1, fill='red')   #image의 경계선(border)를 그림

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True
            flag=~flag
            if flag:
                Char=ImageOps.expand(Char_l_2, border=1, fill='red')   #image의 경계선(border)를 그림 
            else:
                Char=ImageOps.expand(Char_l_1, border=1, fill='red')   #image의 경계선(border)를 그림

        # if not joystick.button_U.value and not joystick.button_L.value:  # 위와 왼쪽 동시에 pressed
        #     command['up_pressed'] = True
        #     command['move'] = True
        #     Char=ImageOps.expand(Char_3, border=1, fill='red')   #image의 경계선(border)를 그림 

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True
            flag=~flag
            if flag:
                Char=ImageOps.expand(Char_r_1, border=1, fill='red')   #image의 경계선(border)를 그림
            # for img in Char_r_list:
            #     Char=ImageOps.expand(img, border=1, fill='red')   #image의 경계선(border)를 그림
            else:    
                Char=ImageOps.expand(Char_r_4, border=1, fill='red')   #image의 경계선(border)를 그림
            

        if not joystick.button_A.value: # A pressed
            #bullet = Bullet(my_circle.center, command)
            bullet = Bullet(Student.center, command)
            bullets.append(bullet)
            

        my_circle.move(command)
        Student.move(command)
        for bullet in bullets:
            bullet.collision_check(enemys_list)
            bullet.hit_wall_check(joystick.width, joystick.height)    #벽에 닿으면 hit 판정
            bullet.move()

            
            
        # my_circle.collision_check(enemys_list)    
        # #그리는 순서가 중요합니다. 배경을 먼저 깔고 위에 그림을 그리고 싶었는데 그림을 그려놓고 배경으로 덮는 결과로 될 수 있습니다.
        # my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
        #my_draw.ellipse(tuple(my_circle.position), outline = my_circle.outline, fill = (0, 0, 0))
        # #print("position: ",my_circle.position[0],my_circle.position[1],my_circle.position[2],my_circle.position[3])
        # #print("center: ",my_circle.center[0],my_circle.center[1])


        Student.collision_check(enemys_list)
        # _, _, _, mask = Char_1.split()
        # my_image.paste(Char_1,tuple((Student.center)),mask)     #투명부분은 안 보이도록 설정

        _, _, _, mask = Char.split()
        # my_image.paste(Char,tuple((Student.center)-20),mask)     #투명부분은 안 보이도록 설정
        my_image.paste(Char,tuple((Student.center)-Student.width_ego),mask)     #투명부분은 안 보이도록 설정


        

        #_, _, _, mask = Subject_img.split()
        _, _, _, mask = Subject_img_border.split()

        # for enemy in enemys_list:
        #     my_image.paste(Subject_img,tuple((enemy.center)),mask)     #투명부분은 안 보이도록 설정
        
        joystick.disp.image(my_image)
        my_image.paste(back_g,(0,0))

        for enemy in enemys_list:
            if enemy.state != 'die':
                #my_draw.ellipse(tuple(enemy.position), outline = enemy.outline, fill = (255, 0, 0))
                
                #my_image.paste(Subject_img,tuple((enemy.center)),mask)     #투명부분은 안 보이도록 설정
                # my_image.paste(Subject_img_border,tuple((enemy.center)-25),mask)     #투명부분은 안 보이도록 설정
                my_image.paste(Subject_img_border,tuple((enemy.center)-enemy.width_ego),mask)     #투명부분은 안 보이도록 설정
            elif enemy.die_flag==0 and enemy.state == 'die':
                print("enemy.state: ",enemy.state,"enemy: ",enemy)
                timer(0,enemy)     # timer ISR을 실행시켜 일정 시간 이후 sign_regen값을 주도록 하기 위함
                enemy.die_flag=1  # enemy.state == 'die' 의 판단을 한번만 하도록 하기위함(timer ISR 여러번 실행 방지)
                
                #for i in range (1,4):
                for explode_img in explode_img_list:
                    _, _, _, mask_1 = explode_img.split()   #투명부분은 안 보이도록 설정
                    #mask를 mask_1으로 선언하여, 앞선 mask와 겹치지 않도록 함
                    my_image.paste(explode_img,tuple((enemy.center)-enemy.width_ego),mask_1) 
                # enemy.regen((-30,-30),0,0) 
                # 안보이는 곳으로 옮김으로써 터진 위치에서 계속 hit 판정을 안나도록 함
                # (이래야 총알이 방금 맞혔던 자리 지나가도 보임)
                
                
                    

                
        
       

        for enemy in enemys_list:
            if enemy.sign_regen==1:
                print("hi",enemy)
                enemy.regen((enemy.center),0,0) 
                # enemy.regen((random.randint(0,240),random.randint(0,240)),0,0)

        for bullet in bullets:
            if bullet.state != 'hit':
                my_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (255, 255, 0))
            else:
                bullets.remove(bullet)  #총알이 계속 list에 존재하는 것 방지

    
        #print(bullets)

        #좌표는 동그라미의 왼쪽 위, 오른쪽 아래 점 (x1, y1, x2, y2)
        #joystick.disp.image(my_image)
        

#def timer():
def timer(count,enemy):
    #global count   #global로 하면 동시에 여러개 timer 동작 못함
    count+=1
    print(count)
    t=threading.Timer(1,timer,args=(count,enemy,))    #"enemy"말고 마지막에 "enemy,"로 꼭 ,붙이기!!!!
   
    t.start()
    if count >=3:   #timer 시간
        count=0     #timer 초기화
        enemy.sign_regen=1    # regen함수를 실행 시키기 위함
        print("Jam",enemy)
        print("타이머를 멈춥니다")
        t.cancel()      #timer 종료

if __name__ == '__main__':
    main()