
from network import Network
from tkinter import * 
from tkinter import messagebox
from tkinter.ttk import Notebook
from PIL import ImageTk, Image
import math
import random
import numpy
import time
import pygame

# RGB color information
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)

# Music
main_music = "White River - Aakash Gandhi.wav"
win_music = "Trimmed & Taught - Dan Lebowitz.wav"

# Object size
SCREEN_WIDTH  = 500
SCREEN_HEIGHT = 300
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)

#pygame.display.set_caption("Quantum Coda")  # 타일틀바에 텍스트 출력.

CARD_WIDTH = 60
CARD_SIZE = (CARD_WIDTH, 1.6*CARD_WIDTH)
Notice = " "        # Notice 첫 값.

max_card_num = 10   # 13까지 가능하나 10 완성 전까지 고정할 것. make_spooky 함수 안으로 넣지 말 것. 
cut_list=[]         # 각 loop당 카드의 갯수
pln=0               # 아이템 쓸 플레이어
clicked = False

class PRINTTEXT():
    def __init__(self, msg, size, font="calibri", bold=False, color=BLACK, antialias=True, background=None):
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

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        self.ready = False
        self.t = 0

    def onpress(self):
        global ck
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            if ck == 0:
                self.ready = not self.ready
                print(str(self.ready))
                ck = 1
        else:
            ck = 0
    
    def g_t(self):
        return self.t

    def g_ready(self):
        return  self.ready
    
    def aa(self):
        self.t = 1

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        if self.ready == True:
            pygame.draw.rect(win, YELLOW, (self.x+25,self.y+25,50,50))
        
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.vel

        if keys[pygame.K_d]:
            self.x += self.vel

        if keys[pygame.K_w]:
            self.y -= self.vel

        if keys[pygame.K_s]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Client")

def redrawWindow(win,player, player2): # draw player 1 and player 2 in pygame 
    pygame.init()
    win.fill((255,255,255))
    player.draw(screen)
    player2.draw(screen)

    if player.g_t() == 1:
        IamREADY = PRINTTEXT("READY", size = 50)
        IamREADY._blit_(loc= (SCREEN_WIDTH*1 // 2, SCREEN_HEIGHT*1//2))
    pygame.display.update()


def f_rn(): # 룸 넘버 입력 받는 tk 임시.
    global room
    rn_tk=Tk()
    rn_tk.title("test.")
    rn_tk.geometry("480x300+100+100")
    rn_tk.resizable(False, False)       # 창 크기 조절 가능 여부 거부
    dum = Label(rn_tk, text = "\n")
    dum.pack()
    label = Label(rn_tk, text="방 번호 1~3")
    
    def pcalc(event):
        global room
        rn = int(entry.get())
        if rn >= 1 and rn <= 3:
            label.config(text=str(rn))
            room = rn
            rn_tk.after(1000, pnd)          # 1000ms 이후 pnd 함수 연결

    def pnd():              # tk 파괴. 위 elif에 바로 연결시 라벨 변경 안멱혀서 따로 뗌
        rn_tk.destroy()

    entry=Entry(rn_tk, bd = 20)     # 기입창, 크기 기본 위아래폭의 30배
    entry.bind("<Return>", pcalc)   # 리턴값 calc 함수에 사용
    entry.pack(pady = 20)           # 위아래 간격 20

    label.pack()

    rn_tk.mainloop()

def main(room):
    run = True
    n = Network(room)
    p = n.getP()
    clock = pygame.time.Clock()

    print(n.check_conn())
    if n.check_conn() == False:
        print("Connected.")

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        #p.move()
        p.onpress()
        redrawWindow(screen, p, p2)

f_rn()
main(room)