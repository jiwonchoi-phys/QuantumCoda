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



class printText():
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
        elif loc.type == tuple: # User input of location
            screen.blit(self.text,loc)


# Set screen size & background color
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)


pygame.display.update()

title = printText("Quantum Coda",size=50)        
new_game = printText("New Game",size=30)

# =============== MAIN LOOP =====================
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

        # Starting menu
        title._blit_(loc='top center')
        new_game._blit_(loc='bottom center')
        pygame.display.flip()

pygame.quit()