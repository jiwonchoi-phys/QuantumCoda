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



def printText(msg,textfont="consolas",size=10,color=BLACK,loc=(0,0)):
    font = pygame.font.SysFont(textfont,size)
    text = font.render(msg, True, color)
    if loc == 'top center': 
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        screen.blit(text,text_rect)
    elif loc == 'center':
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(text,text_rect)
    elif loc.type == tuple: # User input of location
        screen.blit(text,loc)


# Set screen size & background color
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)


pygame.display.update()


# =============== MAIN LOOP =====================
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

        # Starting menu
        printText("Quantum Coda",size=50,loc='top center')        
        pygame.draw.rect(screen, BLACK, [75,175,75,50],5)
        pygame.display.flip()

pygame.quit()