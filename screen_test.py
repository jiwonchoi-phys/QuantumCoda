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


class BUTTON():
    def __init__(self, msg, x, y, width, height, inactive_color, active_color,\
        font_color=BLACK, font="consolas", font_size=30, action=None):
        self.msg = msg
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.ic = inactive_color
        self.ac = active_color
        self.f = font
        self.fc = font_color
        self.fs = font_size

    def _draw_(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.w > mouse_pos[0] > self.x and \
            self.y + self.h > mouse_pos[1]> self.y:
            
            pygame.draw.rect(screen,self.ac,(self.x,self.y,self.w,self.h))

            if click[0] == 1 and action != None:
                action()
        
        else:
            pygame.draw.rect(screen, self.ic, (self.x,self.y,self.w,self.h))
        
        text = pygame.font.SysFont(self.f, self.fs)
        textSurf = text.render(self.msg,True,self.fc)
        textRect = textSurf.get_rect()
        textRect.center = (self.x + self.w/2, self.y + self.h/2)
        screen.blit(textSurf,textRect)


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

but1 = BUTTON("button",100,100,200,200,ORANGE,PURPLE)


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
        but1._draw_()
        
        pygame.display.flip()

pygame.quit()