"""
Some discription for util.py
                    CLASS
===========================================
PRINTTEXT(msg,size,font,color,antialias = True,background=None)
디스플레이에 문자열 출력
    
CARD(color,num)
카드 클래스
"""
from tkinter import *
import pygame
import math
import random
import numpy

pygame.init()       # # pygmae library 초기화.


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

max_card_num = 10 # 13까지 가능하나 10 완성 전까지 고정할 것. make_spooky 함수 안으로 넣지 말 것. 

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

class CARD():
    def __init__(self,color,num):   # 알고리즘 업데이트; num = [숫자,숫자,확률,확률] : 한 원소에 4개 값 List.
        # Set card&font color
        if color == 1: # Black
            self.card_color = BLACK
            self.font_color = WHITE
        else:
            self.card_color = GRAY
            self.font_color = BLACK
        
        self.color = color
        self.card_num = [num[0],num[1]]
        self.card_probability = [num[2],num[3]]
        self.card_loop = num[-1:]
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
                if action == None:
                    pass
                else: #print("클릭됨") # 확인용
                    self.f_click_tile()
        
        if self.opened == True:
            self.number._blit_(loc=(x + self.width/2, y + self.height/2))
            if len(self.get_num()) == 2:
                self.probability._blit_(loc=(x + self.width/2, y + self.height*3/4))
        
    def f_click_tile(self):

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
            PGN = int(entry.get()) # The player's guess number.
            if PGN in self.card_num:
                self.card_num = sf_p(self.card_num, self.card_probability)
                self.number = PRINTTEXT("%s" % self.card_num, 18, color=self.font_color)
                
                label1.config(text=str(t_num)+"로 붕괴 되었습니다.")
                
                ct_tk.after(1000, ctd)

            else:                                                                           #plabel.config(text="플레이어 수가 너무 적습니다 다시 입력해주세요")
                #sf_p(먹었던 타일의 수, 먹었던 타일의 확률)
                # 지원이 함수 연결
                pass

        def ctd():
            ct_tk.destroy()

        entry=Entry(ct_tk, bd = 20)
        entry.bind("<Return>", ctcalc)
        entry.pack(pady = 50)

        label1.pack()
        label2.pack()

        ct_tk.mainloop()
        #return
    
        
        

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

