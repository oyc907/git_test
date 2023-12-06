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
        
        
        #center update
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
            
    def collision_check(self, enemys):
        for enemy in enemys:
            collision = self.overlap(self.position, enemy.position)
            
            if collision:
                enemy.state = 'die'
                self.state = 'hit'

    def overlap(self, ego_position, other_position):
        '''
        두개의 사각형(bullet position, enemy position)이 겹치는지 확인하는 함수
        좌표 표현 : [x1, y1, x2, y2]
        
        return :
            True : if overlap
            False : if not overlap
        '''
        return ego_position[0] > other_position[0] and ego_position[1] > other_position[1] \
                 and ego_position[2] < other_position[2] and ego_position[3] < other_position[3]
        #return에서 \은 그저 줄바꿈
    
    def hit_wall_check(self,width,height):
        if self.center[0]>width or self.center[0]<=0:    #x좌표가 화면 밖으로 넘어감
            self.state='hit'
        if self.center[1]>height or self.center[1]<=0:    #y좌표가 화면 밖으로 넘어감
            self.state='hit'