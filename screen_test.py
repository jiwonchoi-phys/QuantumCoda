# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:50:53 2020

@author: jiwon
"""


import pygame
from util import *

# Initialize pygame
pygame.init()
pygame.display.set_caption("Quantum Coda")
clock = pygame.time.Clock()
done = False
clock.tick(30)



class PRINTTEXT():
    def __init__(self, msg, size, font='consolas', color=BLACK, antialias=True, background=None):
        self.msg = msg
        self.font = font
        self.size = size
        self.antialias = antialias
        self.color = color
        self.background = background 
        texts = pygame.font.SysFont(self.font, self.size)
        self.text = texts.render(self.msg, self.antialias, self.color, self.background)
    
    def _blit_(self, loc=(0,0)):
        
        if loc == 'top center': 
            text_rect = self.text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
            screen.blit(self.text,text_rect)
        
        elif loc == 'center':
            text_rect = self.text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(self.text,text_rect)
        
        elif loc == 'bottom center':
            text_rect = self.text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT*3 // 4)
            screen.blit(self.text,text_rect)
        
        elif type(loc) == tuple: # User input of location
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
        self.width, self.height = CARD_SIZE

    def get_color(self):
        return self.card_color

    def get_num(self):
        return self.card_num

    def out(self):
        pass
    
    def draw_img(self, loc=(0,0)):
        pygame.Rect(loc(0),loc(1),self.width,self.height)

class PLAYER():
    def __init__(self):
        self.deck_list = []
        self.closed_deck = []
        self.opened_deck = []
    
    def num_opened(self):
        return len(self.opened_deck)

        


# Set screen size & background color
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)


pygame.display.update()


# Starting menu object
title = PRINTTEXT("Quantum Coda",size=50)        
new_game = PRINTTEXT("New Game",size=30)
input_pn = PRINTTEXT("# of players: ", size=20)
color_active = GRAY
color_inactive = WHITE

# =============== MAIN LOOP =====================
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

        # Starting menu
        title._blit_(loc='top center')
        new_game._blit_(loc='bottom center')
        input_pn._blit_(loc=(100,400))


        pygame.display.flip()

pygame.quit()