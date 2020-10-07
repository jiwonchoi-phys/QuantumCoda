import pygame
from util import *

#======== Initialize pygame ==========
pygame.init()                               # pygmae library 초기화.
pygame.display.set_caption("Quantum Coda")  # 타일틀바에 텍스트 출력.
clock = pygame.time.Clock()                 # create an object to help track time.
done = False
clock.tick(30)                              # 딜레이 추가. Target_FPS = 30.


screen = pygame.display.set_mode(SCREEN_SIZE)   # util에서 정의.
screen.fill(WHITE)
pygame.display.update()                         # 화면 업데이트.


select_card = PRINTTEXT("Select card", 20) # msg, font 크기
button_sample = BUTTON("test")             # button sample


#========== 카드 생성 및 배분 ==========
num_players = 2                 # 임시 고정.
stn = 4                         # starting tile number

players = [PLAYER() for i in range(num_players)] # 플레이어 수만큼 PLAYER()인스턴스로 players 객체 생성 & 이것은 리스트


p1 = players[0]     # 생성된 리스트의 원소를 새 이름으로 지정
p2 = players[1]

field_black = [] 
field_white = []
make_spooky(field_black)
make_spooky(field_white)

fcn=(max_card_num+1)*2              # full card number

ti = []                             # 전체 타일 묶음
tb = []                             # Tile Black
tw = []                             # Tile White

for i in range(0,max_card_num+1):   # 색상 정보 추가 (Black: 1, While: 0 으로 구분하는 for문)
    tb.append([1,field_black[i]])
    tw.append([0,field_white[i]])
    ti.append(tb[i])
    ti.append(tw[i])                # ti에 0과 1로 구분하고 넣음


random.shuffle(ti)                  # 모든 타일 섞음
spooky_arrange(ti)                  # util 참고.
print("섞은 전체 타일: ",ti)

# 생성된 카드를 클래스로 복제 ??
tii = [CARD(ti[i][0],ti[i][1]) for i in range(len(ti))]

# num_players만큼 플레이어 생성
p = [PLAYER() for i in range(num_players)]

# PLAYER의 덱에 생성된 카드를 랜덤으로 추가
for i in range(num_players):
    p[i].deck_list = []
    p[i].opened_deck = []
    for k in range(0,stn):
        qwer = random.choice(tii)
        p[i].deck_list.append(qwer)
        tii.pop(tii.index(qwer))

        
turn = 1

pl_turn = PRINTTEXT("Turn of player"+str(turn),20)



#============ MAIN LOOP ============
while not done:

    for event in pygame.event.get():        # 닫기 전까지 계속 실행.
        if event.type == pygame.QUIT:
            done = True
        
        # 덱의 카드 정렬
        p[0].tile_arrange()       
        p[1].tile_arrange()
        
        # 덱 그리기
        p[0].draw_card(300, 400)
        p[1].draw_card(300, 100)        
        
        button_sample._draw_(loc=(100,100))
        
        # 카드 지목
        select_card._blit_(loc=(5,30),loc_center=False)
        pl_turn._blit_(loc=(5,5),loc_center=False)        
        
        pygame.display.flip()
        
        
pygame.quit()


