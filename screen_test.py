# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:50:53 2020

@author: jiwon
"""


import pygame
from util import *  # util이 없어!

# Initialize pygame
pygame.init()                               # pygmae library 초기화.
pygame.display.set_caption("Quantum Coda")  # 타일틀바에 텍스트 출력.
clock = pygame.time.Clock()                 # create an object to help track time.
done = False
clock.tick(30)                              # 딜레이 추가. Target_FPS = 30.



class PRINTTEXT():
    def __init__(self, msg, size, font='consolas', color=BLACK, antialias=True, background=None):
        self.msg = msg                  # 메세지
        self.font = font                # font 지정 (기본 conslas)
        self.size = size                # size 지정
        self.antialias = antialias      # AA 지정 (기본 true)
        self.color = color              # 색상 지정 (기본 검정)
        self.background = background    # 바탕 지정 (기본 없음)
        texts = pygame.font.SysFont(self.font, self.size)   # texts는 지정한 폰트와 사이즈 사용.
        self.text = texts.render(self.msg, self.antialias, self.color, self.background) # ?, AA, color, bg 적용하여 렌더링.
    
    def _blit_(self, loc=(0,0)):    # 좌표 지정 위치 0,0의 오른쪽
        
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
        
        elif type(loc) == tuple: # User input of location 튜플이면 그 값을 센터로 받음. ex. (5,10) ?
            text_rect = self.text.get_rect()
            text_rect.center == loc
            screen.blit(self.text,text_rect)

class CARD():
    def __init__(self,color,num):   
        # Set card&font color
        if color == 1: # Black
            self.card_color = BLACK
            self.font_color = WHITE
        else:
            self.card_color = WHITE
            self.font_color = BLACK
        
        self.card_num = num
        self.width, self.height = CARD_SIZE # 밑에서 지정

    def get_color(self):
        return self.card_color

    def get_num(self):
        return self.card_num

    def out(self): # 아직 추가 안한 것?
        pass
    
    def draw_img(self, loc=(0,0)):
        pygame.Rect(loc(0),loc(1),self.width,self.height)   # 사각형 그림 (왼쪽, 위, 너비, 높이)

class PLAYER():
    def __init__(self):
        self.deck_list = []
        self.closed_deck = []
        self.opened_deck = []
    
    def num_opened(self):
        return len(self.opened_deck)

        


# Set screen size & background color
screen = pygame.display.set_mode(SCREEN_SIZE)   # 스크린 사이즈대로 생성
screen.fill(WHITE)                              # 스크린 흰색을 채움


pygame.display.update() # 화면 업데이트


# Starting menu object
title = PRINTTEXT("Quantum Coda",size=50)           # class-PRINTTEXT 사용 msg,size 설정 그외 기본. 
new_game = PRINTTEXT("New Game",size=30)            # 새게임 메세지
input_pn = PRINTTEXT("# of players: ", size=20)     # n 명의 플레이어
color_active = GRAY                                 # 마우스 올리면 회색
color_inactive = WHITE                              # 마우스 없으면 흰색

# =============== MAIN LOOP =====================
while not done:

    for event in pygame.event.get():            # ?
        if event.type == pygame.QUIT:           # ?
            done=True                           # ?

        # Starting menu
        title._blit_(loc='top center')          # title 메세지를 탑센테에 블럭전송
        new_game._blit_(loc='bottom center')    # 새게임 메세지를 중앙센터에 블럭전송
        input_pn._blit_(loc=(100,400))          # pn을 블럭전송


        pygame.display.flip()           #?

pygame.quit()   # 끔