import socket
from _thread import *
from player import Player
from tkinter import *
import pickle
'''
1. 서버에서 클라이인트 정보를 바꿀 수 있는건 reply로 전달 되는 player class뿐. 그외 서버 내에서 변경가능하나 클라로 전송 불가.
    > 리스트로 reply = [player, 기타 변수] 생각해 봤으나, 구축 되어있는 서버 연결 함수상 힘들 듯.
    > 가능한 사람 진행 해주셈.

2. 위의 서버 내에서 변경하는 변수들은 서버에 import하는 Player함수 우선.
    [즉, 클라이언트 화면에 표기 되는 화면 우선순위 서버 player > 클라 player]

TO_DO) 서버에 기존 NEW_MAIN 등 들고와서, 서버에서 카드 미리 생성해 두고, 플레이어 접속시 덱 같이 전송해야 할 듯.

문제점: 현재 구현된 서버-클라 이동 체계가 클라이언트의 화면에서 클릭한 상대 타일의 데이터를 서버에 바로 전송하기 힘들어 보임.
        > 상대 덱 지목하고 결과 까지 '지목하는 플레이어 클라이언트에서 계산해서' 서버에 보내야하는 암담한 상황 예상.
    
요약. 시간 모자람. 망함.
'''
def f_rn(): # 룸 넘버 입력 받는 tk 임시.
    global room
    rn_tk=Tk()
    rn_tk.title("test.")
    rn_tk.geometry("480x300+100+100")
    rn_tk.resizable(False, False)       # 창 크기 조절 가능 여부 거부
    dum = Label(rn_tk, text = "\n")
    dum.pack()
    label = Label(rn_tk, text="방 번호 1~3")
    
    def pcalc(event):
        global room
        rn = int(entry.get())
        if rn >= 1 and rn <= 3:
            label.config(text=str(rn))
            room = rn
            rn_tk.after(1000, pnd)          # 1000ms 이후 pnd 함수 연결

    def pnd():              # tk 파괴. 위 elif에 바로 연결시 라벨 변경 안멱혀서 따로 뗌
        rn_tk.destroy()

    entry=Entry(rn_tk, bd = 20)     # 기입창, 크기 기본 위아래폭의 30배
    entry.bind("<Return>", pcalc)   # 리턴값 calc 함수에 사용
    entry.pack(pady = 20)           # 위아래 간격 20

    label.pack()

    rn_tk.mainloop()



'''
===========================================서버=========================================
'''



def f_room(room):
    server = "localhost"        # server IP
    port = 5554+room                # server Port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # use IPv4 for connection and process any datas as Binary (TCP)
    try:
        s.bind((server, port)) # get server ip and port
    except socket.error as e:
        str(e)
    s.listen(3)
    print("Waiting for a connection, Server Started")

    players = [Player(100,100,100,100,(255,0,0)), Player(300,100,100,100, (0,0,255))] # Server arranges players.

    def threaded_client(conn, player):
        conn.send(pickle.dumps(players[player]))
        reply = ""
        while True:
            try:
                data = pickle.loads(conn.recv(2048)) # recv("packet"). lower to 2K(1K = 1024 bytes) max to 64K. If the data size is 8K and your buffer size is 2K then the data will be process to divide 4 and 2K*4
                players[player] = data

                if not data:
                    print("Disconnected")
                    break
                else:
                    
                    if players[0].g_ready() == True and players[1].g_ready() == True:
                        print("all ready")

                    if player == 1:
                        reply = players[0]
                    else:
                        reply = players[1]
                    
                    #print("Received: ", data)
                    #print("Sending : ", reply)

                conn.sendall(pickle.dumps(reply))
            except:
                break

        print("Lost connection")
        conn.close()

    currentPlayer = 0
    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)
        start_new_thread(threaded_client, (conn, currentPlayer))
        currentPlayer += 1

f_rn()
f_room(room)