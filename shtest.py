import pygame
from util import *
from tkinter import *
from math import *

def shtestroom(): # 조세형 실험실
    screen.fill(WHITE)
    dp = PRINTTEXT("sh testroom", size = 50)
    shb1 = BUTTON("button test")
    shb2 = BUTTON("input test")
    shb3 = BUTTON("yet")
    shbb = BUTTON("back")

    play = False
    while not play:
        for event in pygame.event.get():        # 기본 event loop
            if event.type == pygame.QUIT:       # pygame 종료
                pygame.quit()
                quit()

        shb1._draw_(loc = (100,300), size = (150,30), action=acb1)
        shb2._draw_(loc = (400,300), size = (150,30), action=acb2)
        shb3._draw_(loc = (700,300), size = (150,30), action=acb3)
        shbb._draw_(loc = (800,550), size = (150,30))
        # text positions
        dp._blit_(loc='top center')

        pygame.display.update()

def acb1():
    window = Tk()                              # 윈도우 창을 생성
    window.title("버튼 테스트")                 # 타이틀
    window.geometry("480x300+100+100")         # "너비x높이+x좌표+y좌표"
    label = Label(window, text="test")         # 라벨 등록

    label.pack()



    def b1event():                      # 버튼 함수
        if(b1['text'] == 'hello'):
            b1['text'] = 'world'
            b1['fg'] = 'red'
            b1['bg'] = 'yellow'
        else:
            b1['text'] = 'hello'
            b1['fg'] = 'yellow'
            b1['bg'] = 'red'
        
    b1 = Button(window, text='hello',command = b1event, fg = 'yellow', bg = 'red')
    b1.pack()

    window.mainloop()   # 닫기 까지 이게 메인


def acb2():
    window=Tk()
    window.title("입력 테스트")
    window.geometry("480x300+100+100")
    window.resizable(False, False)                  # 창 크기 조절 가능 여부 거부
    label = Label(window, text="흰창에 숫자 입력")

    def calc(event):
        label.config(text="결과="+str(eval(entry.get()))) # 라벨 수정
        print(str(eval(entry.get())))                     # 기입값 출력

    entry=Entry(window, bd = 20)      # 기입창, 크기 기본 위아래폭의 30배
    entry.bind("<Return>", calc)      # 리턴값 calc 함수에 사용
    entry.pack(pady = 10)             # 위아래 간격 10

    label.pack(pady = 10)

    window.mainloop()

def acb3():
    acb3 = Tk()
    acb3.title("버튼 테스트")
    acb3.geometry()
    image=PhotoImage(file="a.png") 
    label = Label(acb3, image=image)         # 라벨 등록

    label.pack()

    acb3.mainloop()