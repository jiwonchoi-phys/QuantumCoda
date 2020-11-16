import pygame
from util import *
from tkinter import *
from math import *
import time

# 아래 내용들은 완성되면 util에 추가 될 것.

def f_option_room(): # 옵션 설정 방
    screen.fill([207, 216, 220])
    dp = PRINTTEXT("option testroom", size = 50)
    shb1 = BUTTON("button test")
    shb2 = BUTTON("Level Setting")
    shb3 = BUTTON("theory test")
    shbb = BUTTON("back test(main 이동 필요)")

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
    print("kkkkkkkkkkkkkkkkkkkkk")
    pass

def acb2():
    window=Tk()
    window.title("입력 테스트")
    window.geometry("480x300+100+100")
    window.resizable(False, False)                  # 창 크기 조절 가능 여부 거부
    def flash():
        checkbutton1.flash()

    CheckVariety_1=IntVar()
    CheckVariety_2=IntVar()

    checkbutton1=Checkbutton(window, text="O", variable=CheckVariety_1)
    checkbutton2=Checkbutton(window, text="△", variable=CheckVariety_2)
    checkbutton3=Checkbutton(window, text="X", variable=CheckVariety_2, command=flash)

    checkbutton1.pack()
    checkbutton2.pack()
    checkbutton3.pack()

    window.mainloop()

def acb3(): # 아 존나 귀찮다.
    global page
    
    acb3 = Tk()
    acb3.title("이론 설명창 테스트")
    acb3.geometry("600x300+100+100")

    page=0
    mpage = 3
    #image=PhotoImage(file="a.png") 
    #label = Label(acb3, image=image)         # 라벨 등록

    label1 = Label(acb3, text="intro")
    label2 = Label(acb3, text="~")
    label1.pack()
    label2.pack()

    Tbox = ["superposition:","entanglement:","collapse:"]
    Sbox = ["the ability of quantum objects to be in two places at once.",
            "the phenomenon where distant parts of a quantum system display correlations\nthat cannot be explained by either timelike causality or common cause.",
            "the phenomenon where the quantum states of a system are reduced to classical states.\nCollapses occur when a measurement happens,\nbut the mathematics of the current formulation of quantum mechanics is silent on the measurement process.\nMany of the interpretations of quantum mechanics derive from different efforts to deal with the measurement problem."]

    def pageUP():
        global page
        page +=1
        if page == mpage:
            label1.config(text=str(Tbox[page-1]))
            label2.config(text=str(Sbox[page-1]))

            buttonP = Button(acb3, overrelief="solid", width=15, command=pageDOWN, repeatdelay=1000, repeatinterval=100)
            buttonP.pack(side = LEFT, padx = 50)

        else:
            label1.config(text=str(Tbox[page-1]))
            label2.config(text=str(Sbox[page-1]))

            buttonP = Button(acb3, overrelief="solid", width=15, command=pageDOWN, repeatdelay=1000, repeatinterval=100)
            buttonP.pack(side = LEFT, padx = 50)
            buttonN = Button(acb3, overrelief="solid", width=15, command=pageUP, repeatdelay=1000, repeatinterval=100)
            buttonN.pack(side = RIGHT, padx = 50)

        
    def pageDOWN():
        global page
        page -=1

        label1.config(text=str(Tbox[page]))
        label2.config(text=str(Sbox[page]))

        buttonN = Button(acb3, overrelief="solid", width=15, command=pageUP, repeatdelay=1000, repeatinterval=100)
        buttonN.pack(side = RIGHT, padx = 50)

    buttonN = Button(acb3, overrelief="solid", width=15, command=pageUP, repeatdelay=1000, repeatinterval=100)
    buttonN.pack(side = RIGHT, padx = 50)
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
            plabel.config(text="플레이어 수가 너무 많습니다. 다시 입력해주세요.")
        elif pn < 2:
            plabel.config(text="플레이어 수가 너무 적습니다. 다시 입력해주세요.")
        elif pn >=2 and pn <= player_num_max:
            plabel.config(text="플레이어 수가 "+str(eval(entry.get()))+"명으로 결정되었습니다.")
            num_players = pn
            
            pn_tk.after(1000, pnd)          # 1000ms 이후 pnd 함수 연결

    def pnd():              # tk 파괴. 위 elif에 바로 연결시 라벨 변경 안멱혀서 따로 뗌
        pn_tk.destroy()

    entry=Entry(pn_tk, bd = 20)      # 기입창, 크기 기본 위아래폭의 30배
    entry.bind("<Return>", pcalc)      # 리턴값 calc 함수에 사용
    entry.pack(pady = 50)             # 위아래 간격 50

    plabel.pack()

    pn_tk.mainloop()
    return num_players

def f_tn(num_players):
    global tlabel, stn, fcn, max_card_num

    fcn=(max_card_num+1)*2              # full card number
    tn_tk=Tk()
    tn_tk.title("스타팅 타일 수 입력")
    tn_tk.geometry("480x300+100+100")
    tn_tk.resizable(False, False)       # 창 크기 조절 가능 여부 거부
    tlabel = Label(tn_tk, text="시작시 가져갈 초기 타일 수를 결정해 주세요.")
    
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
    entry.pack(pady = 50)             # 위아래 간격 50

    tlabel.pack()

    tn_tk.mainloop()
    return stn

def play_music():
    
    main_music = "White River - Aakash Gandhi.mp3"

    pygame.mixer.init()
    pygame.mixer.music.load(main_music)
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1) # 무한재생.

def button_sound():
    
    b_s = "18V Cordless Drill Switch.mp3"

    pygame.mixer.init()
    pygame.mixer.music.load(b_s)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(1)

def f_draw_card(p, turn, Ttext):
    T = list(range(turn,turn+num_players))
    p[T[0]].draw_card(SCREEN_WIDTH//2-len(p[T[0]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT*3/4)
    Ttext[0]._blit_(loc=(SCREEN_WIDTH//2-len(p[T[0]].deck_list)/2*CARD_WIDTH-50, SCREEN_HEIGHT*3/4),loc_center=False)

    for i in range(num_players):
        if T[i] >= num_players:
            T[i] = T[i]-num_players
    
    if num_players == 2:
        p[T[1]].draw_card(SCREEN_WIDTH//2-len(p[T[1]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT/4)
        Ttext[1]._blit_(loc=(SCREEN_WIDTH//2-len(p[T[1]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT/4-15),loc_center=False)

    if num_players == 3:
        p[T[1]].draw_card(CARD_WIDTH/2, SCREEN_HEIGHT/4)
        Ttext[1]._blit_(loc=(CARD_WIDTH/2, SCREEN_HEIGHT/4-15),loc_center=False)
        p[T[2]].draw_card(SCREEN_WIDTH-CARD_WIDTH*(0.5+len(p[T[2]].deck_list)), SCREEN_HEIGHT/4)
        Ttext[2]._blit_(loc=(SCREEN_WIDTH-CARD_WIDTH*(0.5+len(p[T[2]].deck_list)), SCREEN_HEIGHT/4-15),loc_center=False)
            
    if num_players == 4:
        p[T[1]].draw_card(CARD_WIDTH/2, SCREEN_HEIGHT/4+CARD_WIDTH*1.6+20)
        Ttext[1]._blit_(loc=(CARD_WIDTH/2, SCREEN_HEIGHT/4+CARD_WIDTH*1.6+20-15),loc_center=False)
        p[T[2]].draw_card(SCREEN_WIDTH//2-len(p[T[2]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT/4)
        Ttext[2]._blit_(loc=(SCREEN_WIDTH//2-len(p[T[2]].deck_list)/2*CARD_WIDTH, SCREEN_HEIGHT/4-15),loc_center=False)    
        p[T[3]].draw_card(SCREEN_WIDTH-CARD_WIDTH*(0.5+len(p[T[3]].deck_list)), SCREEN_HEIGHT/4+CARD_WIDTH*1.6+20)
        Ttext[3]._blit_(loc=(SCREEN_WIDTH-CARD_WIDTH*(0.5+len(p[T[3]].deck_list)), SCREEN_HEIGHT/4+CARD_WIDTH*1.6+20-15),loc_center=False)
        



