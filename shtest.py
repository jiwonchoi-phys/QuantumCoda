import pygame
from util import *
from tkinter import *
from math import *
import time

# 아래 내용들은 완성되면 util에 추가 될 것.

def shtestroom(): # 조세형 실험실
    screen.fill(WHITE)
    dp = PRINTTEXT("sh testroom", size = 50)
    shb1 = BUTTON("button test")
    shb2 = BUTTON("input test")
    shb3 = BUTTON("theory test")
    shbb = BUTTON("back test")

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

def f_pn():
    global plabel, num_players
    player_num_max = 4  #게임 가능 플레이어 수 제한

    pn_tk=Tk()
    pn_tk.title("플레이어 수 입력")
    pn_tk.geometry("480x300+100+100")
    pn_tk.resizable(False, False)       # 창 크기 조절 가능 여부 거부
    plabel = Label(pn_tk, text="위의 창에 플레이어 숫자를 입력하세요.\n플레이 최소 인원은 2명이고 최대 인원은 "+str(player_num_max)+"명 입니다.")
    
    def pcalc(event):
        global num_players
        pn = int(entry.get())
        if pn > player_num_max:
            plabel.config(text="플레이어 수가 너무 많습니다 다시 입력해주세요")
        elif pn < 2:
            plabel.config(text="플레이어 수가 너무 적습니다 다시 입력해주세요")
        elif pn >=2 and pn <= player_num_max:
            plabel.config(text="플레이어 수가 "+str(eval(entry.get()))+"명으로 결정되었습니다.")
            num_players = pn
            
            pn_tk.after(1000, pnd)          # 1000ms 이후 pnd 함수 연결

    def pnd():              # tk 파괴. 위 elif에 바로 연결시 라벨 변경 안멱혀서 따로 뗌
        pn_tk.destroy()

    entry=Entry(pn_tk, bd = 20)      # 기입창, 크기 기본 위아래폭의 30배
    entry.bind("<Return>", pcalc)      # 리턴값 calc 함수에 사용
    entry.pack(pady = 10)             # 위아래 간격 10

    plabel.pack(pady = 10)

    pn_tk.mainloop()
    return num_players

def f_tn(num_players):
    global tlabel, stn, fcn, max_card_num

    fcn=(max_card_num+1)*2              # full card number
    tn_tk=Tk()
    tn_tk.title("스타팅 타일 수 입력")
    tn_tk.geometry("480x300+100+100")
    tn_tk.resizable(False, False)       # 창 크기 조절 가능 여부 거부
    tlabel = Label(tn_tk, text="시작시 가져갈 초기 타일 수를 결정해 주세요(3 권장).")
    
    def tcalc(event):
        global num_players, stn
        stn = int(entry.get())
        if stn > fcn/num_players:
            tlabel.config(text="패를 나누기 위한 전체 타일 수가 부족합니다. 작은 수로 다시 입력해주세요.")
        elif stn < 2:
            tlabel.config(text="타일 수가 너무 적습니다. 다시 입력해주세요.")
        elif stn >= 2 and stn <= fcn/num_players:
            tlabel.config(text="플레이어가 받는 타일 수가 "+str(stn)+"개로 결정되었습니다.")

            tn_tk.after(1000, tnd)          # 1000ms 이후 pnd 함수 연결

    def tnd():              # tk 파괴. 위 elif에 바로 연결시 라벨 변경 안멱혀서 따로 뗌
        tn_tk.destroy()

    entry=Entry(tn_tk, bd = 20)      # 기입창, 크기 기본 위아래폭의 30배
    entry.bind("<Return>", tcalc)      # 리턴값 calc 함수에 사용
    entry.pack(pady = 10)             # 위아래 간격 10

    tlabel.pack(pady = 10)

    tn_tk.mainloop()
    return stn
