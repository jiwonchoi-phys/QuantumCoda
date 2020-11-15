'''
Please Check System font because a number of fonts doesn't support Korean.
Windows:
Ubuntu: notosanscjkkr
'''

import pygame

for i in pygame.font.get_fonts():
    print(i)