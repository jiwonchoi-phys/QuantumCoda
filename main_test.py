import pygame
from util import *

# Initialize pygame
pygame.init()
pygame.display.set_caption("Quantum Coda")
clock = pygame.time.Clock()
done = False
clock.tick(30)


screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)
pygame.display.update()

# 2 players game
num_players = 2

players = [PLAYER() for i in range(num_players)]
print(players)

p1 = players[0]
p2 = players[1]

field_black = []
field_white = []
make_spooky(field_black)
make_spooky(field_white)


title = PRINTTEXT("Quantum Coda", size=50)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        title._blit_(loc='top center')
        pygame.display.flip()
        
pygame.quit()


