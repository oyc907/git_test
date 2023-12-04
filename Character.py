import numpy as np

class Character:
    def __init__(self, width, height):
        self.appearance = 'circle'
        self.state = None
        self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])
        #position에서 얼마만큼 값 빼는 게 character의 크기를 알려줌(닿았을 때 알기 위해 필요)

        # 총알 발사를 위한 캐릭터 중앙 점 추가
        #self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.center = np.array([int((self.position[0] + self.position[2]) / 2), int((self.position[1] + self.position[3]) / 2)])
        self.outline = "#FFFFFF"

        self.width_ego=20   #Character가 차지하는 width,height (내가 설정하기 나름)
        self.height_ego=20

    def move(self, command = None):
        if command['move'] == False:
            self.state = None
            self.outline = "#FFFFFF" #흰색상 코드!
        
        else:
            self.state = 'move'
            self.outline = "#FF0000" #빨강색상 코드!

            if command['up_pressed']:
                self.position[1] -= 5
                self.position[3] -= 5

            if command['down_pressed']:
                self.position[1] += 5
                self.position[3] += 5

            if command['left_pressed']:
                self.position[0] -= 5
                self.position[2] -= 5
                
            if command['right_pressed']:
                self.position[0] += 5
                self.position[2] += 5
                
        #center update
        #self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2]) 
        self.center = np.array([int((self.position[0] + self.position[2]) / 2), int((self.position[1] + self.position[3]) / 2)])


    def collision_check(self, enemys):
        for enemy in enemys:
            #collision = self.overlap(self.center, enemy.center, enemy.die_flag)
            collision = self.overlap(self, enemy)
            
            if collision:
                enemy.state = 'die'
                self.state = 'hit'

    #def overlap(self, ego_center, other_center,other_die_flag):
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
            

        # if not other_die_flag and ego_center[0]<other_center[0] and ego_center[1]>other_center[1]:
        # # 주인공의 오른쪽 위에 Enemy가 존재
        # # not other_die_flag를 하는 이유는 닿는 판정을 한번만 하기위해서
        #     if (ego_center[0]+20)>(other_center[0]-25) and (ego_center[1]-20)<(other_center[1]+25):
        #     # 부딪혔을 때
        #         return 1 
        #     else:
        #         return 0
        