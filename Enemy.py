import numpy as np
import threading
import time


count=0
#sign_regen=0
class Enemy:
    #global sign_regen   #sign_regen을 gloabal 변수로 선언(timer가 값을 넣어줄 수 있도록)
    def __init__(self, spawn_position,die_flag,sign_regen):
        self.appearance = 'circle'
        self.state = 'alive'
        self.position = np.array([spawn_position[0] - 25, spawn_position[1] - 25, spawn_position[0] + 25, spawn_position[1] + 25])
        
        #self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.center = np.array([int((self.position[0] + self.position[2]) / 2), int((self.position[1] + self.position[3]) / 2)])
        self.outline = "#00FF00"

        self.die_flag=die_flag
        self.sign_regen=sign_regen

        
        
    def regen(self,spawn_position,die_flag,sign_regen): # regen이라는 함수를 정의해야만
        #global sign_regen
        #timer()
        #time.sleep(2)
        # if sign_regen==1:
        #     print("hi")
        #     sign_regen=0
        #     self.state = 'alive'
        #     self.position = np.array([spawn_position[0] - 25, spawn_position[1] - 25, spawn_position[0] + 25, spawn_position[1] + 25])
        #     self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        #     self.outline = "#00FF00"
        # else:
        #     print("oh..")
        #sign_regen=0
        
        self.appearance = 'circle'
        self.state = 'alive'
        self.position = np.array([spawn_position[0] - 25, spawn_position[1] - 25, spawn_position[0] + 25, spawn_position[1] + 25])
        #self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.center = np.array([int((self.position[0] + self.position[2]) / 2), int((self.position[1] + self.position[3]) / 2)])
        self.outline = "#00FF00"

        self.die_flag=die_flag
        self.sign_regen=sign_regen

        
    


        
def timer():
    global count
    #global sign_regen
    count+=1
    print(count)
    t=threading.Timer(1,timer)
    t.start()
    if count ==5:
        count=0
        #sign_regen=1
        Enemy.sign_regen=1    # regen함수를 실행 시키기 위함
        #Ene.regen(spawn_position)
        print("타이머를 멈춥니다")
        t.cancel()
        
    
#Enemy.regen(100,5)

    


    