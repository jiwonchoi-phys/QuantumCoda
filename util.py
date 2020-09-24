import pygame

pygame.init()


# RGB color information
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)
RED     = (255,  0,  0)
GREEN   = (  0,255,  0)
BLUE    = (0  ,  0,255)
YELLOW  = (255,255,  0)
CYAN    = (  0,255,255)
MAGENTA = (255,  0,255)

ORANGE  = (255, 94,  0)
PURPLE  = (217, 65,197)
GRAY    = (201,201,201)


# Object size
SCREEN_WIDTH  = 900
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)

CARD_WIDTH = 60
CARD_SIZE = (CARD_WIDTH, 1.6*CARD_WIDTH)

screen = pygame.display.set_mode(SCREEN_SIZE)

first_handcard_num = 3
max_card_num = 5
min_loop_num = 2



class PRINTTEXT():
    """
    PRINTTEXT : 디스플레이에 글자를 출력하기 위한 클래스

    msg : 출력하고자 하는 문자열
    size : 문자열의 사이즈
    font : 문자열의 글꼴
    color : 문자열의 색깔
    ...
    """

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
        self.action = action

    def _draw_(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.w > mouse_pos[0] > self.x and \
            self.y + self.h > mouse_pos[1]> self.y:
            
            pygame.draw.rect(screen,self.ac,(self.x,self.y,self.w,self.h))

            if click[0] == 1 and self.action != None:
                action()
        
        else:
            pygame.draw.rect(screen, self.ic, (self.x,self.y,self.w,self.h))
        
        text = pygame.font.SysFont(self.f, self.fs)
        textSurf = text.render(self.msg,True,self.fc)
        textRect = textSurf.get_rect()
        textRect.center = (self.x + self.w/2, self.y + self.h/2)
        screen.blit(textSurf,textRect)


def make_spooky(x):
    global max_card_num # 패의 최대 숫자 전역변수
    global min_loop_num  # 최소 루프 개수
    
    cut_num = list(range(0,math.ceil((max_card_num+1)/min_loop_num)-2)) # [0,1] # math.ceil함수는 숫자 올림
    cut = []                     # cut1을 보관하는 장소
    card_list = list(range(0,max_card_num+1)) # 0~5 총 6개
    random.shuffle(card_list) # 섞는다 (shuffle 함수 기능)
    
    while 1:  # 얽힐 숫자들을 정하는 코드
        cut1 = 3+random.choice(cut_num) # cut_num의 임의 원소 선택, 루프 안에 들어가는 숫자의 개수, 3+가 있는 이유는 최소 루프 안에 들어있는 카드 숫자가 3이상이어야 하기 때문에. cut_num에서 숫자를 가져오는 이유는 루프 안에 있는 숫자의 개수를 다양화하기 위해 가져옴.
        cut.append(cut1) # 3 아님 4 추가
    
        if sum(cut) == max_card_num + 1:         # 총 얽힘수가 총 카드수랑 같으면 멈춤
            break
    
        elif sum(cut) > max_card_num + 1:            # cut수가 총 카드수보다 크면 마지막 cut1을 cut에서 뺀 후 뺀 것을 cut2라고 지정
            cut2 = cut.pop()
    
            if max_card_num + 1 - sum(cut) < 3:         # 남아 있는 수가 최소 얽힘수(3)보다 작다면 이전에 있던 cut1의 숫자를 늘려서 루프에 포함시킨다.
                cut[len(cut)-1] += max_card_num + 1 - sum(cut) 
    
            else:
                cut.append(cut2)          # 반대로 남아 있는 카드 수가 최소 얽힘수(3)보다 크거나 같으면 이전에 없앴던 cut1을 줄여서 남은 카드 수만큼 맞춘 다음, 다시 cut에 집어넣는다.
                cut[len(cut)-1] = max_card_num + 1 - sum(cut)    
    
    card_num = list(numpy.zeros(len(cut)))       # 루프 수만큼 방을 생성
    add_card_s = -cut[0] 
    add_card_f = 0
    
    for i in range(0,len(cut)):          # 얽혀 있는 카드들끼리 한 방을 쓰도록 배정
        card_num[i] = []
        add_card_s += cut[i] 
        add_card_f += cut[i]                   
    
        for k in range(add_card_s,add_card_f): 
            card_num[i].append(card_list[k])
    
    for i in range(0,len(card_num)):                # 각 방에 배정받은 숫자를 짝지어 spooky 카드를 만들도록 함
    
        for k in range(0,len(card_num[i])):   
            spooky_card_num = [card_num[i][k-1],card_num[i][k]] 
            x.append(spooky_card_num)
    
    return x           

