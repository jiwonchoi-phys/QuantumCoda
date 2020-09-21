# -*- coding: utf-8 -*-

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
        
        elif loc == 'bottom left':
            text_rect = self.text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT*3 // 4)
            screen.blit(self.text,text_rect)
        
        elif loc == 'bottom right':
            text_rect = self.text.get_rect()
            text_rect.center = (SCREEN_WIDTH * 3 // 4, SCREEN_HEIGHT*3 // 4)
            screen.blit(self.text,text_rect)
        
        elif type(loc) == tuple: # User input of location
            text_rect = self.text.get_rect()
            text_rect.center = loc
            screen.blit(self.text,text_rect)        


class CARD():
    def __init__(self,color,num):
        # Set card&font color
        if color == 1: # Black
            self.card_color = BLACK
            self.font_color = WHITE
        else:
            self.card_color = GRAY
            self.font_color = BLACK
        
        self.card_num = num
        self.width, self.height = CARD_SIZE
        self.number = PRINTTEXT("%s" % self.card_num, 25, color=self.font_color)

    def get_color(self):
        return self.card_color

    def get_num(self):
        return self.card_num

    def out(self):
        pass
    
    def draw_img(self, loc=(0,0)):
        x, y = loc[0:2]
        pygame.draw.rect(screen, self.card_color, [x,y,self.width,self.height])
        self.number._blit_(loc=(x + self.width/2, y + self.height/2))
        


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
new_p2 = PRINTTEXT("2 Player", size=30)
new_p3 = PRINTTEXT("3 Player", size=30)
new_p4 = PRINTTEXT("4 Player", size=30)
color_active = GRAY
card1 = CARD(1,1)
card2 = CARD(0,1)


# ================== MAIN LOOP =====================
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

        # Starting menu
        title._blit_(loc='top center')
        
        new_p2._blit_(loc='bottom left')
        new_p3._blit_(loc='bottom center')
        new_p4._blit_(loc='bottom right')
        card1.draw_img()
        card2.draw_img(loc=(60,0))

        pygame.display.flip()

pygame.quit()