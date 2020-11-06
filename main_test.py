import pygame
from util import *
#======건들지 마시오=====
from shtest import *
from tkinter import *
#=======================


'''
코드 순서도 일람 (나중에 더 괜찮은 배치가 있으면 수정바람)
- 카드 생성 및 배분 (알고리즘)
- pygame 진행에 필요한 함수들 (장면 추가시 함수추가바람.)
- 기본 pygame 실행 순서
'''

#========== 카드 생성 및 배분 ==========

stn = 4                         # starting tile number

players = [PLAYER() for i in range(num_players)] # 플레이어 수만큼 PLAYER()인스턴스로 players 객체 생성 & 이것은 리스트


for i in range(num_players):
    globals()['p{}'.format(i+1)] = players[i]

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

#========== functions for pygame ==========#
def game_intro():       # Game intro scene
    intro = False       # while문 돌리기 위함
    # Title Texts
    title = PRINTTEXT("Quantum Coda", size = 50)
    new_p2 = PRINTTEXT("2 Player", size=30)
    new_p3 = PRINTTEXT("3 Player", size=30)
    new_p4 = PRINTTEXT("4 Player", size=30)

    # Button Texts
    new_p2 = BUTTON("new_p2")
    new_p3 = BUTTON("new_p3")
    new_p4 = BUTTON("new_p4")
    sh = BUTTON("sehyoung test")

    while not intro:
        for event in pygame.event.get():        # 기본 event loop
            if event.type == pygame.QUIT:       # pygame 종료
                pygame.quit()
        
        # text positions
        title._blit_(loc='top center')
        
        new_p2._draw_(loc = 'bottom left', size = (60,30), action=how_to_play)
        new_p3._draw_(loc = 'bottom center', size = (60,30), action=main_loop)
        new_p4._draw_(loc = 'bottom right', size = (60,30),action=next_turn)
        sh._draw_(loc = (800,550), size = (180,30), action=shtestroom)

        pygame.display.update()
        clock.tick(15)

def how_to_play(): # scene for game description # 장면 테스트 중
    screen.fill(WHITE)
    dp = PRINTTEXT("Quantum", size = 50)
    play = False
    while not play:
        for event in pygame.event.get():        # 기본 event loop
            if event.type == pygame.QUIT:       # pygame 종료
                pygame.quit()
        
        # text positions
        dp._blit_(loc='top center')

        pygame.display.flip()


def main_loop(): # Game main loop scene
    screen.fill(WHITE)
    done = False

    select_card = PRINTTEXT("Select card", 20) # msg, font 크기
    button_sample = BUTTON("test")             # button sample
    button_turn = BUTTON("Next")

    while not done:
        for event in pygame.event.get():        # 닫기 전까지 계속 실행.
            if event.type == pygame.QUIT:       # 종료 if문
                pygame.quit()
                quit()
        
        # 덱의 카드 정렬
        p[0].tile_arrange()
        p[1].tile_arrange()
        
        # 덱 그리기
        p[1].draw_card(300, 400)
        p[0].draw_card(300, 100)    
        
        button_sample._draw_(loc=(100,100))
        button_turn._draw_(loc = (800,550), size = (60,30))
        
        # 카드 지목
        select_card._blit_(loc=(5,30),loc_center=False)
        pl_turn._blit_(loc=(5,5),loc_center=False)        
        
        pygame.display.update()

#======== Initialize pygame ==========
pygame.init()                               # pygame library 초기화.
clock = pygame.time.Clock()                 # create an object to help track time.
clock.tick(30)                              # 딜레이 추가. Target_FPS = 30.

screen.fill(WHITE)                          # 화면 흰색으로 채움
pygame.display.update()                     # 화면 업데이트.

game_intro()                                # 실행 장면을 위한 함수들
shtestroom()
how_to_play()
main_loop()


pygame.quit()                               # pygame 종료


