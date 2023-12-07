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

        self.width_ego=25   #Enemy가 차지하는 width,height (내가 설정하기 나름)
        self.height_ego=25

        
        
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


    def move(self,Character):
        # self.appearance = 'circle'
        # self.state = 'alive'
        # self.outline = "#00FF00"

        

        if Character.center[0]!=self.center[0] :
            if Character.center[0]>self.center[0]:
                # self.center=np.array([int((self.position[0] + self.position[2]) / 2), int((self.position[1] + self.position[3]) / 2)])
                self.center[0]+=1
            if Character.center[0]<self.center[0]:
                # self.center=np.array([int((self.position[0] + self.position[2]) / 2), int((self.position[1] + self.position[3]) / 2)])
                self.center[0]-=1
        if Character.center[1]!=self.center[1] :
            if Character.center[1]>self.center[1]:
                # self.center=np.array([int((self.position[0] + self.position[2]) / 2), int((self.position[1] + self.position[3]) / 2)])
                self.center[1]+=1
            if Character.center[1]<self.center[1]:
                # self.center=np.array([int((self.position[0] + self.position[2]) / 2), int((self.position[1] + self.position[3]) / 2)])
                self.center[1]-=1

   

    


    