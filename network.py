import socket
import pickle
import time

class Network:
    def __init__(self,room):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"           # Server IP
        self.port = 5554 + room                   # Server port
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p
    
    def check_conn(self):
        try:
            self.client.connect(self.addr)
            self.client.shutdown(2)
            return True
        except:
            return False

    def connect(self):
        try:
            self.client.connect(self.addr)
            print("Connected to",self.server,self.port)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)