#===========<서버용 시작>===========
import pygame
from network import Network
import pickle
#===========<서버용 끝>=============

#===========<main용 시작>===========
from tkinter import * 
from tkinter import messagebox
from tkinter.ttk import Notebook
from PIL import ImageTk, Image
#import pygame # 중복
import math
import random
import numpy
import time
import platform # OS Environment module
#===========<main용 끝>=============

'''
=====================================<< main 시작>>================================================
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

# Music
main_music = "White River - Aakash Gandhi.wav"
win_music = "Trimmed & Taught - Dan Lebowitz.wav"

# Object size
SCREEN_WIDTH  = 1100
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Quantum Coda")  # 타일틀바에 텍스트 출력.

CARD_WIDTH = 60
CARD_SIZE = (CARD_WIDTH, 1.6*CARD_WIDTH)
Notice = " "        # Notice 첫 값.

max_card_num = 10   # 13까지 가능하나 10 완성 전까지 고정할 것. make_spooky 함수 안으로 넣지 말 것. 
cut_list=[]         # 각 loop당 카드의 갯수
pln=0               # 아이템 쓸 플레이어
clicked = False

class PRINTTEXT():
    def __init__(self, msg, size, font=None, bold=False, color=BLACK, antialias=True, background=None):
        if font == None:                # OS별 폰트 문제 체크
            if platform.system() == 'Windows':
                font = 'calibri'
            elif platform.system() == 'Darwin':
                font = 'applesdgothicneo'
            elif platform.system() == 'Linux':
                font = 'notosanscjkkr'
            else:
                font = 'nanumgothic'
    
        self.msg = msg                  # 메세지
        self.font = font                # font 지정 (기본 conslas)
        self.size = size                # size 지정
        self.bold = bold                # bold 지정 (기본 True)
        self.antialias = antialias      # AA 지정 (기본 False)
        self.color = color              # 색상 지정 (기본 검정)
        self.background = background    # 바탕 지정 (기본 없음)
        texts = pygame.font.SysFont(self.font, self.size, self.bold)   # texts는 지정한 폰트와 사이즈 사용
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
        self.deck_list = []     # 덱 리스트
        self.point = 0
        self.num_list = []
        self.p_num=0

    def get_point(self):
        return self.point
    
    def put_point(self, x):
        self.point = self.point + x 

    def draw_card(self,x,y):
        for i, card in enumerate(self.deck_list):
            card.draw_img(loc=(x + i*CARD_WIDTH,y)) # 같은 행에 카드 폭만큼 다른 열로 이어 붙임.\

    def make_numlist(self):
        self.num_list = [card.card_num for card in self.deck_list]
        #print(self.num_list)
    
    def tile_arrange(self):
        deck = self.deck_list                   # 임시 리스트 생성.
        for q in range(len(deck)):              # 총 길이만큼 교환을 반복.
            for k in range(0,len(deck)-1):      # 모든 원소에 대해
                
                if sum(deck[k].get_num())/len(deck[k].get_num()) < sum(deck[k+1].get_num())/len(deck[k+1].get_num()): # 1) 평균 비교: 앞에놈이 작으면 놔둠.
                    pass
                
                elif sum(deck[k].get_num())/len(deck[k].get_num()) == sum(deck[k+1].get_num())/len(deck[k+1].get_num()): # 2) 평균이 같다면
                    if deck[k].get_num()[0] < deck[k+1].get_num()[0]:    # 2) spooky 값 비교. 앞에 놈이 작으면 놔둠 (붕괴된 수랑 비교시 붕괴된 수가 항상 가장 오른쪽.)
                        pass                                             
                
                    elif deck[k].get_num()[0] == deck[k+1].get_num()[0]:    # 2) spooky 값도 같다면 색상 비교
                        if deck[k].get_color() < deck[k+1].get_color() and states[0] == True :  # 하양색이 앞에 오면
                            deck[k+1],deck[k] = deck[k],deck[k+1]                               # 검정색이 먼저 앞에 오게 바꿈.
                            self.deck_list = deck  
                    
                    else:                                       # 2) spooky 앞에 놈이 크면 자리 바꿈.
                        deck[k+1],deck[k] = deck[k],deck[k+1]
                        self.deck_list = deck  
                
                else:                                       # 1) 평균값이 앞에 놈이 크면 타일 바꿈
                    deck[k+1],deck[k] = deck[k],deck[k+1] 
                    self.deck_list = deck                   # 저장

class CARD():
    global RT, YATT, Notice
    def __init__(self,color,num,prob,loop):
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
        self.opened = False
        self.number = PRINTTEXT("%s" % self.card_num, 18, color=self.font_color)
        self.probability = PRINTTEXT("%s" % self.card_probability, 15, color=self.font_color)
        
    def is_opened(self):
        self.opened = True
    
    def get_opened(self):
        return self.opened
    
    def get_color(self):
        return self.color

    def get_num(self):
        return self.card_num

    def get_pro(self):
        return self.card_probability

    def get_loop(self):
        return self.card_loop

    def draw_img(self, loc=(0,0), action=True):
        x, y = loc[0:2]
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()        
        
        pygame.draw.rect(screen, self.card_color, [x,y,self.width,self.height])
        pygame.draw.rect(screen, WHITE, [x,y,self.width,self.height],1)
        
        # 마우스 올렸을때 테두리 및 클릭 함수.
        if x < mouse_pos[0] < x + self.width and \
            y < mouse_pos[1] < y + self.height:
            pygame.draw.rect(screen, RED, [x,y,self.width,self.height],1)
            
            if click[0] == 1:
                if YATT != 1: # 타일 안먹으면 클릭 안됨. 아래 두 경우 제외.
                    if YATT == 0 and len(fti_b) == 0 and len(fti_w) == 0: # 타일이 없어 못 먹은 경우 추측 가능.
                        self.f_click_tile()
                    elif YATT == 3:   # 추측 성공시 추가 추측 가능.
                        self.f_click_tile()
                    pass
                elif YATT == 1: # 타일 먹은경우 클릭 허용.
                    self.f_click_tile()

        if self in p[turn].deck_list:   # 내 덱의 경우. 숫자 확률 표기.
            self.number._blit_(loc=(x + self.width/2, y + self.height/2))
            if states[1] == False:
                self.probability._blit_(loc=(x + self.width/2, y + self.height*3/4))

        if self.opened == True:     # 오픈된 타일의 경우.
            self.number._blit_(loc=(x + self.width/2, y + self.height/2))           # 숫자 표기.
            self.probability = PRINTTEXT("Opened", 12, color=self.font_color)       # 확률 텍스트 변경 후, 표기.
            self.probability._blit_(loc=(x + self.width/2, y + self.height*3/4))

        if len(self.get_num()) == 2 and states[1] == True:                          # 확률 보기 사용 on/ 시 상대 확률 표기.
            self.probability._blit_(loc=(x + self.width/2, y + self.height*3/4))
        
        if len(self.get_num()) ==1 and self.opened == False:
            self.probability = PRINTTEXT("Collapsed.", 12, color=self.font_color)   # 확률 텍스트 변경 후, 표기.
            self.probability._blit_(loc=(x + self.width/2, y + self.height*3/4))

    def f_click_tile(self):
        global RT, YATT, Notice

        # 자신의 패 선택 불가.
        if self in p[turn].deck_list:
            Notice = "You cannot select your tiles."
        
        # 타인의 패 선택시
        else:
            if self.opened == True: # 오픈된 타일 클릭 막음.
                Notice = "You cannot select the opened tile."
                pass
            elif self.opened == False:  # 아직 오픈 아닌 타일.
                Notice = " "
                t_num = self.card_num
                t_probability = self.card_probability

                ct_tk=Tk()
                ct_tk.title("Please enter the number you are guessing.")
                ct_tk.geometry("480x300+100+100")
                ct_tk.resizable(False, False)


                label1 = Label(ct_tk, text="Please enter the number you are guessing.")
                if len(self.card_num) == 2:
                    label2 = Label(ct_tk, text="probability: "+str(t_probability)+" (%).")
                elif len(self.card_num) == 1:
                    label2 = Label(ct_tk, text="probability: [100] (%).")

                def sf_p(number, probability):
                    x = random.randint(1,101)
                    if x <= probability[0]:
                        del number[number.index(number[1])]
                    else:
                        del number[number.index(number[0])]
                    return number
                    
                def ctcalc(event): 
                    global RT, YATT, Notice     # RT; type: CARD class
                    PGN = int(entry.get())      # The player's guess number.
                    
                    # 추측 수가 타일에 존재.
                    if PGN in self.card_num:

                        if len(self.card_num) == 2:     # 추측 타일 상태가 붕괴되지 않음.
                            self.card_num = sf_p(self.card_num, self.card_probability)
                            self.number = PRINTTEXT("%s" % self.card_num, 18, color=self.font_color)
                        
                            label1.config(text="The guessed number "+str(PGN)+" exists on the tile!\n추측한 숫자 "+str(PGN)+"가 타일에 존재합니다!")
                        
                            if PGN == self.card_num[0]: # 추측 성공 (self.card_num type: list) 
                                YATT = 3
                                self.is_opened()
                                p[turn].put_point(200)
                                label2.config(text="The tile collapsed to the guessed number.\nContinuous guessing is possible.\n추측한 숫자로 타일이 붕괴되었습니다.\n다른 타일의 숫자 추정이 가능합니다.")
                                Notice = "Continuous guessing is possible."
                                ct_tk.after(1700, ctd)
                                collapse_loop(self)
                            else:   # 붕괴는 하였으나 추측 실패. (오픈 상태 아님.)
                                YATT = 2
                                p[turn].put_point(100)
                                label2.config(text="The tile collapsed, but did not collapse \nwith the guessed number.\n타일은 붕괴되었지만, 추측한 숫자로 붕괴되지 않았습니다.")
                                ct_tk.after(1700, ctd)
                        
                        elif len(self.card_num) == 1: # 추측 타일 상태가 붕괴된 경우.
                            YATT = 3
                            self.is_opened()
                            p[turn].put_point(200)
                            label2.config(text="The tile collapsed to the guessed number.\nContinuous guessing is possible.\n추측한 숫자로 타일이 붕괴되었습니다.\n다른 타일의 숫자 추정이 가능합니다.")
                            Notice = "Continuous guessing is possible."
                            ct_tk.after(1200, ctd)

                    # 추측 수가 타일에 존재하지 않을 때.
                    else:
                        label1.config(text="The guessed number "+str(PGN)+" does not exist on the tile.\n추측한 숫자 "+str(PGN)+"는 타일에 존재하지 않습니다.")
                        if YATT == 0:   # 이번 턴에 먹은 타일이 없을 때.
                            YATT = 2
                            p[turn].put_point(20)
                            label2.config(text="There are no tiles added this turn,\nso the collapse and open process is skipped.\n이번 턴에 타일이 더 이상 없었으므로\n붕괴 및 카드 공개과정은 생략합니다.")
                            Notice = "Collapse and Open process is skipped."
                            ct_tk.after(1700, ctd)
                            pass

                        elif YATT == 1 or YATT == 3: # 이번 턴에 타일을 먹었을 때. (먹은 타일 붕괴)
                            YATT = 2
                            p[turn].put_point(20)
                            label2.config(text="The tile that you brought a new this turn\n now be collapsed and opened.\n이번 턴에서 새로 가져온 타일을 붕괴하고 공개합니다.")

                            if len(RT.get_num()) == 1:  # 붕괴된 타일을 먹었다면, 공개만.
                                Notice = "Failure to guess, opening an added tile."
                                del p[turn].deck_list[p[turn].deck_list.index(RT)]  # 오픈 안된 RT 제거
                                RT.is_opened()
                                p[turn].deck_list.append(RT)    # 오픈 후 다시 RT 추가.

                            elif len(RT.get_num()) == 2:    # 붕괴되지 않은 타일을 먹었다면, 붕괴후 공개.
                                Notice = "Failure to guess, opening after collapse of added tile."
                                NTC = RT.get_color()
                                NTN = sf_p(RT.get_num(), RT.get_pro())
                                label3 = Label(ct_tk, text="The collapsed number is "+str(NTN)+"\n붕괴된 숫자는 "+str(NTN)+"입니다.")
                                label3.pack()
                                NT = CARD(NTC, NTN, None,  RT.get_loop())
                                NT.is_opened()
                                p[turn].deck_list.append(NT)
                                del p[turn].deck_list[p[turn].deck_list.index(RT)]
                                collapse_loop(NT)
                                RT = NT
                            
                            ct_tk.after(2100, ctd)
                            
                def ctd():
                    ct_tk.destroy()

                entry=Entry(ct_tk, bd = 20)
                entry.bind("<Return>", ctcalc)
                entry.pack(pady = 40)

                label1.pack()
                label2.pack()

                ct_tk.mainloop()

class BUTTON():
    def __init__(self, msg, inactive_color=GRAY, active_color=GRAY_2,\
        font_color=BLACK, font=None, font_size=20, action=None):
        global pln

        if font == None:                # OS별 폰트 문제 체크
            if platform.system() == 'Windows':
                font = 'malgungothic'
            elif platform.system() == 'Darwin':
                font = 'applesdgothicneo'
            elif platform.system() == 'Linux':
                font = 'notosanscjkkr'
            else:
                font = 'consolas'
        
        self.msg = msg
        self.ic = inactive_color
        self.ac = active_color
        self.f = font
        self.fc = font_color
        self.fs = font_size
        self.action = action
        self.active = active_color
        self.inactive = inactive_color
        self.i = 0

    def get_i(self):
        pln = self.i
        print(pln)
        return self.i

    def _draw_(self, loc=(0,0),loc_center=True, size=(60,40),action=None): # 각각 self, 위치, 버튼 크기, 실행함수
        global asdf

        def button_sound():
            b_s = pygame.mixer.Sound("18V Cordless Drill Switch.wav")
            b_s.play()

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
                elif asdf == 0:
                    button_sound()
                    action()
                    asdf = 1
                    print(1)
            else:
                asdf = 0
        
        else:
            pygame.draw.rect(screen,self.inactive,(x-w/2,y-h/2,w,h))
            clicked == False
        text = PRINTTEXT(self.msg, self.fs, font=self.f, color=self.fc, \
                         antialias=True, background=None)
        text._blit_(loc=(x,y))

def make_spooky(x):
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

    for x in cut_list:
        for j in range(len(x)):
            if x[j] == 0:
                del x[j]

    print(cut_list)
    
    return x      

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
    for i,player in enumerate(p):
        player.p_num = i


    # PLAYER의 덱에 생성된 카드를 랜덤으로 추가
    for i in range(num_players):
        p[i].deck_list = []
        p[i].opened_deck = []
        for k in range(0,stn):
            qwer = random.choice(tii)
            p[i].deck_list.append(qwer)
            tii.pop(tii.index(qwer))

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

def f_ftile_color_arrnage(tii):           
    global fti_b, fti_w
    fti_b = []  # 검은색을 뽑을건지 흰색을 뽑을건지 플레이어가 정함
    fti_w = []  # 그래서 따로 검은색 흰색 그룹을 생성

    for i in range(len(tii)):  # 검은색 흰색 그룹에 색에 맞게 넣음
        if tii[i].get_color() == 1:
            fti_b.append(tii[i])
        elif tii[i].get_color() == 0:
            fti_w.append(tii[i])

def exit_window(): # Exit Warning window Tk.
    ex = Tk()
    ex.withdraw()

    ex.bell()
    msgbox = messagebox.askquestion("Warning", "Do you want to end this game? \n게임을 끝내실 건가요?",\
        icon='warning')
    
    if msgbox == 'yes':
        ex.destroy()
        quit()
    else:
        ex.destroy()

def tbu_window(): # To Be Updated window tk
    tbu = Tk()
    tbu.withdraw()

    msgbox = messagebox.showerror("To Be Updated", "Currently this feature is not available. To be updated.\n현재 이 기능은 사용할 수 없습니다. 업데이트 예정입니다.")

    if msgbox == 'ok':
        tbu.destroy()
    else:
        pass

def bati_window(): # Back to the Title window tk
    bati = Tk()
    bati.withdraw()

    msgbox = messagebox.askyesno("Back to Title", "Do you want to back to the title?\n타이틀로 돌아가시겠습니까?")

    if msgbox == True:
        pygame.mixer.music.stop()
        bati.destroy()
        game_intro()
    else:
        bati.destroy()

def theory_desc(): # 이론 Tk.
    window=Tk()
    window.title("Theory.")
    window.geometry("800x500+100+100")
    window.resizable(False, False)
    
    n_width = 720
    n_heigh = 480
    notebook=Notebook(window, width = n_width, height = n_heigh)
    notebook.pack()
    
    # Introduction
    frame1=Frame(window)
    notebook.add(frame1, text="Intro")

    A = open('Intro.txt', 'r', encoding='UTF8')
    Intro = A.read()
    
    msg1=Message(frame1, width = n_width, text=Intro)
    msg1.pack(side = "top", anchor = "w")

    # Description tab for superposition in English
    frame2=Frame(window)
    notebook.add(frame2, text="Superposition")

    B = open('superposition_en.txt', 'r', encoding='UTF8')
    sup_en = B.read()
    
    msg2=Message(frame2, width = n_width, text=sup_en)
    msg2.pack(side = "top", anchor = "w")
                   
    # Description tab for entanglement in English
    frame3=Frame(window)
    notebook.add(frame3, text="Entanglement")

    C = open('entanglement_en.txt', 'r', encoding='UTF8')
    ent_en = C.read()
    
    msg3 = Message(frame3, width = n_width, text=ent_en)
    msg3.pack(side = "top", anchor = "w")

    # Description tab for Observation & Collapse in English 
    frame4 = Frame(window)
    notebook.add(frame4, text="Measurement & Collapse")

    D = open('measurement_and_collapse_en.txt', 'r', encoding='UTF8')
    measncoll_en = D.read()
    
    msg4 = Message(frame4, width = n_width, text=measncoll_en)
    msg4.pack(side = "top", anchor = "w")

    # Description tab for superposition in Korean 
    frame5=Frame(window)
    notebook.add(frame5, text="중첩")

    B = open('superposition_ko.txt', 'r', encoding='UTF8')
    sup_ko = B.read()
    
    msg5=Message(frame5, width = n_width, text=sup_ko)
    msg5.pack(side = "top", anchor = "w")

    # Description tab for entanglement in Korean 
    frame6=Frame(window)
    notebook.add(frame6, text="얽힘")

    C = open('entanglement_ko.txt', 'r', encoding='UTF8')
    ent_ko = C.read()
    
    msg6 = Message(frame6, width = n_width, text=ent_ko)
    msg6.pack(side = "top", anchor = "w")

    # Description tab for Measurement & Collapse in Korean 
    frame7 = Frame(window)
    notebook.add(frame7, text="측정과 붕괴")

    D = open('measurement_and_collapse_ko.txt', 'r', encoding='UTF8')
    measncoll_ko = D.read()
    
    msg7 = Message(frame7, width = n_width, text=measncoll_ko)
    msg7.pack(side = "top", anchor = "w")

    # 4
    frame8 = Frame(window)
    notebook.add(frame8, text="이미지 크기조절 및 출력 테스트")

    image=Image.open("a.png")
    image = image.resize((n_width,n_heigh-20),Image.ANTIALIAS)
    r_img = ImageTk.PhotoImage(image)
    
    msg8=Label(frame8, width = n_width, image=r_img)
    msg8.pack(side = "top", anchor = "w")

    window.mainloop()

def f_pn(): # 플레이어 수를 입력 받는 Tk.
    global plabel, num_players
    player_num_max = 4  #게임 가능 플레이어 수 제한

    pn_tk=Tk()
    pn_tk.title("Please enter the number of players.")
    pn_tk.geometry("480x300+100+100")
    pn_tk.resizable(False, False)       # 창 크기 조절 가능 여부 거부
    dum = Label(pn_tk, text = "\n")
    dum.pack()
    plabel = Label(pn_tk, \
        text="Please enter the number of players in the space above.\nThe minimum playable number is 2. The maximum is 4.\n\n플레이어 숫자를 위의 칸에 입력해주세요.\n최소 플레이어 수는 2, 최대 플레이어 수는 4 입니다.")
    
    def pcalc(event):
        global num_players
        pn = int(entry.get())
        if pn > player_num_max:
            plabel.config(text="Too many players. Please enter again.\n\n너무 많은 플레이어 숫자를 입력했습니다. 다시 입력하세요.")
        elif pn < 2:
            plabel.config(text="Too few players. Please enter again.\n\n너무 적은 플레이어 숫자를 입력했습니다. 다시 입력하세요.")
        elif pn >=2 and pn <= player_num_max:
            plabel.config(text="The number of players was determined to be "+str(eval(entry.get()))+".\n\n플레이어 수가 "+str(eval(entry.get()))+"(으)로 결정 되었습니다.")
            num_players = pn
            pn_tk.after(1000, pnd)          # 1000ms 이후 pnd 함수 연결

    def pnd():              # tk 파괴. 위 elif에 바로 연결시 라벨 변경 안멱혀서 따로 뗌
        pn_tk.destroy()
        f_tn(num_players)

    entry=Entry(pn_tk, bd = 20)     # 기입창, 크기 기본 위아래폭의 30배
    entry.bind("<Return>", pcalc)   # 리턴값 calc 함수에 사용
    entry.pack(pady = 20)           # 위아래 간격 20

    plabel.pack()

    pn_tk.mainloop()
    
def f_tn(num_players):  # 초기 타일 수를 입력 받는 Tk.
    global tlabel, stn, fcn, max_card_num

    fcn=(max_card_num+1)*2              # full card number
    tn_tk=Tk()
    tn_tk.title("Enter the number of starting tiles.")
    tn_tk.geometry("480x300+100+100")
    tn_tk.resizable(False, False)       # 창 크기 조절 가능 여부 거부
    dum = Label(tn_tk, text = "\n")
    dum.pack()
    tlabel = Label(tn_tk, text="Please enter the number of tiles\nwhen players start the game.\n\n게임 시작할 때 받을 플레이어의 타일 수를 입력해주세요.")
    
    def tcalc(event):
        global num_players, stn
        stn = int(entry.get())
        if stn > fcn/num_players:
            tlabel.config(text="Total tiles are not sufficient to divide cards. Please enter a small number.\n\n전체 타일이 충분하지 않아 나눌 수 없습니다. 더 작은 수를 입력해주세요.")
        elif stn < 2:
            tlabel.config(text="Too few tiles. Please enter again.\n\n타일수가 너무 적습니다. 다시 입력하세요.")
        elif stn >= 2 and stn <= fcn/num_players:
            tlabel.config(text="The number of tiles per players was decided as "+str(stn)+".\n\n타일수가 "+str(stn)+"(으)로 결정 되었습니다.")
            
            tn_tk.after(1000, tnd)          # 1000ms 이후 pnd 함수 연결
            
    def tnd():              # tk 파괴. 위 elif에 바로 연결시 라벨 변경 안멱혀서 따로 뗌
        tn_tk.destroy()
        main_loop()

    entry=Entry(tn_tk, bd = 20)     # 기입창, 크기 기본 위아래폭의 30배
    entry.bind("<Return>", tcalc)   # 리턴값 calc 함수에 사용
    entry.pack(pady = 20)           # 위아래 간격 20

    tlabel.pack()

    tn_tk.mainloop()

def f_play_music(name, vol): # 음악 연속 재생 함수. (vol: 0 ~ 1)
    pygame.mixer.init()
    pygame.mixer.music.load(name)
    pygame.mixer.music.set_volume(vol)
    pygame.mixer.music.play(-1) # 무한재생.

def f_level_set(): # 난이도 설정 Tk.
    global states
    
    name_box = ["Use color alignment","Use probability view","Use items"]
    chk = [0,0,0] # Dummy list for name.
    
    def onPress(i):                       
        states[i] = not states[i]   
    root = Tk()
    root.title("Level Settings.")
    root.geometry("480x300+100+100")
    root.resizable(False, False)
    t = Label(text="Difficulty increases if you don't use the features. (Check =  Use)\n난이도는 아래의 기능들을 사용하지 않으면 올라갑니다.")
    t.pack(pady=10)
    a1 = Message(width = 480, text="# Color Alignment (색상 정렬) :")
    a1.pack(anchor = "w")
    a2 = Message(width = 480, justify= "left", text="If both tiles black and white have the same spooky numbers, always have black on the left. (ex. Wh[1, 4], Bl[1, 4] >> Bl[1, 4] , Wh[1, 4] )\n검정색과 흰색 두 타일이 같은 추정 숫자를 가지는 경우, 항상 검은색 타일이 왼쪽으로 정렬되도록 합니다.")
    a2.pack(anchor = "w")
    a3 = Message(width = 480, text="# Probability view (확률 보기) :")
    a3.pack(anchor = "w", pady=0)
    a4 = Message(width = 480, justify= "left", text="Watch the probability of tiles on your opponent.\n상대방이 소유한 타일의 확률을 봅니다.")
    a4.pack(anchor = "w", pady=0)
    a5 = Message(width = 480, text="# Items (아이템) :")
    a5.pack(anchor = "w", pady=0)
    a6 = Message(width = 480, justify= "left", text="Use an item that lowers the difficulty of the game.\n게임의 난이도를 낮추는 아이템을 사용합니다.")
    a6.pack(anchor = "w", pady=0)
    
    for i in range(3):
        chk[i] = Checkbutton(root, text=name_box[i], command=(lambda i=i: onPress(i)) )
        if states[i] == True:
            chk[i].select()
        chk[i].place(x=240)
    
    chk[0].place(y=56)
    chk[1].place(y=144)
    chk[2].place(y=209)

    root.mainloop()

def f_win_page(): # 승리 페이지.
    screen.fill([255, 249, 196])
    dp = PRINTTEXT("The result of the game.", size = 50)
    wpb1 = BUTTON("ReGame", inactive_color = WHITE, active_color=GRAY)
    wpb2 = BUTTON("home", inactive_color = WHITE, active_color=GRAY)
    wpb3 = BUTTON("Level Setting", inactive_color = WHITE, active_color=GRAY)
    f_play_music(win_music, 0.6)
    play = False
    while not play:
        for event in pygame.event.get():        # 기본 event loop
            if event.type == pygame.QUIT:       # pygame 종료
                pygame.quit()
                quit()

        wpb1._draw_(loc = (SCREEN_WIDTH*4/5,SCREEN_HEIGHT/4), size = (150,60), action=main_loop)
        wpb2._draw_(loc = (SCREEN_WIDTH*4/5,SCREEN_HEIGHT*2/4), size = (150,60), action=bati_window)
        wpb3._draw_(loc = (SCREEN_WIDTH*4/5,SCREEN_HEIGHT*3/4), size = (150,60), action=f_level_set)
        
        # text positions
        dp._blit_(loc= (SCREEN_WIDTH/10, SCREEN_HEIGHT/10), loc_center=False)

        # rank 
        def sf_calculate_rank(vector):
            a={}
            rank=1
            for num in sorted(vector):
                if num not in a:
                    a[num]=rank
                    rank=rank+1
            return[a[i] for i in vector]

        box , em = [], []
        for i in range(0,num_players):
            box.append(-p[i].get_point())
            em.append(i)
        
        cbox = sf_calculate_rank(box)

        for i in range(0,num_players):
            em[i] = PRINTTEXT("Player "+str(i+1)+":  >>> rank: "+str(cbox[i])+" [point: "+str(p[i].get_point())+"].", size = 26)
            em[i]._blit_(loc= (SCREEN_WIDTH/10+10, SCREEN_HEIGHT/4+i*54), loc_center=False)
        
        pygame.display.update()

def f_end_conditions(): # 승리 조건 함수.
    for i in range(0,num_players): # 모든 플레이어에 대해
        dummy = 0
        for k in range(0,len(p[i].deck_list)): 
            if p[i].deck_list[k].get_opened() == True:
                dummy += 1
            if dummy == len(p[i].deck_list): # 자신의 덱 카드가 모두 오픈이면 게임 끝냄.
                f_win_page()

def f_draw_card(p, turn, T, Ttext): # 플레이 인원 수에 따라 덱의 위치를 지정한 함수.
    p[T[0]].draw_card(SCREEN_WIDTH//2-len(p[T[0]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT*3/4)
    Ttext[0]._blit_(loc=(SCREEN_WIDTH//2-len(p[T[0]].deck_list)/2*CARD_WIDTH-54, SCREEN_HEIGHT*3/4),loc_center=True)

    if num_players == 2:
        p[T[1]].draw_card(SCREEN_WIDTH//2-len(p[T[1]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT/4)
        Ttext[1]._draw_(loc=(SCREEN_WIDTH//2-len(p[T[1]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT/4-15),size=(120,20),loc_center=True,action=Ttext[1].get_i)

    if num_players == 3:
        p[T[1]].draw_card(CARD_WIDTH/2, SCREEN_HEIGHT/4)
        Ttext[1]._draw_(loc=(CARD_WIDTH/2, SCREEN_HEIGHT/4-15),size=(120,20),loc_center=True,action=Ttext[1].get_i)
        p[T[2]].draw_card(SCREEN_WIDTH-CARD_WIDTH*(0.5+len(p[T[2]].deck_list)), SCREEN_HEIGHT/4)
        Ttext[2]._draw_(loc=(SCREEN_WIDTH-CARD_WIDTH*(0.5+len(p[T[2]].deck_list)), SCREEN_HEIGHT/4-15),size=(120,20),loc_center=True,action=Ttext[2].get_i)
            
    if num_players == 4:
        p[T[1]].draw_card(CARD_WIDTH/2, SCREEN_HEIGHT/4+CARD_WIDTH*1.6+20)
        Ttext[1]._draw_(loc=(CARD_WIDTH/2, SCREEN_HEIGHT/4+CARD_WIDTH*1.6+20-15),size=(120,20),loc_center=True,action=Ttext[1].get_i)
        p[T[2]].draw_card(SCREEN_WIDTH//2-len(p[T[2]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT/4)
        Ttext[2]._draw_(loc=(SCREEN_WIDTH//2-len(p[T[2]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT/4-15),size=(120,20),loc_center=True,action=Ttext[2].get_i)    
        p[T[3]].draw_card(SCREEN_WIDTH-CARD_WIDTH*(0.5+len(p[T[3]].deck_list)), SCREEN_HEIGHT/4+CARD_WIDTH*1.6+20)
        Ttext[3]._draw_(loc=(SCREEN_WIDTH-CARD_WIDTH*(0.5+len(p[T[3]].deck_list)), SCREEN_HEIGHT/4+CARD_WIDTH*1.6+20-15),size=(120,20),loc_center=True,action=Ttext[3].get_i)

def collapse_loop(x):   # 변수 x는 방금 붕괴된 카드(class)를 나타냄
    global fti_w, fti_b
    loop_num=x.card_num[0]      
    print("x[0]: ",x.card_num[0])   # loop_num을 방금 붕괴된 카드의 숫자로 받아옴

    for iter in range(10):  # 충분히 많이 반복
        for player in p:    # 모든 플레이어의
            for card in player.deck_list:      #모든 카드를 돌면서
                if (card.card_color == x.card_color) and (card.card_loop == x.card_loop): # 루프와 색상이 같은 경우에
                    # 카드가 loop_num을 가지고 있고, 카드 숫자가 두개면
                    if (loop_num in card.card_num) and (len(card.card_num) == 2):        
                        del card.card_num[card.card_num.index(loop_num)]    # loop_num과 다른 숫자로 붕괴
                        card.number = PRINTTEXT("%s" % card.card_num, 18, color=card.font_color)    # card_num 업데이트
                        loop_num = card.card_num[0]     # loop_num을 card_num으로 바꿈(루프내 다른 카드를 붕괴시킬 수 있도록)

        if x.card_color == BLACK:        
            for card_b in fti_b:
                if (card_b.card_loop == x.card_loop) and (loop_num in card_b.card_num) and (len(card_b.card_num) == 2):
                        del card_b.card_num[card_b.card_num.index(loop_num)]
                        card_b.number = PRINTTEXT("%s" % card_b.card_num, 18, color=card_b.font_color)
                        loop_num = card_b.card_num[0]

        else:                
            for card_w in fti_w:
                if (card_w.card_loop == x.card_loop) and (loop_num in card_w.card_num) and (len(card_w.card_num) == 2):
                        del card_w.card_num[card_w.card_num.index(loop_num)]
                        card_w.number = PRINTTEXT("%s" % card_w.card_num, 18, color=card_w.font_color)
                        loop_num = card_w.card_num[0]
#
class mButton:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False
        pygame.font.init()
#
def redrawWindow(win, game, p):
    win.fill((128,128,128))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Your Move", 1, (0, 255,255))
        win.blit(text, (80, 200))

        text = font.render("Opponents", 1, (0, 255, 255))
        win.blit(text, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothWent():
            text1 = font.render(move1, 1, (0,0,0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, 1, (0,0,0))
            elif game.p1Went:
                text1 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text1 = font.render("Waiting...", 1, (0, 0, 0))

            if game.p2Went and p == 1:
                text2 = font.render(move2, 1, (0,0,0))
            elif game.p2Went:
                text2 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", 1, (0, 0, 0))

        if p == 1:
            win.blit(text2, (100, 350))
            win.blit(text1, (400, 350))
        else:
            win.blit(text1, (100, 350))
            win.blit(text2, (400, 350))

        for btn in btns:
            btn.draw(win)

    pygame.display.flip()
#
def main(room):
    run = True
    clock = pygame.time.Clock()
    n = Network(room)
    player = int(n.getP())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            redrawWindow(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render("You Won!", 1, (255,0,0))
            elif game.winner() == -1:
                text = font.render("Tie Game!", 1, (255,0,0))
            else:
                text = font.render("You Lost...", 1, (255, 0, 0))

            win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)
                        else:
                            if not game.p2Went:
                                n.send(btn.text)

        redrawWindow(win, game, player)
#
def menu_screen(room):
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        win.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main(room)
#
def start(room):
    global width, height, win, btns, rn
    pygame.font.init()
    width = 700
    height = 700
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Client")
    btns = [mButton("Rock", 50, 500, (0,0,0)), mButton("Scissors", 250, 500, (255,0,0)), mButton("Paper", 450, 500, (0,255,0))]
    rn = room
    while True:
        menu_screen(rn)
#
def f_rn(): # 룸 넘버 입력 받는 tk 임시.
    rn_tk=Tk()
    rn_tk.title("test.")
    rn_tk.geometry("480x300+100+100")
    rn_tk.resizable(False, False)       # 창 크기 조절 가능 여부 거부
    dum = Label(rn_tk, text = "\n")
    dum.pack()
    label = Label(rn_tk, text="방 번호 1~3")
    label.pack()
    
    def bmain1():
        run = True
        rn_tk.destroy()
        start(1)
        '''
        커넥션 체킹 용인데 소켓을 두 번 전송해서 player 0로 접속하고 1로 접속하는 상황 발생함.
        n = Network(room=1)
        
        while run:
            clock.tick(60)
            try:
                game = n.send("get")
                print("Room 1 OK Chekced")
                rn_tk.destroy()
                start(1)
            except:
                run = False
                print("Couldn't get game")
                break
        '''

    def bmain2():
        run = True
        rn_tk.destroy()
        
    def bmain3():
        run = True
        rn_tk.destroy()

    r1 = Button(rn_tk, text="1", command = bmain1)
    r2 = Button(rn_tk, text="2", command = bmain2)
    r3 = Button(rn_tk, text="3", command = bmain3)               

    r1.pack()
    r2.pack()
    r3.pack()

    rn_tk.mainloop()
#                         
def game_intro():   # Game intro scene
    screen.fill(WHITE)
    intro = False   # while문 돌리기 위함

    title = PRINTTEXT("Quantum Coda", size = 50)    # Title Texts
    version = PRINTTEXT("v.0.11", size = 15)

    credits_title = PRINTTEXT("Credits", size = 30)
    credits_affilation = PRINTTEXT("Undergraduate Students, Department of Physics, Pukyong National University", size = 20)
    credits_name = PRINTTEXT("Jong hee Kim, Yong chul Lee, Yong Kwon, Se hyoung Jo, Ji won Choi", size = 20)

    # Button Texts
    gsettings_button = BUTTON("Game settings")
    title_exit_button = BUTTON("Exit",active_color=RED)
    splay_button = BUTTON("Single Player")
    mplay_button = BUTTON("Multi Player")
    how_button = BUTTON("How to Play?")

    while not intro:
        for event in pygame.event.get():        # 기본 event loop
            if event.type == pygame.QUIT:       # pygame 종료
                pygame.quit()
        
        # text _blit_ location
        title._blit_(loc= (SCREEN_WIDTH*1 // 2, SCREEN_HEIGHT*3 // 16))
        version._blit_(loc=(SCREEN_WIDTH-40, SCREEN_HEIGHT-20))
        credits_title._blit_(loc=(SCREEN_WIDTH*1 // 2, SCREEN_HEIGHT-100))
        credits_affilation._blit_(loc=(SCREEN_WIDTH*1 // 2, SCREEN_HEIGHT-70))
        credits_name._blit_(loc=(SCREEN_WIDTH*1 // 2, SCREEN_HEIGHT-40))
        
        # button _draw_ functions
        splay_button._draw_(loc = (SCREEN_WIDTH*4 // 10, SCREEN_HEIGHT*3 // 8), size = (160,60),action=f_pn)
        mplay_button._draw_(loc = (SCREEN_WIDTH*6 // 10, SCREEN_HEIGHT*3 // 8), size = (160,60),action=f_rn)
        how_button._draw_(loc = (SCREEN_WIDTH*4 // 10, SCREEN_HEIGHT*4 // 8), size = (160,60),action=how_to_play)
        gsettings_button._draw_(loc = (SCREEN_WIDTH*6 // 10,SCREEN_HEIGHT*4 // 8), size = (160,60), action=f_level_set)
        title_exit_button._draw_(loc = (SCREEN_WIDTH // 2, SCREEN_HEIGHT*5 // 8), size = (160,60),action=quit)

        pygame.display.update()
        clock.tick(15)

def how_to_play(): # scene for game description # 장면 테스트 중
    screen.fill(WHITE)
    play = False
        
    # dp: description

    dp_en1 = PRINTTEXT("Quantum Coda is a new game based on 'Coda' and the game included", size = 20)
    dp_en2 = PRINTTEXT("weird elements inspired on the phenomenon of Quantum Mechanics.", size = 20)
    dp_en3 = PRINTTEXT("If you need 'help' about this game, click the button on the rightside", size = 20)
    dp_en4 = PRINTTEXT("what you want to know.", size = 20)
    dp_en5 = PRINTTEXT("", size = 20)
    dp_en6 = PRINTTEXT("English and Korean are supported to understand our game.", size = 20)

    theory_button = BUTTON("Theory 이론")
    Rule_button = BUTTON("Rule 게임규칙")
    prac_button = BUTTON("Practice 연습게임")
    back_button = BUTTON("Back to Title")
    exit_button = BUTTON("Exit",active_color=RED)

    while not play:
        for event in pygame.event.get():        # 기본 event loop
            if event.type == pygame.QUIT:       # pygame 종료
                pygame.quit()

        # text positions
        dp_en = [dp_en1,dp_en2,dp_en3,dp_en4,dp_en5,dp_en6]
        for i in range (6):
            dp_en[i]._blit_(loc= (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 4 + 25*i))

        theory_button._draw_(loc = (SCREEN_WIDTH-200, SCREEN_HEIGHT // 4), size = (SCREEN_WIDTH // 4,100), action = theory_desc)
        Rule_button._draw_(loc = (SCREEN_WIDTH-200, SCREEN_HEIGHT*2 // 4), size = (SCREEN_WIDTH // 4,100), action = tbu_window)
        prac_button._draw_(loc = (SCREEN_WIDTH-200, SCREEN_HEIGHT*3 // 4), size = (SCREEN_WIDTH // 4,100), action = tbu_window)
        back_button._draw_(loc = (800,50), size = (130,30), action = game_intro)
        exit_button._draw_(loc = (SCREEN_WIDTH-100,50), size = (130,30), action = pygame.quit)

        pygame.display.flip()
        clock.tick(15)

def main_loop(): # Game main loop scene
    global num_players, stn, turn, YATT, RT
    turn , RT = 0, 0        # 첫값 0. 수정 금지.
    screen.fill(WHITE)
    done = False
    make_card(num_players, stn)
    f_play_music(main_music, 1)
    f_ftile_color_arrnage(tii)

    select_card = PRINTTEXT("Select card", 20)      # msg, font 크기
    button_take = BUTTON("Take a tile")             # button sample
    button_turn = BUTTON("Next")
    button_back = BUTTON("Back to Title")
    button_exit = BUTTON("Exit",active_color=RED)

    YATT = 0    # You already took the tile. [먹기전: 0, 먹음(추측전): 1, 추측실패: 2, 추측성공: 3]
    
    def next_turn(): # 메인 루프 밖으로 절대 빼지 마시오.
        global turn, pl_turn, YATT, Notice
        if YATT == 2 or YATT == 3: # 추측 이후 턴넘김 활성화
            Notice = " "
            turn += 1
            YATT = 0
            time.sleep(1.6)   # 임시 1.6초 딜레이
            if turn == num_players:
                turn = 0
        elif YATT == 0:
            Notice = "Take the tile first this turn."
            
        elif YATT == 1:
            Notice = "Guess the number of tiles on your opponent."
        
        for player in p:
            player.make_numlist()
 
    def f_take_tile(): # 메인 루프 밖으로 절대 빼지 마시오. + 함수 위치 고정.
        global fti_b, fti_w, YATT, RT, Notice
        Notice = " "
        wtt = Tk()                             # 윈도우 창을 생성
        wtt.title("Get Tiles.")                # 타이틀
        wtt.geometry("480x300+100+100")        # "너비x높이+x좌표+y좌표"

        label1 = Label(wtt, text="Take a new tile from the decks.\n새로운 타일을 덱에서 가져가세요.")    # 라벨 등록
        label1.pack(pady=10)
        label2 = Label(wtt, text="Choose the color of the tile to take.\n가져갈 타일의 색상을 선택하세요.")   # 라벨 등록
        label2.pack(pady=10)
        
        pixelVirtual = PhotoImage(width=1, height=1) # 기준 픽셀 추가

        def sf_bb():
            global fti_b, p, YATT, RT

            if len(fti_b) == 0:
                label2.config(text="There are no more tiles of this color.\n이 색상의 타일은 더 이상 없습니다.")
            else:
                RT = random.choice(fti_b)
                p[turn].deck_list.append(RT)
                fti_b.pop(fti_b.index(RT))
                YATT += 1
                wtt.after(1000, wttd)

        def sf_bw():
            global fti_w, p, YATT, RT
        
            if len(fti_w) == 0:
                label2.config(text="There are no more tiles of this color.\n이 색상의 타일은 더 이상 없습니다.")
            else:
                RT = random.choice(fti_w)
                p[turn].deck_list.append(RT)
                fti_w.pop(fti_w.index(RT))
                YATT += 1
                wtt.after(1000, wttd)
    
        bb = Button(wtt, text='Get Black\n'+'remaining tiles: '+str(len(fti_b)), command = sf_bb, fg = 'white', bg = "black",
                    image=pixelVirtual, width=100, height=160, compound="c")                # 크기 텍스트 기준이 아닌 기준 픽셀 기준, 텍스트는 중앙표기.
        bw = Button(wtt, text='Get White\n'+'remaining tiles: '+str(len(fti_w)), command = sf_bw, fg = 'black', bg = "ghost white",
                    image=pixelVirtual, width=100, height=160, compound="c")
        bb.pack(side = LEFT, padx = 50)
        bw.pack(side = RIGHT, padx = 50)

        def wttd():              # tk 파괴. 위 elif에 바로 연결시 라벨 변경 안멱혀서 따로 뗌
            wtt.destroy()

        if len(fti_b) == 0 and len(fti_w) == 0:
            label2.config(text="There are no more tiles.\n더 이상의 타일이 없습니다.")
            
            wtt.after(1000, wttd)
        
        if YATT != 0:
            label2.config(text="You have already taken a tile this turn.\n이번 차례에 이미 타일을 가져갔습니다.")
            bb.destroy()
            bw.destroy()
            wtt.after(1000, wttd)

        wtt.mainloop()


    for i,player in enumerate(p):
        print(i+1)
        print(player.num_list)

    #========== main loop 창 실행 ==========#
    while not done:
        for event in pygame.event.get():        # 닫기 전까지 계속 실행.
            if event.type == pygame.QUIT:       # 종료 if문
                exit_window()

        # 턴 관련
        pygame.draw.rect(screen, WHITE, [0,0,SCREEN_WIDTH,SCREEN_HEIGHT])          # 삭제금지.
        pl_turn = PRINTTEXT("Turn of player "+str(turn+1), 25)
        pl_turn._blit_(loc=(5,5),loc_center=False)  
        
        # 덱의 카드 정렬
        all_arrange(p)

        # 승리 조건
        f_end_conditions()
        
        # 공지
        Notice_box = PRINTTEXT(Notice, 20)
        Notice_box._blit_(loc=(SCREEN_WIDTH/2,50))
        
        # 덱 그리기(플러이어 텍스트 포함)
        T = list(range(turn,turn+num_players))
        for i in range(num_players):
            if T[i] >= num_players:
                T[i] = T[i]-num_players

        Ttext = list(range(num_players))
        Ttext[0] = PRINTTEXT(msg='Yours: ',size=20)

        Ptext = PRINTTEXT('point: '+str((p[turn].get_point())), size= 15)
        Ptext._blit_(loc=(SCREEN_WIDTH//2-len(p[turn].deck_list)/2*CARD_WIDTH-44, SCREEN_HEIGHT*3/4+30))
        
        for i in range(1,num_players):
            Ttext[i] = BUTTON(msg='Player: '+str(T[i]+1)+' ( point: '+str((p[T[i]].get_point()))+' )',\
                inactive_color=WHITE,font_size=15,action=None)
            Ttext[i].i = T[i]
        f_draw_card(p, turn, T, Ttext)
        
        # 버튼 및 텍스트 그리기
        button_take._draw_(loc = (SCREEN_WIDTH-100,105), size = (130,30), action = f_take_tile)
        button_turn._draw_(loc = (SCREEN_WIDTH-100,570), size = (130,30), action = next_turn)
        button_back._draw_(loc = (SCREEN_WIDTH-180,40), size = (130,30), action = bati_window)
        button_exit._draw_(loc = (SCREEN_WIDTH-67,40), size = (64,30), action = exit_window)
        select_card._blit_(loc=(5,30),loc_center=False)

        pygame.display.update()

#======== Initialize main game ==========#
pygame.init()                               # pygame library 초기화.
clock = pygame.time.Clock()                 # create an object to help track time.
clock.tick(30)                              # 딜레이 추가. Target_FPS = 30.

states = [True,True,True]                   # 초기 난이도 세팅 값.
game_intro()                                # 실행 장면을 위한 최초 함수.

pygame.quit()                               # pygame 종료

'''
=====================================<< main 끝>>================================================
'''