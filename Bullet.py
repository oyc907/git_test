import numpy as np

class Bullet:
    def __init__(self, position, command,flag_lr):
        self.appearance = 'rectangle'
        self.speed = 10
        self.damage = 10
        self.position = np.array([position[0]-3, position[1]-3, position[0]+3, position[1]+3])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.direction = {'up' : False, 'down' : False, 'left' : False, 'right' : False}
        self.state = None
        self.outline = "#FFFF00"

        self.width_ego=3   #Bullet가 차지하는 width,height (내가 설정하기 나름)
        self.height_ego=3
        # if command['up_pressed']:
        #     self.direction['up'] = True
        # if command['down_pressed']:
        #     self.direction['down'] = True
            
        # if command['right_pressed']:
        if not flag_lr:
            self.direction['right'] = True

        # if command['left_pressed']:
        elif flag_lr:
            self.direction['left'] = True
        


        # if command['up_pressed']:
        #     self.direction['up'] = True
        # if command['down_pressed']:
        #     self.direction['down'] = True
            
        # if command['right_pressed']:
        # # if not flag_lr:
        #     self.direction['right'] = True

        # if command['left_pressed']:
        # # elif flag_lr:
        #     self.direction['left'] = True
        
        

    def move(self):
        # if self.direction['up']:
        #     self.position[1] -= self.speed
        #     self.position[3] -= self.speed

        # if self.direction['down']:
        #     self.position[1] += self.speed
        #     self.position[3] += self.speed

        # if self.direction['left']:
        #     self.position[0] -= self.speed
        #     self.position[2] -= self.speed

         
        # if self.direction['right']:

        # if not flag_lr: #오른쪽
        if self.direction['right'] == True:
            self.position[0] += self.speed
            self.position[2] += self.speed


        else:   #왼쪽

            self.position[0] -= self.speed
            self.position[2] -= self.speed






        # if self.direction['up']:
        #     self.position[1] -= self.speed
        #     self.position[3] -= self.speed

        # if self.direction['down']:
        #     self.position[1] += self.speed
        #     self.position[3] += self.speed

        # if self.direction['left']:
        #     self.position[0] -= self.speed
        #     self.position[2] -= self.speed

         
        # # if self.direction['right']:

        # # if not flag_lr: #오른쪽
        # if self.direction['right'] == True:
        #     self.position[0] += self.speed
        #     self.position[2] += self.speed


        # # else:   #왼쪽
        # if self.direction['left']:
        #     self.position[0] -= self.speed
        #     self.position[2] -= self.speed
        
        
        #center update
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
            
    def collision_check(self, enemys,Character):
        
        for enemy in enemys:
            # collision = self.overlap(self.position, enemy.position)
            collision = self.overlap(self, enemy)
            
            if collision:
                enemy.state = 'die'
                self.state = 'hit'
                Character.score+=1
                print("Bullet!! collision bullet: ",self.center,enemy.center)

    # def overlap(self, ego_position, other_position):
    def overlap(self, ego, other):
        '''
        두개의 사각형(bullet position, enemy position)이 겹치는지 확인하는 함수
        좌표 표현 : [x1, y1, x2, y2]
        
        return :
            True : if overlap
            False : if not overlap
        '''
        # return ego_position[0] > other_position[0] and ego_position[1] > other_position[1] \
        #          and ego_position[2] < other_position[2] and ego_position[3] < other_position[3]
        # #return에서 \은 그저 줄바꿈




        if not other.die_flag and ego.center[0]<=other.center[0] and ego.center[1]>=other.center[1]:
        # 주인공의 오른쪽 위에 Enemy가 존재
        # not other_die_flag를 하는 이유는 닿는 판정을 한번만 하기위해서
            if (ego.center[0]+ego.width_ego)>=(other.center[0]-other.width_ego) and (ego.center[1]-ego.height_ego)<=(other.center[1]+other.height_ego):
            # 부딪혔을 때
                return 1 
            else:
                return 0
        if not other.die_flag and ego.center[0]>=other.center[0] and ego.center[1]>=other.center[1]:
        # 주인공의 왼쪽 위에 Enemy가 존재
            if (ego.center[0]-ego.width_ego)<=(other.center[0]+other.width_ego) and (ego.center[1]-ego.height_ego)<=(other.center[1]+other.height_ego):
            # 부딪혔을 때
                return 1 
            else:
                return 0
        if not other.die_flag and ego.center[0]>=other.center[0] and ego.center[1]<=other.center[1]:
        #주인공의 왼쪽 아래에 Enemy가 존재
            if (ego.center[0]-ego.width_ego)<=(other.center[0]+other.width_ego) and (ego.center[1]+ego.height_ego)>=(other.center[1]-other.height_ego):
            # 부딪혔을 때
                return 1 
            else:
                return 0
        if not other.die_flag and ego.center[0]<=other.center[0] and ego.center[1]<=other.center[1]:
        #주인공의 오른쪽 아래에 Enemy가 존재
            if (ego.center[0]+ego.width_ego)>=(other.center[0]-other.width_ego) and (ego.center[1]+ego.height_ego)>=(other.center[1]-other.height_ego):
            # 부딪혔을 때
                return 1 
            else:
                return 0


    
    def hit_wall_check(self,width,height):
        if self.center[0]>width or self.center[0]<=0:    #x좌표가 화면 밖으로 넘어감
            self.state='hit'
        if self.center[1]>height or self.center[1]<=0:    #y좌표가 화면 밖으로 넘어감
            self.state='hit'