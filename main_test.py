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

fcn=(max_card_num+1)*2              # full card number

ti = []                             # 전체 타일 묶음
tb = []                             # Tile Black
tw = []                             # Tile White

for i in range(0,max_card_num+1):   # 색상 정보 추가 (Black: 1, While: 0 으로 구분하는 for문)
    tb.append([1,field_black[i]])
    tw.append([0,field_white[i]])
    ti.append(tb[i])
    ti.append(tw[i])                # ti에 0과 1로 구분하고 넣음


random.shuffle(ti)                  # 모든 타일 섞음
# 아래 ti는 테스트를 위한 임시 타일묶음으로 지우지 말아주세요!!
# ti = [[1, [3, 5]], [1, [1, 0]], [1, [4, 1]], [1, [2, 5]], [0, [1, 0]], [1, [2, 3]], [0, [3, 0]], [0, [2, 5]], [0, [4, 5]], [0, [3, 2]], [1, [0, 4]], [0, [4, 1]]]
print("섞은 전체 타일: ",ti)

tii = [CARD(ti[i][0],ti[i][1]) for i in range(len(ti))]


for i in range(len(tii)):
    print(tii[i].get_color(), tii[i].get_num())


num_players = 3
stn = 3

p = [PLAYER() for i in range(num_players)]

for i in range(num_players): # 플레이어 수만큼 리스트 생성
    p[i].deck_list = []                           # 플레이어 i가 가지고 있는 패 (공개되지 않은것)
    p[i].opened_deck = []                # 플레이어 i가 가지고 있는 패중 공개된 
    for k in range(0,stn): #플레이어 리스트에 타일 배분
        qwer = random.choice(tii)
        p[i].deck_list.append(qwer)
        tii.pop(tii.index(qwer))


title = PRINTTEXT("Quantum Coda", size=50)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        title._blit_(loc='top center')
        
        
        for i, card in enumerate(tii):
            card.draw_img(loc=(i*CARD_WIDTH,0))
        pygame.display.flip()
        
        
pygame.quit()


