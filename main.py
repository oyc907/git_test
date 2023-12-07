from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageChops
import time
import random
import cv2 as cv
import numpy as np

import threading
import random
import time

from colorsys import hsv_to_rgb
from Enemy import Enemy
from Bullet import Bullet
from Character import Character
from Joystick import Joystick

#count=0

filename_right_basic="Student_40_right.png"
filename_right_1="Student_40_right_1.png"
filename_right_2="Student_40_right_2.png"
filename_right_3="Student_40_right_3.png"
filename_right_4="Student_40_right_4.png"




filename_left_1="Student_40_left_1.png"
filename_left_2="Student_40_left_2.png"


filename_up="Student_up_40.png"
filename_down="Student_down_40.png"

subject_filename="Subject_50.png"
backg_filename="Earth.png"
game_over_filename="GAME_OVER.png"
game_start_filename="GAME_START.png"
game_clear_filename="GAME_CLEAR.png"

# explode_1_flename="prac_Explode_1(50).png"
# explode_2_flename="prac_Explode_2(50).png"
# explode_3_flename="prac_Explode_3(50).png"
# explode_4_flename="prac_Explode_4(50).png"

explode_1_flename="Explode_1(50).png"
explode_2_flename="Explode_2(50).png"
explode_3_flename="Explode_3(50).png"
explode_4_flename="Explode_4(50).png"
explode_5_flename="Explode_5(50).png"
explode_6_flename="Explode_6(50).png"
explode_7_flename="Explode_7(50).png"
explode_8_flename="Explode_8(50).png"
explode_9_flename="Explode_9(50).png"

explode_1=Image.open(explode_1_flename) #터지는 이미지
explode_2=Image.open(explode_2_flename)
explode_3=Image.open(explode_3_flename)
explode_4=Image.open(explode_4_flename)
explode_5=Image.open(explode_5_flename) 
explode_6=Image.open(explode_6_flename)
explode_7=Image.open(explode_7_flename)
explode_8=Image.open(explode_8_flename)
explode_9=Image.open(explode_9_flename)
    
explode_img_list=[explode_1,explode_2,explode_3,explode_4,explode_5,explode_6,explode_7,explode_8,explode_9]

joystick = Joystick()
# my_image = Image.new("RGB", (joystick.width, joystick.height))
my_image = Image.new("RGBA", (joystick.width, joystick.height)) #RGB말고, RGBA로 해야 ImageChops 이용가능

back_g=Image.open(backg_filename)   #배경 이미지
back_g_origin=Image.open(backg_filename)

game_over=Image.open(game_over_filename)
game_start=Image.open(game_start_filename)
game_clear=Image.open(game_clear_filename)

Char_r=Image.open(filename_right_basic) #움직일 character의 그림(오른쪽)
Char_r_1=Image.open(filename_right_1) 
Char_r_2=Image.open(filename_right_2)
Char_r_3=Image.open(filename_right_3)
Char_r_4=Image.open(filename_right_4)
Char_r_list=[Char_r_1,Char_r_2,Char_r_3,Char_r_4]
# Char=ImageOps.expand(Char_r, border=1, fill='red')   #image의 경계선(border)를 그림
Char=Image.open(filename_right_basic)

flag_attack=0  #attack동작 구현 위한 전역변수

bbox     = (0,0,joystick.width,joystick.height)
text_pos = (bbox[0],bbox[1])
# font=ImageFont.truetype("Oswald-VariableFont_wght.ttf", 20) 
font=ImageFont.load_default()

image = ImageChops.subtract(my_image,back_g)    #폭발하는 부분만 가져옴
image_f=ImageChops.add(back_g_origin,image)
stage=1
def main():
    # global back_g   #Character 동작 보이기 위해
    
    my_draw = ImageDraw.Draw(my_image)
    
    

    
    my_circle = Character(joystick.width, joystick.height)
    
    
     
    Char_r=Image.open(filename_right_basic) #움직일 character의 그림(오른쪽)
    Char_r_1=Image.open(filename_right_1) 
    Char_r_2=Image.open(filename_right_2)
    Char_r_3=Image.open(filename_right_3)
    Char_r_4=Image.open(filename_right_4)
    Char_r_list=[Char_r_1,Char_r_2,Char_r_3,Char_r_4]


    Char_l_1=Image.open(filename_left_1) #움직일 character의 그림(왼쪽)
    Char_l_2=Image.open(filename_left_2) #움직일 character의 그림(왼쪽)


    # Char_3=Image.open(filename_up) #움직일 character의 그림(위쪽)
    # Char_4=Image.open(filename_down) #움직일 character의 그림(아래쪽)
    
    
    # Char=ImageOps.expand(Char_r, border=1, fill='red')   #image의 경계선(border)를 그림
    Char=Image.open(filename_right_basic)

    

    Subject_img=Image.open(subject_filename) #Enemy(과목)의 그림
    Subject_img_border = ImageOps.expand(Subject_img, border=1, fill='blue')

    # back_g=Image.open(backg_filename)   #배경 이미지

    explode_1=Image.open(explode_1_flename) #터지는 이미지
    explode_2=Image.open(explode_2_flename)
    explode_3=Image.open(explode_3_flename)
    explode_4=Image.open(explode_4_flename)
    
    # explode_img_list=[explode_1,explode_2,explode_3,explode_4]    #여기서 list를 가져옴
    explode_img_list=[explode_1,explode_2,explode_3,explode_4,explode_5,explode_6,explode_7,explode_8,explode_9]



    Student= Character(joystick.width, joystick.height)
    
    enemy_1 = Enemy((5, 60),0,0)
    enemy_2 = Enemy((5, 90),0,0)
    enemy_3 = Enemy((5, 120),0,0)
    enemy_4 = Enemy((235, 60),0,0)
    enemy_5 = Enemy((235, 90),0,0)
    enemy_6 = Enemy((235, 120),0,0)

    enemys_list = [enemy_1, enemy_2, enemy_3,enemy_4, enemy_5, enemy_6]


    bullets = []

    flag=0    #움직일 때, 걷는 것처럼 구현하기 위한 flag
    

    flag_lr=0     #총알 발사 시, 왼쪽 OR 오른쪽 발사
    stage=1
    # my_draw.text(text_pos,'Hello',(255,255,255),font=font)
    while joystick.button_B.value:
        joystick.disp.image(game_start)  
    while True:
        

        # joystick = Joystick()
        # # my_image = Image.new("RGB", (joystick.width, joystick.height))
        joystick.disp.image(my_image)
        my_image.paste(back_g,(0,0))    #터지는 것 구현 시, back_g를 이용
        # back_g=image_f
        # text='life: '+Student
        text=['life: ',str(Student.life),'score: ',str(Student.score),'stage: ']
        # my_draw.text(text_pos,text[0]+text[1],(255,255,255),font=font)
        # my_draw.text((0,10),text[2]+text[3],(255,255,255),font=font)
        # my_draw.text((180,0),text[4]+str(stage),(255,255,255),font=font)

        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False, 'A_pressed': False}
        
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
            flag_lr=1
            flag=~flag
            if flag:
                # Char=ImageOps.expand(Char_l_2, border=1, fill='red')   #image의 경계선(border)를 그림
                Char=Image.open(filename_left_2) 
            else:
                # Char=ImageOps.expand(Char_l_1, border=1, fill='red')   #image의 경계선(border)를 그림
                Char=Image.open(filename_left_1) 

        # if not joystick.button_U.value and not joystick.button_L.value:  # 위와 왼쪽 동시에 pressed
        #     command['up_pressed'] = True
        #     command['move'] = True
        #     Char=ImageOps.expand(Char_3, border=1, fill='red')   #image의 경계선(border)를 그림 

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True
            flag_lr=0
            flag=~flag
            if flag:
                # Char=ImageOps.expand(Char_r_1, border=1, fill='red')   #image의 경계선(border)를 그림
                Char=Image.open(filename_right_1) 
            else:    
                # Char=ImageOps.expand(Char_r_4, border=1, fill='red')   #image의 경계선(border)를 그림
                Char=Image.open(filename_right_4)
        
            

        if not joystick.button_A.value: # A pressed
            # bullet = Bullet(my_circle.center, command)
            
            command['A_pressed'] = True
            command['move'] = True
            bullet = Bullet(Student.center, command,flag_lr)
            # bullet = Bullet(Student.center, command)
            bullets.append(bullet)
            
            # bullet.move(command)
            # Student.state='attack'
            # print(Student.state)
            # th_1=threading.Thread(target=show_Moving,args=(Student,my_image))
            # th_1.start()
        # for bullet in bullets:
        #     bullet.move()

        my_circle.move(command)
        Student.move(command)
        Student.attack(command)
        for bullet in bullets:
            bullet.move()
            bullet.hit_wall_check(joystick.width, joystick.height)    #벽에 닿으면 hit 판정
            bullet.collision_check(enemys_list,Student)

        
            
        
        # my_draw.ellipse(tuple(my_circle.position), outline = my_circle.outline, fill = (0, 0, 0))
        # print("position: ",my_circle.position[0],my_circle.position[1],my_circle.position[2],my_circle.position[3])
        # print("center: ",my_circle.center[0],my_circle.center[1])


        Student.collision_check(enemys_list)
        

        for enemy in enemys_list:
            if enemy.state != 'die':
                #my_draw.ellipse(tuple(enemy.position), outline = enemy.outline, fill = (255, 0, 0))
                
                #my_image.paste(Subject_img,tuple((enemy.center)),mask)     #투명부분은 안 보이도록 설정
                # my_image.paste(Subject_img_border,tuple((enemy.center)-25),mask)     #투명부분은 안 보이도록 설정
                # enemy.collision_check(bullets)
                enemy.move(Student)
                
                # _, _, _, mask = Subject_img_border.split()
                # my_image.paste(Subject_img_border,tuple((enemy.center)-enemy.width_ego),mask)     #투명부분은 안 보이도록 설정
                _, _, _, mask = Subject_img.split()
                my_image.paste(Subject_img,tuple((enemy.center)-enemy.width_ego),mask)     #투명부분은 안 보이도록 설정
                

            elif enemy.die_flag==0 and enemy.state == 'die':
                print("enemy.state: ",enemy.state,"enemy: ",enemy)
                timer(0,enemy)     # timer ISR을 실행시켜 일정 시간 이후 sign_regen값을 주도록 하기 위함
                enemy.die_flag=1  # enemy.state == 'die' 의 판단을 한번만 하도록 하기위함(timer ISR 여러번 실행 방지)
                
                
                th=threading.Thread(target=show_Explode,args=(enemy,my_image))
                th.start()
                
            if enemy.sign_regen==1:
                print("hi",enemy)
                # enemy.regen((enemy.center),0,0) 
                select=random.randint(0,2)
                if select==0:
                    enemy.regen((235,random.randint(0,240)),0,0)
                elif select==1:
                    enemy.regen((5,random.randint(0,240)),0,0)
                
    
        # for img in Char_r_list:
        #         Char_1=ImageOps.expand(img, border=1, fill='red')   #image의 경계선(border)를 그림
        #         _, _, _, mask = Char_1.split()
        #         # my_image.paste(Char,tuple((Student.center)-20),mask)     #투명부분은 안 보이도록 설정
        #         my_image.paste(Char_1,(50,150),mask)     #투명부분은 안 보이도록 설정
        #         #joystick.disp.image(my_image)
        #         #my_image.paste(back_g,(0,0))
                
                
        # for enemy in enemys_list:
        # #     enemy.move(Student)
        #     enemy.collision_check(bullets)
       

        # for enemy in enemys_list:
        #     if enemy.sign_regen==1:
        #         print("hi",enemy)
        #         # enemy.regen((enemy.center),0,0) 
        #         enemy.regen((235,random.randint(0,240)),0,0)

        for bullet in bullets:
            if bullet.state != 'hit':
                
                my_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (255, 255, 0))
                
            else:
                
                bullets.remove(bullet)  #총알이 계속 list에 존재하는 것 방지
                

    
        if Student.state != 'attack' and not flag_attack:
            _, _, _, mask = Char.split()
            # my_image.paste(Char,tuple((Student.center)-20),mask)     #투명부분은 안 보이도록 설정
            my_image.paste(Char,tuple((Student.center)-Student.width_ego),mask)     #투명부분은 안 보이도록 설정
            
        elif Student.state == 'attack':
            # for img in Char_r_list:
            #     Char=ImageOps.expand(img, border=1, fill='red')   #image의 경계선(border)를 그림
            #     _, _, _, mask_1 = Char.split()   #투명부분은 안 보이도록 설정
            #     #mask를 mask_1으로 선언하여, 앞선 mask와 겹치지 않도록 함
            #     my_image.paste(Char,tuple((Student.center)-Student.width_ego),mask_1) 
            #     image = ImageChops.subtract(my_image,back_g)    #폭발하는 부분만 가져옴
            #     image_f=ImageChops.add(back_g_origin,image)     #기본 배경에 폭발하는 부분만 더함
            #     # back_g=image_f
                
            #     joystick.disp.image(my_image)    
            #     # my_image.paste(image_f,(0,0))    #터지는 것 구현 시, back_g를 이용
            # th_1=threading.Thread(target=show_Moving,args=(Student,my_image))
            # th_1.start()

            _, _, _, mask = Char.split()
            # my_image.paste(Char,tuple((Student.center)-20),mask)     #투명부분은 안 보이도록 설정
            my_image.paste(Char,tuple((Student.center)-Student.width_ego),mask)
            # continue


        my_draw.text(text_pos,text[0]+text[1],(255,255,255),font=font)
        my_draw.text((0,10),text[2]+text[3],(255,255,255),font=font)
        my_draw.text((180,0),text[4]+str(stage),(255,255,255),font=font)

        if Student.life<=0: #life 모두 소모
            
            while joystick.button_B.value:
                joystick.disp.image(game_over)    
                stage=1
            Student.life=3      #초기화
            Student.score=0
            
            Student= Character(joystick.width, joystick.height)
            enemy_1.regen((5,60),0,0)
            enemy_2.regen((5, 90),0,0)
            enemy_3.regen((5, 120),0,0)
            enemy_4.regen((235, 60),0,0)
            enemy_5.regen((235, 90),0,0)
            enemy_6.regen((235, 120),0,0)
            for bullet in bullets:
                bullet.state ='hit'
            for bullet in bullets:
                bullets.remove(bullet)
            my_image.paste(back_g_origin,(0,0))
            # joystick.disp.image(my_image)
            
        if Student.score>=18:   #한 stage clear
            stage+=1
            Student.score=0
        if stage==5:            #전체 stage clear
            while joystick.button_B.value:
                joystick.disp.image(game_clear)    
                stage=1
            Student.life=3      #초기화
            Student.score=0
            
            Student= Character(joystick.width, joystick.height)
            my_image.paste(back_g_origin,(0,0))
            enemy_1.regen((5,60),0,0)
            enemy_2.regen((5, 90),0,0)
            enemy_3.regen((5, 120),0,0)
            enemy_4.regen((235, 60),0,0)
            enemy_5.regen((235, 90),0,0)
            enemy_6.regen((235, 120),0,0)
            for bullet in bullets:
                bullet.state ='hit'
            for bullet in bullets:
                bullets.remove(bullet)
            my_image.paste(back_g_origin,(0,0))
            
            

        # print("bullets: ",bullets)

        #좌표는 동그라미의 왼쪽 위, 오른쪽 아래 점 (x1, y1, x2, y2)
        #joystick.disp.image(my_image)
        # joystick.disp.image(my_image)
        # my_image.paste(back_g,(0,0))
        # for bullet in bullets:
        #     bullet.collision_check(enemys_list)
            
        
        
def show_Explode(enemy,my_image):     #터지는 장면 보이기 위해 thread 함수 정의
    global back_g
    global back_g_origin
    for explode_img in explode_img_list:
        _, _, _, mask_1 = explode_img.split()   #투명부분은 안 보이도록 설정
        #mask를 mask_1으로 선언하여, 앞선 mask와 겹치지 않도록 함
        my_image.paste(explode_img,tuple((enemy.center)-enemy.width_ego),mask_1) 
        
        # timer_1(0)
        # joystick.disp.image(my_image) #그냥 쓰면 검은 화면만 나옴...

        image = ImageChops.subtract(my_image,back_g)    #폭발하는 부분만 가져옴
        image_f=ImageChops.add(back_g_origin,image)     #기본 배경에 폭발하는 부분만 더함
        back_g=image_f
        
          
        time.sleep(0.05)    #이 정도의 시간 간격이 있어야 터지는 게 자연스럽게 보임(안그러면 너무 빠름)
    # print("show_Explode over")
    back_g=back_g_origin
    enemy.regen((-60,-60),0,0)
    # 안보이는 곳으로 옮김으로써 터진 위치에서 계속 hit 판정을 안나도록 함
    # (이래야 총알이 방금 맞혔던 자리 지나가도 보임)
            

# def show_Moving(Student,my_image):
#     global back_g
#     global back_g_origin
#     global Char
#     global flag_attack
#     for img in Char_r_list:
#     # for img in explode_img_list:
#         flag_attack=1
#         Char=ImageOps.expand(img, border=1, fill='red')   #image의 경계선(border)를 그림
#         _, _, _, mask_1 = Char.split()   #투명부분은 안 보이도록 설정
#         #mask를 mask_1으로 선언하여, 앞선 mask와 겹치지 않도록 함
#         my_image.paste(Char,tuple((Student.center)-Student.width_ego),mask_1) 
        
#         # timer_1(0)
#         # joystick.disp.image(my_image) #그냥 쓰면 검은 화면만 나옴...

#         image = ImageChops.subtract(my_image,back_g)    #폭발하는 부분만 가져옴
#         image_f=ImageChops.add(back_g_origin,image)     #기본 배경에 폭발하는 부분만 더함
#         back_g=image_f
        
          
#         time.sleep(0.05)    #이 정도의 시간 간격이 있어야 터지는 게 자연스럽게 보임(안그러면 너무 빠름)
#     print("show_Moving over")
#     flag_attack=0
#     back_g=back_g_origin
            
        


def timer(count,enemy):
    #global count   #global로 하면 동시에 여러개 timer 동작 못함
    count+=1
    # print(count)
    t=threading.Timer(1,timer,args=(count,enemy,))    #"enemy"말고 마지막에 "enemy,"로 꼭 ,붙이기!!!!
   
    t.start()
    if count >=3:   #timer 시간
        count=0     #timer 초기화
        enemy.sign_regen=1    # regen함수를 실행 시키기 위함
        # print("Jam",enemy)
        # print("타이머를 멈춥니다")
        t.cancel()      #timer 종료


# def timer_1(count):
#     #global count   #global로 하면 동시에 여러개 timer 동작 못함
#     count+=1
#     print("timer_1: ",count)
#     t=threading.Timer(0.1,timer_1,args=(count,))    #"enemy"말고 마지막에 "enemy,"로 꼭 ,붙이기!!!!
   
#     t.start()
#     if count >=3:   #timer 시간
#         count=0     #timer 초기화
        
#         print("timer_1 타이머를 멈춥니다")
#         t.cancel()      #timer 종료
if __name__ == '__main__':
    main()