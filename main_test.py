'''
- 시간상 플레이에 플레이어수 입력받는 것으로 처리.
- 이후 붕괴까지 구현시 시간 남으면, 다시 버튼에 숫자를 심는 형태로 바꿀 예정.
- TO-DO) 턴 관련 모든 것
- 1. 누구의 턴인가
- 2. 카드 휙득
- 3. 정렬
- 4. 지목 (플레이어를 지목 x. 바로 특정 플레이어의 카드 지목)
- 5. 유추
- 6. 붕괴
'''
# import pygame
from util import *
#======건들지 마시오=====
from shtest import *
from tkinter import *
#=======================

'''
=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=

fcn, num_players, stn 등에서 충돌로 코드 순서 수정.
functions for pygame > Initialize pygame 순서 고정 바람. 변동시 에러 가능성 높음.

=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=@=
'''
#========== functions for pygame ==========#
def game_intro():       # Game intro scene
    intro = False       # while문 돌리기 위함
    # Title Texts
    title = PRINTTEXT("Quantum Coda", size = 50)

    credits_title = PRINTTEXT("Credits", size = 30)
    credits_affilation = PRINTTEXT("Undergraduate Students, Department of Physics, Pukyong National University", size = 20)
    credits_name = PRINTTEXT("Jong hee Kim, Yong chul Lee, Yong Kwon, Sea hyoung Jo, Ji won Choi", size = 20)

    # Button Texts
    new_p2 = BUTTON("2 Player")
    new_p4 = BUTTON("4 Player")

    sh = BUTTON("sehyoung test")

    exit_button = BUTTON("Exit")
    play_button = BUTTON("Play!")
    how_button = BUTTON("How to Play?")

    while not intro:
        for event in pygame.event.get():        # 기본 event loop
            if event.type == pygame.QUIT:       # pygame 종료
                pygame.quit()
        
        # text positions
        title._blit_(loc= (SCREEN_WIDTH*1 // 2, SCREEN_HEIGHT*3 // 16))
        credits_title._blit_(loc=(SCREEN_WIDTH*1 // 2, SCREEN_HEIGHT-120))
        credits_affilation._blit_(loc=(SCREEN_WIDTH*1 // 2, SCREEN_HEIGHT-70))
        credits_name._blit_(loc=(SCREEN_WIDTH*1 // 2, SCREEN_HEIGHT-40))
        
        new_p2._draw_(loc = 'bottom left', size = (60,30), action=None)
        new_p4._draw_(loc = 'bottom right', size = (60,30),action=None)
        sh._draw_(loc = (800,SCREEN_HEIGHT*3 // 8), size = (180,30), action=shtestroom)
        
        play_button._draw_(loc = (SCREEN_WIDTH // 2, SCREEN_HEIGHT*3 // 8), size = (140,60),action=main_loop)
        how_button._draw_(loc = (SCREEN_WIDTH // 2, SCREEN_HEIGHT*4 // 8), size = (140,60),action=None)
        exit_button._draw_(loc = (SCREEN_WIDTH // 2, SCREEN_HEIGHT*5 // 8), size = (140,60),action=pygame.quit)

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
    global num_players, stn, turn
    screen.fill(WHITE)
    done = False
    num_players = f_pn()
    stn = f_tn(num_players)
    make_card(num_players, stn)

    select_card = PRINTTEXT("Select card", 20) # msg, font 크기
    button_sample = BUTTON("test")             # button sample
    button_turn = BUTTON("Next")

    def next_turn(): # 메인 루프 밖으로 절대 빼지 마시오.
        global turn
        turn += 1
        time.sleep(3)   # 임시 5초 딜레이
        win = 0
        if turn == num_players:
            turn = 0
        print(turn)

    while not done:
        for event in pygame.event.get():        # 닫기 전까지 계속 실행.
            if event.type == pygame.QUIT:       # 종료 if문
                pygame.quit()
                quit()
        
        pygame.init()
        
        pl_turn = PRINTTEXT("Turn of player"+str(turn+1),20)   

        # 덱의 카드 정렬
        all_arrange(p)
        
        # 덱 그리기
        
        for i in range(1,num_players):
            
            if i+turn < num_players:
                p[i+turn].draw_card(SCREEN_WIDTH/num_players+(i-1)*CARD_WIDTH*(stn+1)-stn/2*CARD_WIDTH, SCREEN_HEIGHT//4)
            
            elif i+turn >= num_players:
                p[i+turn-num_players].draw_card(SCREEN_WIDTH/num_players+(i-1)*CARD_WIDTH*(stn+1)-stn/2*CARD_WIDTH, SCREEN_HEIGHT//4)
        p[turn].draw_card(SCREEN_WIDTH//2-stn/2*CARD_WIDTH, SCREEN_HEIGHT*3//4)
        
        button_sample._draw_(loc=(100,100))
        button_turn._draw_(loc = (800,550), size = (60,30), action = next_turn)
        
        # 카드 지목
        select_card._blit_(loc=(5,30),loc_center=False)
        pl_turn._blit_(loc=(5,5),loc_center=False)     
        
        pygame.display.update()

def make_card(num_players, stn):
    global p
    players = [PLAYER() for i in range(num_players)] # 플레이어 수만큼 PLAYER()인스턴스로 players 객체 생성 & 이것은 리스트

    for i in range(num_players):
        globals()['p{}'.format(i+1)] = players[i]

    field_black = [] 
    field_white = []
    make_spooky(field_black)
    make_spooky(field_white)


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
    #print("섞은 전체 타일: ",ti)

    tii = [CARD(ti[i][0],ti[i][1]) for i in range(len(ti))] # 생성된 카드를 클래스로 복제

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

#======== Initialize pygame ==========#
pygame.init()                               # pygame library 초기화.
clock = pygame.time.Clock()                 # create an object to help track time.
clock.tick(30)                              # 딜레이 추가. Target_FPS = 30.
turn = 0    # 첫값 0. 수정 금지.

screen.fill(WHITE)                          # 화면 흰색으로 채움
pygame.display.update()                     # 화면 업데이트.

game_intro()                                # 실행 장면을 위한 함수들
shtestroom()
how_to_play()

main_loop()


pygame.quit()                               # pygame 종료

