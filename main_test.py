'''
- 시간상 생략된 것.
- 플레이에 플레이어수 입력받는 것으로 처리. 이후 붕괴까지 구현시 시간 남으면, 다시 버튼에 숫자를 심는 형태로 바꿀 예정.
- 처음 턴 누구(플레이어 1고정.)

### 201113(15:00) 세형, 지원 패치노트
GUI branch: util.py, main_test.py

- 스크린 사이즈 키움.
    > 메인 루프 안의 버튼들 크기 사이즈에 따라 일반화.

- 음악 함수 주석처리. (임시)
- util; from tkinter import *

- 지목(플레이어를 지목 x. 바로 특정 플레이어의 카드 지목)시 추측 함수 생성 및 연결 1차 완.
    > 추측 숫자가 spooky 두 수에 대응하면 붕괴. (오픈 여부 주의!)
    > 추측 실패시 먹은 타일 붕괴 후 오픈 (구현중..)
    > 붕괴시 카드의 확률 표기 삭제.

- 정렬) 붕괴되어 하나로 고정된 값과 두개의 spooky 평균값을 비교하게 코드 수정.

- TO-DO) 연쇄 붕괴
- 0. 현재 임시로 패안먹고 턴넘기기가 가능하나(테스트용) 다음주 주말에 막을 예정.

- 1. 붕괴;
    > 2차(지원). (연쇄 붕괴) 위의 타일의 붕괴에 따라 알고리즘 함수 생성 및 얽힌 타일 붕괴. >> 진행 중..
    > 2차(세형). 유추 실패시 먹은 타일 붕괴 후 지원이 함수에 연결 >> 진행 중..

- 2. 버튼 클릭시 효과음 추가. 이론 설명 및 난이도 세팅 함수들 생성. >> 진행 중.. 
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
class CARD():
    global RT
    def __init__(self,color,num):   # 알고리즘 업데이트; num = [숫자,숫자,확률,확률] : 한 원소에 4개 값 List.
        # Set card & font color
        if color == 1: # Black
            self.card_color = BLACK
            self.font_color = WHITE
        else:
            self.card_color = GRAY
            self.font_color = BLACK
        
        self.color = color
        if len(num) == 4:
            self.card_num = [num[0],num[1]]
            self.card_probability = [num[2],num[3]]
        elif len(num) == 1:
            self.card_num = num
            self.card_probability = 100
        self.width, self.height = CARD_SIZE
        self.opened = True
        self.number = PRINTTEXT("%s" % self.card_num, 18, color=self.font_color)
        self.probability = PRINTTEXT("%s" % self.card_probability, 15, color=self.font_color)

    def is_opened(self):
        self.opened = True
    
    def get_color(self):
        return self.color

    def get_num(self):
        return self.card_num

    def get_pro(self):
        return self.card_probability

    def out(self):
        pass
    
    def draw_img(self, loc=(0,0), action=True):
        x, y = loc[0:2]
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()        
        
        pygame.draw.rect(screen, self.card_color, [x,y,self.width,self.height])
        pygame.draw.rect(screen, WHITE, [x,y,self.width,self.height],1)
        
        if x < mouse_pos[0] < x + self.width and \
            y < mouse_pos[1] < y + self.height:    
            pygame.draw.rect(screen, RED, [x,y,self.width,self.height],1)
            
            if click[0] == 1:
                if action == None or YATT == 0:
                    if YATT == 0 and len(fti_b) == 0 and len(fti_w) == 0:
                        self.f_click_tile()
                    pass
                else: #print("클릭됨") # 확인용
                    self.f_click_tile()
        
        if self.opened == True:
            self.number._blit_(loc=(x + self.width/2, y + self.height/2))
            if len(self.get_num()) == 2:
                self.probability._blit_(loc=(x + self.width/2, y + self.height*3/4))
        
    def f_click_tile(self):
        global RT
        ct_tk=Tk()
        ct_tk.title("유추 수 입력")
        ct_tk.geometry("480x300+100+100")
        ct_tk.resizable(False, False)       # 창 크기 조절 가능 여부 거부

        t_num = self.card_num
        t_probability = self.card_probability

        label1 = Label(ct_tk, text=str(t_num))
        label2 = Label(ct_tk, text=str(t_probability))

        def sf_p(number, probability):
            x = random.randint(1,101)
            if x <= probability[0]:
                del number[number.index(number[1])]
                del probability

            else:
                del number[number.index(number[0])]
                del probability
            return number
            
        def ctcalc(event):
            global RT
            PGN = int(entry.get()) # The player's guess number.
            if PGN in self.card_num:
                self.card_num = sf_p(self.card_num, self.card_probability)
                self.number = PRINTTEXT("%s" % self.card_num, 18, color=self.font_color)
                label1.config(text="추측한 "+str(PGN)+"숫자가 타일에 존재 합니다!")
                if PGN == t_num:
                    label2.config(text="추측 성공! 연속 추측 가능.")
                    YATT -= 1
                    ct_tk.after(1000, ctd)
                else:
                    label2.config(text="붕괴는 시켰으나, 추측 수로 붕괴되지 않음.")
                    ct_tk.after(1000, ctd)

            else:
                label1.config(text="추측한 "+str(PGN)+"숫자가 타일에 존재 하지 않습니다..")
                label2.config(text="유추에 실패 하여 이번 턴에 휙득한 타일을 붕괴 후, 공개합니다.")
                
                NTC = RT.get_color()
                NTN = sf_p(RT.get_num(), RT.get_pro())

                label3 = Label(ct_tk, text="붕괴된 숫자 :"+str(NTN))
                label3.pack()

                NT = CARD(NTC, NTN)
                p[turn].deck_list.append(NT)
                del p[turn].deck_list[p[turn].deck_list.index(RT)]
                
                ct_tk.after(1500, ctd)

        def ctd():
            ct_tk.destroy()

        entry=Entry(ct_tk, bd = 20)
        entry.bind("<Return>", ctcalc)
        entry.pack(pady = 50)

        label1.pack()
        label2.pack()

        ct_tk.mainloop()

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

    sh = BUTTON("(option) test")

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
    global num_players, stn, turn, YATT, RT
    screen.fill(WHITE)
    done = False
    num_players = f_pn()
    stn = f_tn(num_players)
    make_card(num_players, stn)
    
    #play_music() # 임시 주석처리.
    
    f_ftile_color_arrnage(tii)

    select_card = PRINTTEXT("Select card", 20)      # msg, font 크기
    button_take = BUTTON("take a tile")             # button sample
    button_turn = BUTTON("Next")
    button_exit = BUTTON("Exit",active_color=RED)

    YATT = 0

    def next_turn(): # 메인 루프 밖으로 절대 빼지 마시오.
        global turn, pl_turn, YATT

        turn += 1
        YATT = 0        # You already took the tile. [먹기전: 0, 먹음: 1]
        time.sleep(2)   # 임시 2초 딜레이
        win = 0
        if turn == num_players:
            turn = 0
            
    def f_take_tile(): # 메인 루프 밖으로 절대 빼지 마시오. + 함수 위치 고정.
        global fti_b, fti_w, YATT, RT
        wtt = Tk()                             # 윈도우 창을 생성
        wtt.title("타일 가져오기")              # 타이틀
        wtt.geometry("480x300+100+100")        # "너비x높이+x좌표+y좌표"

        label1 = Label(wtt, text="1차 완성")         # 라벨 등록
        label1.pack(pady=10)
        label2 = Label(wtt, text="가져올 타일을 선택하세요.")         # 라벨 등록
        label2.pack(pady=10)
        
        pixelVirtual = PhotoImage(width=1, height=1) # 기준 픽셀 추가

        def sf_bb():
            global fti_b, p, YATT, RT

            if len(fti_b) == 0:
                label2.config(text="새캬 없는걸 왜 눌러.")
            else:
                RT = random.choice(fti_b)
                p[turn].deck_list.append(RT)
                fti_b.pop(fti_b.index(RT))
                YATT += 1
                wtt.after(1000, wttd)

        def sf_bw():
            global fti_w, p, YATT, RT
        
            if len(fti_w) == 0:
                label2.config(text="새캬 없는걸 왜 눌러.")
            else:
                RT = random.choice(fti_w)
                p[turn].deck_list.append(RT)
                fti_w.pop(fti_w.index(RT))
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
        button_take._draw_(loc = (SCREEN_WIDTH-100,100), size = (130,30), action = f_take_tile)
        button_turn._draw_(loc = (SCREEN_WIDTH-100,570), size = (60,30), action = next_turn)
        button_exit._draw_(loc = (SCREEN_WIDTH-100,50), size = (130,30), action = pygame.quit)
        select_card._blit_(loc=(5,30),loc_center=False) 
        
        pygame.display.update()

def make_card(num_players, stn):
    global p, tii
    
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
RT = 0      # 상동.
screen.fill(WHITE)                          # 화면 흰색으로 채움
pygame.display.update()                     # 화면 업데이트.

game_intro()                                # 실행 장면을 위한 함수들
shtestroom()
how_to_play()

main_loop()



pygame.quit()                               # pygame 종료

