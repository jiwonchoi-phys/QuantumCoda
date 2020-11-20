import socket
from _thread import *
from player import Player
import pickle

server = "192.168.0.30"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # use IPv4 for connection and process any datas as Binary (TCP)

try:
    s.bind((server, port)) # get server ip and port
except socket.error as e:
    str(e)

s.listen(3)
print("Waiting for a connection, Server Started")


players = [Player(0,0,50,50,(255,0,0)), Player(100,100, 50,50, (0,0,255)), Player(200,200, 50,50, (0,255,255))] # Server arranges players.

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
                if player == 1:
                    reply = players[0]
                elif player == 2:
                    reply = players[1]
                else:
                    reply = players[2]

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