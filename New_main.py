#======건들지 마시오=====
from tkinter import *
import pygame
import math
import random
import numpy
import time
#=======================

'''
현재 순서 고정 바람. 변동시 에러 가능성 높음.
사운드 파일 추가시 .wav, .ogg 사용바람. .mp3 사용시 에러 가능성 높음
'''

# RGB color information
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)
RED     = (255,  0,  0)
GREEN   = (  0,255,  0)
BLUE    = (0  ,  0,255)
YELLOW  = (255,255,  0)
CYAN    = (  0,255,255)
MAGENTA = (255,  0,255)

ORANGE  = (255, 94,  0)
PURPLE  = (217, 65,197)
GRAY    = (201,201,201)
GRAY_2  = (169,169,169)

#======== Initialize pygame ==========
# Object size
SCREEN_WIDTH  = 1100
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Quantum Coda")  # 타일틀바에 텍스트 출력.

CARD_WIDTH = 60
CARD_SIZE = (CARD_WIDTH, 1.6*CARD_WIDTH)


max_card_num = 10   # 13까지 가능하나 10 완성 전까지 고정할 것. make_spooky 함수 안으로 넣지 말 것. 
cut_list=[] # 첫번째 원소가 black, 두번째 원소가 white
idx=0

"""
    ====================<<<     Util    >>>====================
"""
class PRINTTEXT():
    def __init__(self, msg, size, font='notosanscjkkr', color=BLACK, antialias=True, background=None):
        self.msg = msg                  # 메세지
        self.font = font                # font 지정 (기본 conslas)
        self.size = size                # size 지정
        self.antialias = antialias      # AA 지정 (기본 true)
        self.color = color              # 색상 지정 (기본 검정)
        self.background = background    # 바탕 지정 (기본 없음)
        texts = pygame.font.SysFont(self.font, self.size)   # texts는 지정한 폰트와 사이즈 사용
        self.text = texts.render(self.msg, self.antialias, self.color, self.background) # 렌더링.
    
    def _blit_(self, loc=(0,0), loc_center=True):   # 좌표 지정 위치 0,0의 오른쪽
        if loc_center == True:
            if loc == 'top center': 
                text_rect = self.text.get_rect()                                # 사각형 텍스트
                text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)      # 중간 위에서 1/4 지점(= top)
                screen.blit(self.text,text_rect)                                # 텍스트를 지정 위치에 블럭전송
            
            elif loc == 'center':
                text_rect = self.text.get_rect()
                text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)      # 위치 중간
                screen.blit(self.text,text_rect)
            
            elif loc == 'bottom center':
                text_rect = self.text.get_rect()
                text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT*3 // 4)    # 위치 아래
                screen.blit(self.text,text_rect)
            
            elif loc == 'bottom left':
                text_rect = self.text.get_rect()
                text_rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT*3 // 4)
                screen.blit(self.text,text_rect)
            
            elif loc == 'bottom right':
                text_rect = self.text.get_rect()
                text_rect.center = (SCREEN_WIDTH * 3 // 4, SCREEN_HEIGHT*3 // 4)
                screen.blit(self.text,text_rect)
            
            elif type(loc) == tuple: # User input of location 튜플이면 그 값을 위치로 받음. ex. (5,10)
                text_rect = self.text.get_rect()
                text_rect.center = loc
                screen.blit(self.text,text_rect)        
        
        else:
            if type(loc) == tuple: # User input of location
                screen.blit(self.text,loc)

class PLAYER():
    def __init__(self):
        self.deck_list = []         # 덱 리스트
        self.closed_deck = []
        self.opened_deck = []       # 오픈덱 리스트
    
    def draw_card(self,x,y):
        for i, card in enumerate(self.deck_list):
            card.draw_img(loc=(x + i*CARD_WIDTH,y)) # 같은 행에 카드 폭만큼 다른 열로 이어 붙임.
    
    def tile_arrange(self):
        deck = self.deck_list                   # 임시 리스트 생성.
        for q in range(len(deck)):              # 총 길이만큼 교환을 반복.
            for k in range(0,len(deck)-1):      # 모든 원소에 대해
                
                if sum(deck[k].get_num())/len(deck[k].get_num()) < sum(deck[k+1].get_num())/len(deck[k+1].get_num()): # 1) 평균 비교: 앞에놈이 작으면 놔둠.
                    pass
                
                elif sum(deck[k].get_num())/len(deck[k].get_num()) == sum(deck[k+1].get_num())/len(deck[k+1].get_num()): # 2) 평균이 같다면
                    if deck[k].get_num()[0] < deck[k+1].get_num()[0]:    # 2) spooky 값 비교. 앞에 놈이 작으면 놔둠
                        pass
                
                    elif deck[k].get_num()[0] == deck[k+1].get_num()[0]:    # 2) spooky 값도 같다면 색상 비교
                        if deck[k].get_color() > deck[k+1].get_color():     # 흰색이 뒤로 오면
                            deck[k+1],deck[k] = deck[k],deck[k+1]           # 검정색이 먼저오게 바꿈.
                            self.deck_list = deck  
                    
                    else:                                       # 2) spooky 앞에 놈이 크면 자리 바꿈.
                        deck[k+1],deck[k] = deck[k],deck[k+1]
                        self.deck_list = deck  
                
                else:                                       # 1) 평균값이 앞에 놈이 크면 타일 바꿈
                    deck[k+1],deck[k] = deck[k],deck[k+1] 
                    self.deck_list = deck                   # 저장

class CARD():
    global RT
    def __init__(self,color,num,prob,loop):   # 알고리즘 업데이트; num = [숫자,숫자,확률,확률] : 한 원소에 4개 값 List.
        # Set card & font color
        if color == 1: # Black
            self.card_color = BLACK
            self.font_color = WHITE
        else:
            self.card_color = GRAY
            self.font_color = BLACK
        
        self.color = color
        self.card_num = num
        self.card_probability = prob
        self.card_loop = loop
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

    def get_loop(self):
        return self.card_loop

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
            global RT # class CARD
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
                #collapse_loop(self)

            else:
                label1.config(text="추측한 "+str(PGN)+"숫자가 타일에 존재 하지 않습니다..")
                label2.config(text="유추에 실패 하여 이번 턴에 휙득한 타일을 붕괴 후, 공개합니다.")
                
                NTC = RT.get_color() #
                NTN = sf_p(RT.get_num(), RT.get_pro()) #
                
                label3 = Label(ct_tk, text="붕괴된 숫자 :"+str(NTN))
                label3.pack()

                NT = CARD(NTC, NTN, None, RT.get_loop())
                p[turn].deck_list.append(NT)
                del p[turn].deck_list[p[turn].deck_list.index(RT)]
                #
                ct_tk.after(1500, ctd)
                collapse_loop(RT)


        def ctd():
            ct_tk.destroy()

        entry=Entry(ct_tk, bd = 20)
        entry.bind("<Return>", ctcalc)
        entry.pack(pady = 50)

        label1.pack()
        label2.pack()

        ct_tk.mainloop()

class BUTTON():
    def __init__(self, msg, inactive_color=GRAY, active_color=GRAY_2,\
        font_color=BLACK, font="consolas", font_size=20, action=None):
        self.msg = msg
        self.ic = inactive_color
        self.ac = active_color
        self.f = font
        self.fc = font_color
        self.fs = font_size
        self.action = action
        self.active = active_color
        self.inactive = inactive_color

    def _draw_(self, loc=(0,0),loc_center=True, size=(60,40),action=None): # 각각 self, 위치, 버튼 크기, 실행함수

        # 텍스트로 위치 지정, 텍스트 아니면 직접 값으로 위치 지정
        if loc_center == True:
            if loc == 'top center':
                loc = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
            elif loc == 'center':
                loc = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            elif loc == 'bottom center':
                loc = (SCREEN_WIDTH // 2, SCREEN_HEIGHT*3 // 4)
            elif loc == 'bottom left':
                loc = (SCREEN_WIDTH // 4, SCREEN_HEIGHT*3 // 4)
            elif loc == 'bottom right':
                loc = (SCREEN_WIDTH * 3 // 4, SCREEN_HEIGHT*3 // 4)
        else:
            if type(loc) == tuple: # User input of location
                return loc
        
        x,y = loc
        w,h = size
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x-w/2 < mouse_pos[0] < x+w/2 and y-h/2 < mouse_pos[1] < y+h/2:
            pygame.draw.rect(screen,self.active,(x-w/2,y-h/2,w,h))
            
            if click[0] == 1:
                if action == None:
                    pass
                else: #print("클릭됨") # 확인용
                    #button
                    action()
        
        else:
            pygame.draw.rect(screen,self.inactive,(x-w/2,y-h/2,w,h))
        
        text = PRINTTEXT(self.msg, self.fs, font=self.f, color=self.fc, \
                         antialias=True, background=None)
        text._blit_(loc=(x,y))

def make_spooky(x): # 알고리즘 에러 정리 안 됨!!) 확률이 정렬에 따라 변하지 않음.
    global max_card_num # 패의 최대 숫자 전역변수
    min_loop_num = 2 # 최소 루프 개수
    cut_num = list(range(0,math.ceil((max_card_num+1)/min_loop_num)-2)) # math.ceil함수는 숫자 올림
    cut = []                     # cut1을 보관하는 장소
    card_list = list(range(0,max_card_num+1)) # 0~5 총 6개
    random.shuffle(card_list) # 섞는다 (shuffle 함수 기능)

    while 1:  # 얽힐 숫자들을 정하는 코드
        cut1 = 3+random.choice(cut_num) # cut_num의 임의 원소 선택, 루프 안에 들어가는 숫자의 개수, 3+가 있는 이유는 최소 루프 안에 들어있는 카드 숫자가 3이상이어야 하기 때문에. cut_num에서 숫자를 가져오는 이유는 루프 안에 있는 숫자의 개수를 다양화하기 위해 가져옴.
        cut.append(cut1) # 3 아님 4 추가

        if sum(cut) == max_card_num + 1:         # 총 얽힘수가 총 카드수랑 같으면 멈춤
            break

        elif sum(cut) > max_card_num + 1:            # cut수가 총 카드수보다 크면 마지막 cut1을 cut에서 뺀 후 뺀 것을 cut2라고 지정
            cut2 = cut.pop()

            if max_card_num + 1 - sum(cut) < 3:         # 남아 있는 수가 최소 얽힘수(3)보다 작다면 이전에 있던 cut1의 숫자를 늘려서 루프에 포함시킨다.
                cut[len(cut)-1] += max_card_num + 1 - sum(cut) 
                break
            else:                                       # 반대로 남아 있는 카드 수가 최소 얽힘수(3)보다 크거나 같으면 이전에 없앴던 cut1을 줄여서 남은 카드 수만큼 맞춘 다음, 다시 cut에 집어넣는다.          
                cut2 = max_card_num + 1 - sum(cut)   
                cut.append(cut2)
                break

    card_num = list(numpy.zeros(len(cut)))       # 루프 수만큼 방을 생성
    cut.append(0)
    add_card_s = 0
    add_card_f = cut[0]

    for i in range(0,len(cut)-1):          # 얽혀 있는 카드들끼리 한 방을 쓰도록 배정
        card_num[i] = []

        for k in range(add_card_s,add_card_f): 
            card_num[i].append(card_list[k])
        add_card_s += cut[i]
        add_card_f += cut[i+1]

    for i in range(0,len(card_num)):                # 각 방에 배정받은 숫자를 짝지어 spooky 카드를 만들도록 함
        for k in range(0,len(card_num[i])):   
            if k == 0:
                spooky_card_num = [card_num[i][k-1],card_num[i][k]] 
                alpha = max(spooky_card_num)
                spooky_card_num.append(int((spooky_card_num[0]+alpha/2)/(spooky_card_num[0]+spooky_card_num[1]+alpha)*100))
                beta = 100 - int((spooky_card_num[0]+alpha/2)/(spooky_card_num[0]+spooky_card_num[1]+alpha)*100)
                spooky_card_num.append(beta)
                spooky_card_num.append(i)
                x.append(spooky_card_num)
            else:
                gama = int(x[len(x)-1][3]+random.random()*20-10)
                spooky_card_num = [card_num[i][k-1],card_num[i][k],gama,100-gama,i]
                x.append(spooky_card_num)
    cut_list.append(cut)
    print(cut_list)

    return x      

def spooky_arrange(t):
    l = t
    for k in range(0,len(l)): 
        if l[k][1][0] < l[k][1][1]: # 두 spooky 수 고려 작으면 놔둠
            pass
        else:   #다르면 교환 후 저장
            l[k][1][0], l[k][1][1] = l[k][1][1], l[k][1][0]
            t = l

def all_arrange(players):
    for p in players:
        p.tile_arrange()

def f_option_room(): # 옵션 설정 방
    screen.fill([207, 216, 220])
    dp = PRINTTEXT("option testroom", size = 50)
    shb1 = BUTTON("button test")
    shb2 = BUTTON("Level Setting")
    shb3 = BUTTON("theory test")
    shbb = BUTTON("back test(main 이동 필요)")

    play = False
    while not play:
        for event in pygame.event.get():        # 기본 event loop
            if event.type == pygame.QUIT:       # pygame 종료
                pygame.quit()
                quit()

        shb1._draw_(loc = (100,300), size = (150,30), action=acb1)
        shb2._draw_(loc = (400,300), size = (150,30), action=acb2)
        shb3._draw_(loc = (700,300), size = (150,30), action=acb3)
        shbb._draw_(loc = (800,550), size = (150,30))
        # text positions
        dp._blit_(loc='top center')

        pygame.display.update()

def f_pn():
    global plabel, num_players
    player_num_max = 4  #게임 가능 플레이어 수 제한

    pn_tk=Tk()
    pn_tk.title("플레이어 수 입력")
    pn_tk.geometry("480x300+100+100")
    pn_tk.resizable(False, False)       # 창 크기 조절 가능 여부 거부
    plabel = Label(pn_tk, text="위의 창에 플레이어 숫자를 입력하세요.\n플레이 최소 인원은 2명이고 최대 인원은 "+str(player_num_max)+"명 입니다.")
    
    def pcalc(event):
        global num_players
        pn = int(entry.get())
        if pn > player_num_max:
            plabel.config(text="플레이어 수가 너무 많습니다. 다시 입력해주세요.")
        elif pn < 2:
            plabel.config(text="플레이어 수가 너무 적습니다. 다시 입력해주세요.")
        elif pn >=2 and pn <= player_num_max:
            plabel.config(text="플레이어 수가 "+str(eval(entry.get()))+"명으로 결정되었습니다.")
            num_players = pn
            
            pn_tk.after(1000, pnd)          # 1000ms 이후 pnd 함수 연결

    def pnd():              # tk 파괴. 위 elif에 바로 연결시 라벨 변경 안멱혀서 따로 뗌
        pn_tk.destroy()

    entry=Entry(pn_tk, bd = 20)      # 기입창, 크기 기본 위아래폭의 30배
    entry.bind("<Return>", pcalc)      # 리턴값 calc 함수에 사용
    entry.pack(pady = 50)             # 위아래 간격 50

    plabel.pack()

    pn_tk.mainloop()
    return num_players

def f_tn(num_players):
    global tlabel, stn, fcn, max_card_num

    fcn=(max_card_num+1)*2              # full card number
    tn_tk=Tk()
    tn_tk.title("스타팅 타일 수 입력")
    tn_tk.geometry("480x300+100+100")
    tn_tk.resizable(False, False)       # 창 크기 조절 가능 여부 거부
    tlabel = Label(tn_tk, text="시작시 가져갈 초기 타일 수를 결정해 주세요.")
    
    def tcalc(event):
        global num_players, stn
        stn = int(entry.get())
        if stn > fcn/num_players:
            tlabel.config(text="패를 나누기 위한 전체 타일 수가 부족합니다. 작은 수로 다시 입력해주세요.")
        elif stn < 2:
            tlabel.config(text="타일 수가 너무 적습니다. 다시 입력해주세요.")
        elif stn >= 2 and stn <= fcn/num_players:
            tlabel.config(text="플레이어가 받는 타일 수가 "+str(stn)+"개로 결정되었습니다.")

            tn_tk.after(1000, tnd)          # 1000ms 이후 pnd 함수 연결

    def tnd():              # tk 파괴. 위 elif에 바로 연결시 라벨 변경 안멱혀서 따로 뗌
        tn_tk.destroy()

    entry=Entry(tn_tk, bd = 20)      # 기입창, 크기 기본 위아래폭의 30배
    entry.bind("<Return>", tcalc)      # 리턴값 calc 함수에 사용
    entry.pack(pady = 50)             # 위아래 간격 50

    tlabel.pack()

    tn_tk.mainloop()
    return stn

def play_music():
    
    main_music = "White River - Aakash Gandhi.wav"

    pygame.mixer.init()
    pygame.mixer.music.load(main_music)
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1) # 무한재생.

def f_draw_card(p, turn, Ttext):
    T = list(range(turn,turn+num_players))
    p[T[0]].draw_card(SCREEN_WIDTH//2-len(p[T[0]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT*3/4)
    Ttext[0]._blit_(loc=(SCREEN_WIDTH//2-len(p[T[0]].deck_list)/2*CARD_WIDTH-50, SCREEN_HEIGHT*3/4),loc_center=False)

    for i in range(num_players):
        if T[i] >= num_players:
            T[i] = T[i]-num_players
    
    if num_players == 2:
        p[T[1]].draw_card(SCREEN_WIDTH//2-len(p[T[1]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT/4)
        Ttext[1]._blit_(loc=(SCREEN_WIDTH//2-len(p[T[1]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT/4-15),loc_center=False)

    if num_players == 3:
        p[T[1]].draw_card(CARD_WIDTH/2, SCREEN_HEIGHT/4)
        Ttext[1]._blit_(loc=(CARD_WIDTH/2, SCREEN_HEIGHT/4-15),loc_center=False)
        p[T[2]].draw_card(SCREEN_WIDTH-CARD_WIDTH*(0.5+len(p[T[2]].deck_list)), SCREEN_HEIGHT/4)
        Ttext[2]._blit_(loc=(SCREEN_WIDTH-CARD_WIDTH*(0.5+len(p[T[2]].deck_list)), SCREEN_HEIGHT/4-15),loc_center=False)
            
    if num_players == 4:
        p[T[1]].draw_card(CARD_WIDTH/2, SCREEN_HEIGHT/4+CARD_WIDTH*1.6+20)
        Ttext[1]._blit_(loc=(CARD_WIDTH/2, SCREEN_HEIGHT/4+CARD_WIDTH*1.6+20-15),loc_center=False)
        p[T[2]].draw_card(SCREEN_WIDTH//2-len(p[T[2]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT/4)
        Ttext[2]._blit_(loc=(SCREEN_WIDTH//2-len(p[T[2]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT/4-15),loc_center=False)    
        p[T[3]].draw_card(SCREEN_WIDTH-CARD_WIDTH*(0.5+len(p[T[3]].deck_list)), SCREEN_HEIGHT/4+CARD_WIDTH*1.6+20)
        Ttext[3]._blit_(loc=(SCREEN_WIDTH-CARD_WIDTH*(0.5+len(p[T[3]].deck_list)), SCREEN_HEIGHT/4+CARD_WIDTH*1.6+20-15),loc_center=False)

def collapse_loop(x):   # 변수 x는 방금 붕괴된 카드를 나타냄
    loop_num=[]
    if x.card_color == BLACK:    #색깔별로 인덱스 지정(balck = 0/white = 1)
        idx = 0
    elif x.card_color == WHITE:
        idx = 1
    
    loop_idx = x.get_loop()
    

    while len(loop_num) < cut_list[idx][loop_idx]-1:
        for player in p:
            for card in player.deck_list: # 모든 플레이어의 모든 카드에 대해

                if card.card_loop == x.card_loop: # x와 카드 루프가 같고
                    if x.card_num in card.card_num: # x의 숫자가 있으면
                        loop_num.append(x.card_num)
                        del card.card_num[index(x.card_num)] # 다른 숫자로 붕괴
                    
                    for num in loop_num:
                        if num in card.card_num:
                            loop_num.append(num)
                            del card.card_num[index(num)]

"""
    ====================<<<     SH-TEST    >>>=================
"""

def acb1():
    print("kkkkkkkkkkkkkkkkkkkkk")
    pass

def acb2():
    window=Tk()
    window.title("입력 테스트")
    window.geometry("480x300+100+100")
    window.resizable(False, False)                  # 창 크기 조절 가능 여부 거부
    def flash():
        checkbutton1.flash()

    CheckVariety_1=IntVar()
    CheckVariety_2=IntVar()

    checkbutton1=Checkbutton(window, text="O", variable=CheckVariety_1)
    checkbutton2=Checkbutton(window, text="△", variable=CheckVariety_2)
    checkbutton3=Checkbutton(window, text="X", variable=CheckVariety_2, command=flash)

    checkbutton1.pack()
    checkbutton2.pack()
    checkbutton3.pack()

    window.mainloop()

def acb3():
    global page
    
    acb3 = Tk()
    acb3.title("이론 설명창 테스트")
    acb3.geometry("600x300+100+100")

    page=0
    mpage = 3
    #image=PhotoImage(file="a.png") 
    #label = Label(acb3, image=image)         # 라벨 등록

    label1 = Label(acb3, text="intro")
    label2 = Label(acb3, text="~")
    label1.pack()
    label2.pack()

    Tbox = ["superposition:","entanglement:","collapse:"]
    Sbox = ["the ability of quantum objects to be in two places at once.",
            "the phenomenon where distant parts of a quantum system display correlations\nthat cannot be explained by either timelike causality or common cause.",
            "the phenomenon where the quantum states of a system are reduced to classical states.\nCollapses occur when a measurement happens,\nbut the mathematics of the current formulation of quantum mechanics is silent on the measurement process.\nMany of the interpretations of quantum mechanics derive from different efforts to deal with the measurement problem."]

    def pageUP():
        global page
        page +=1
        if page == mpage:
            label1.config(text=str(Tbox[page-1]))
            label2.config(text=str(Sbox[page-1]))

            buttonP = Button(acb3, overrelief="solid", width=15, command=pageDOWN, repeatdelay=1000, repeatinterval=100)
            buttonP.pack(side = LEFT, padx = 50)

        else:
            label1.config(text=str(Tbox[page-1]))
            label2.config(text=str(Sbox[page-1]))

            buttonP = Button(acb3, overrelief="solid", width=15, command=pageDOWN, repeatdelay=1000, repeatinterval=100)
            buttonP.pack(side = LEFT, padx = 50)
            buttonN = Button(acb3, overrelief="solid", width=15, command=pageUP, repeatdelay=1000, repeatinterval=100)
            buttonN.pack(side = RIGHT, padx = 50)

    def pageDOWN():
        global page
        page -=1

        label1.config(text=str(Tbox[page]))
        label2.config(text=str(Sbox[page]))

        buttonN = Button(acb3, overrelief="solid", width=15, command=pageUP, repeatdelay=1000, repeatinterval=100)
        buttonN.pack(side = RIGHT, padx = 50)

    buttonN = Button(acb3, overrelief="solid", width=15, command=pageUP, repeatdelay=1000, repeatinterval=100)
    buttonN.pack(side = RIGHT, padx = 50)
    acb3.mainloop()

def button_sound():
    
    b_s = "18V Cordless Drill Switch.wav"

    pygame.mixer.init()
    pygame.mixer.music.load(b_s)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(1)

"""
    ====================<<<     Main    >>>====================
"""

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

    option = BUTTON("Option test")

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
        option._draw_(loc = (800,SCREEN_HEIGHT*3 // 8), size = (180,30), action=f_option_room)
        
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
    
    #play_music()
    
    f_ftile_color_arrnage(tii)

    select_card = PRINTTEXT("Select card", 20)      # msg, font 크기
    button_take = BUTTON("take a tile")             # button sample
    button_turn = BUTTON("Next")
    button_exit = BUTTON("Exit",active_color=RED)

    YATT = 0    # You already took the tile. [먹기전: 0, 먹음: 1]
    

    def next_turn(): # 메인 루프 밖으로 절대 빼지 마시오.
        global turn, pl_turn, YATT
        turn += 1
        YATT = 0
        time.sleep(1.6)   # 임시 1.6초 딜레이
        win = 0
        if turn == num_players:
            turn = 0
            
    def f_take_tile(): # 메인 루프 밖으로 절대 빼지 마시오. + 함수 위치 고정.
        global fti_b, fti_w, YATT, RT
        wtt = Tk()                             # 윈도우 창을 생성
        wtt.title("타일 가져오기")              # 타이틀
        wtt.geometry("480x300+100+100")        # "너비x높이+x좌표+y좌표"

        label1 = Label(wtt, text="1차 완성")    # 라벨 등록
        label1.pack(pady=10)
        label2 = Label(wtt, text="가져올 타일을 선택하세요.")   # 라벨 등록
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
    global p, tii, max_card_num
    
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

    for i in ti:
        print(i)

    random.shuffle(ti)                  # 모든 타일 섞음
    spooky_arrange(ti)                  # util 참고.
    

    tii = [CARD(ti[i][0],ti[i][1][0:2],\
        ti[i][1][2:4],ti[i][1][4]) for i in range(len(ti))] # 생성된 카드를 클래스로 복제

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