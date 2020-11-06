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

    play = False
    while not play:
        for event in pygame.event.get():        # 기본 event loop
            if event.type == pygame.QUIT:       # pygame 종료
                pygame.quit()
                quit()

        shb1._draw_(loc = (100,300), size = (150,30), action=acb1)
        shb2._draw_(loc = (400,300), size = (150,30), action=acb2)
        shb3._draw_(loc = (700,300), size = (150,30))
        # text positions
        dp._blit_(loc='top center')

        pygame.display.update()

def acb1():
    window = Tk()
    window.title("버튼 테스트")
    window.geometry()
    label = Label(window, text="test")

    label.pack()

    b1 = Button(window, text="teeeest")
    b1.pack()

    window.mainloop()


def acb2():
    window=Tk()
    window.title("입력 테스트")
    window.geometry()
    window.resizable(False, False)
    label = Label(window, text="흰창에 숫자 입력")

    def calc(event):
        label.config(text="결과="+str(eval(entry.get())))
        print(str(eval(entry.get())))

    entry=Entry(window)
    entry.bind("<Return>", calc)
    entry.pack()

    label.pack()

    window.mainloop()