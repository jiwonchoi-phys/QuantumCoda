# -*- coding: utf-8 -*-

import pygame
from util import *

# Initialize pygame
pygame.init()
pygame.display.set_caption("Quantum Coda")
clock = pygame.time.Clock()
done = False
clock.tick(30)


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