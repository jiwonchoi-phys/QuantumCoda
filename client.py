import pygame
from network import Network
from player import Player

win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Client")


def redrawWindow(win,player, player2): # draw player 1 and player 2 in pygame 
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        p.onpress()
        redrawWindow(win, p, p2)

main()