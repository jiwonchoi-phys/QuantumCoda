import socket
from _thread import *
from player import Player
import pickle

server = "localhost"        # server IP
port = 5555                 # server Port

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
                    #players[0].aa()
                    #players[1].aa()
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