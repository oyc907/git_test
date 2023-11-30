import numpy as np
import threading
import time


count=0
sign_regen=0
class Enemy:
    
    def __init__(self, spawn_position):
        self.appearance = 'circle'
        self.state = 'alive'
        self.position = np.array([spawn_position[0] - 25, spawn_position[1] - 25, spawn_position[0] + 25, spawn_position[1] + 25])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#00FF00"

        # self.die_flag=die_flag
        # self.sign_regen=sign_regen
        
    def regen(self,spawn_position): # regen이라는 함수를 정의해야만
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
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#00FF00"

        # self.die_flag=die_flag
        # self.sign_regen=sign_regen


        
def timer(self, Ene ,spawn_position):
    global count
    global sign_regen
    count+=1
    print(count)
    t=threading.Timer(1,timer)
    t.start()
    if count ==5:
        count=0
        sign_regen=1
        Ene.regen(spawn_position)
        print("타이머를 멈춥니다")
        t.cancel()
        
    
#Enemy.regen(100,5)

    


    