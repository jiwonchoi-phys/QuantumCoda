'''
- 시간상 플레이에 플레이어수 입력받는 것으로 처리.
- 이후 붕괴까지 구현시 시간 남으면, 다시 버튼에 숫자를 심는 형태로 바꿀 예정.

- TO-DO) 붕괴 관련 모든 것.
- 0. 처음 턴 누구(일단 생략. 플레이어 1고정.) 
- 1. 카드 휙득 및 패 추가함수 생성. >> 1차 완.
- 2. 각각의 카드 패 위에 누구의 패인지 텍스트 추가. (턴넘김시 타일위치 변경에 따라 같이 변경.) >> 진행 중..
    >>> util의 max_card_num = 5 에서 5가 아닌 숫자에서 에러 발생확인. 원인 확인 중..
========= 아래 진행 바람 ==============================================================
- 4. 지목(플레이어를 지목 x. 바로 특정 플레이어의 카드 지목)시 추측 함수 생성 및 연결.
    > 1차. 해당 값에 타일의 spooky 수 유무 검토 있으면 해당 타일 붕괴.
    > 2치. 위의 타일의 붕괴에 따라 알고리즘 쪽 함수 가져와서 얽힌 타일 붕괴.


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
    screen.fill(WHITE)
    intro = False       # while문 돌리기 위함
    # Title Texts
    title = PRINTTEXT("Quantum Coda", size = 50)

    credits_title = PRINTTEXT("Credits", size = 30)
    credits_affilation = PRINTTEXT("Undergraduate Students, Department of Physics, Pukyong National University", size = 20)
    credits_name = PRINTTEXT("Jong hee Kim, Yong chul Lee, Yong Kwon, Sea hyoung Jo, Ji won Choi", size = 20)

    # Button Texts
    new_test1 = BUTTON("test 1")
    new_test2 = BUTTON("test 2")

    sh = BUTTON("sehyoung test")

    title_exit_button = BUTTON("Exit",active_color=RED)
    play_button = BUTTON("Play!")
    how_button = BUTTON("How to Play?")

    while not intro:
        for event in pygame.event.get():        # 기본 event loop
            if event.type == pygame.QUIT:       # pygame 종료
                pygame.quit()
        
        # text positions
        title._blit_(loc= (SCREEN_WIDTH*1 // 2, SCREEN_HEIGHT*3 // 16))
        credits_title._blit_(loc=(SCREEN_WIDTH*1 // 2, SCREEN_HEIGHT-100))
        credits_affilation._blit_(loc=(SCREEN_WIDTH*1 // 2, SCREEN_HEIGHT-70))
        credits_name._blit_(loc=(SCREEN_WIDTH*1 // 2, SCREEN_HEIGHT-40))
        
        new_test1._draw_(loc = 'bottom left', size = (60,30), action=None)
        new_test2._draw_(loc = 'bottom right', size = (60,30),action=None)
        sh._draw_(loc = (800,SCREEN_HEIGHT*3 // 8), size = (180,30), action=shtestroom)
        
        play_button._draw_(loc = (SCREEN_WIDTH // 2, SCREEN_HEIGHT*3 // 8), size = (140,60),action=main_loop)
        how_button._draw_(loc = (SCREEN_WIDTH // 2, SCREEN_HEIGHT*4 // 8), size = (140,60),action=how_to_play)
        title_exit_button._draw_(loc = (SCREEN_WIDTH // 2, SCREEN_HEIGHT*5 // 8), size = (140,60),action=pygame.quit)

        pygame.display.update()
        clock.tick(15)

def how_to_play(): # scene for game description # 장면 테스트 중
    screen.fill(WHITE)
    play = False

    dp = PRINTTEXT("Quantum Coda는 기존의 Coda(다빈치 코드)게임에 양자역학적 현상을 접목시켜 만든 게임입니다.", size = 20)
    
    back_button = BUTTON("Back to Title")
    exit_button = BUTTON("Exit")

    while not play:
        for event in pygame.event.get():        # 기본 event loop
            if event.type == pygame.QUIT:       # pygame 종료
                pygame.quit()

        # text positions
        dp._blit_(loc='top center')
        
        back_button._draw_(loc = (800,50), size = (130,30), action = game_intro)
        exit_button._draw_(loc = (800,100), size = (130,30), action = pygame.quit)

        pygame.display.flip()
        clock.tick(15)


def main_loop(): # Game main loop scene
    global num_players, stn, turn, YATT
    screen.fill(WHITE)
    done = False
    num_players = f_pn()
    stn = f_tn(num_players)
    make_card(num_players, stn)
    
    play_music()
    
    f_ftile_color_arrnage(tii)

    select_card = PRINTTEXT("Select card", 20)      # msg, font 크기
    button_take = BUTTON("take a tile")             # button sample
    button_turn = BUTTON("Next")
    button_exit = BUTTON("Exit",active_color=RED)

    YATT = 0

    def next_turn(): # 메인 루프 밖으로 절대 빼지 마시오.
        global turn, pl_turn, YATT

        turn += 1
        YATT = 0
        time.sleep(2)   # 임시 2초 딜레이
        win = 0
        if turn == num_players:
            turn = 0
            
    def f_take_tile(): # 메인 루프 밖으로 절대 빼지 마시오. + 함수 위치 고정.
        global fti_b, fti_w, YATT
        wtt = Tk()                              # 윈도우 창을 생성
        wtt.title("타일 가져오기")     # 타이틀
        wtt.geometry("480x300+100+100")         # "너비x높이+x좌표+y좌표"

        label1 = Label(wtt, text="1차 완성")         # 라벨 등록
        label1.pack(pady=10)
        label2 = Label(wtt, text="가져올 타일을 선택하세요.")         # 라벨 등록
        label2.pack(pady=10)
        
        pixelVirtual = PhotoImage(width=1, height=1) # 기준 픽셀 추가

        def sf_bb():
            global fti_b, p, YATT

            if len(fti_b) == 0:
                label2.config(text="새캬 없는걸 왜 눌러.")
            else:
                qwer = random.choice(fti_b)
                p[turn].deck_list.append(qwer)
                fti_b.pop(fti_b.index(qwer))
                YATT += 1
                wtt.after(1000, wttd)

        def sf_bw():
            global fti_w, p, YATT
        
            if len(fti_w) == 0:
                label2.config(text="새캬 없는걸 왜 눌러.")
            else:
                qwer = random.choice(fti_w)
                p[turn].deck_list.append(qwer)
                fti_w.pop(fti_w.index(qwer))
                YATT += 1
                wtt.after(1000, wttd)
    
        bb = Button(wtt, text='검정색 가져오기\n'+'남은 타일 수: '+str(len(fti_b)), command = sf_bb, fg = 'white', bg = "black",
                    image=pixelVirtual, width=100, height=160, compound="c")                # 크기 텍스트 기준이 아닌 기준 픽셀 기준, 텍스트는 중앙표기.
        bw = Button(wtt, text='하양색 가져오기\n'+'남은 타일 수: '+str(len(fti_w)), command = sf_bw, fg = 'black', bg = "ghost white",
                    image=pixelVirtual, width=100, height=160, compound="c")
        bb.pack(side = LEFT, padx = 50)
        bw.pack(side = RIGHT, padx = 50)

        def wttd():              # tk 파괴. 위 elif에 바로 연결시 라벨 변경 안멱혀서 따로 뗌
            wtt.destroy()

        if len(fti_b) == 0 and len(fti_w) == 0:
            label2.config(text="더 이상 타일이 없습니다.")
            
            wtt.after(1000, wttd)
        
        if YATT == 1:
            label2.config(text="이번 턴에 이미 패를 먹었습니다.")
            bb.destroy()
            bw.destroy()
            wtt.after(1000, wttd)

        wtt.mainloop()

    #========== main loop 창 실행 ==========#
    while not done:
        for event in pygame.event.get():        # 닫기 전까지 계속 실행.
            if event.type == pygame.QUIT:       # 종료 if문
                pygame.quit()
                quit()

        # 턴 관련
        pygame.draw.rect(screen, WHITE, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT])          # 삭제금지.
        pl_turn = PRINTTEXT("Turn of player "+str(turn+1), 25)
        pl_turn._blit_(loc=(5,5),loc_center=False)  
        #print("2차",turn)
        # 덱의 카드 정렬
        all_arrange(p)
        
        # 덱 그리기(플러이어 텍스트 포함)
        Ttext = list(range(num_players))
        Ttext[0] = PRINTTEXT('Yours:', size= 20)
        for i in range(1,num_players):
            Ttext[i] = PRINTTEXT('Player: '+str(i+turn+1), size= 15)
            if i+turn+1 > num_players:
                Ttext[i] = PRINTTEXT('Player: '+str(i+turn+1-num_players), size= 15)
        f_draw_card(p, turn, Ttext)
        
        # 버튼 및 텍스트 그리기
        button_take._draw_(loc = (800,100), size = (130,30), action = f_take_tile)
        button_turn._draw_(loc = (800,570), size = (60,30), action = next_turn)
        button_exit._draw_(loc = (800,50), size = (130,30), action = pygame.quit)
        select_card._blit_(loc=(5,30),loc_center=False) 
        
        pygame.display.update()

def make_card(num_players, stn):
    global p, tii
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

def f_ftile_color_arrnage(tii):           
    global fti_b, fti_w
    fti_b = []  # 검은색을 뽑을건지 흰색을 뽑을건지 플레이어가 정함
    fti_w = []  # 그래서 따로 검은색 흰색 그룹을 생성

    for i in range(len(tii)):  # 검은색 흰색 그룹에 색에 맞게 넣음
        if tii[i].get_color() == 1:
            fti_b.append(tii[i])
        elif tii[i].get_color() == 0:
            fti_w.append(tii[i])

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

