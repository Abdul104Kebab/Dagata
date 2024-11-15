import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server = "172.22.20.132"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.sendto(pickle.dumps("connect"), self.addr)
            data, _ = self.client.recvfrom(2048)
            return pickle.loads(data)
        except: 
            print("MAUROBOLGIA")

    def send(self):
        try:
            self.client.sendto(pickle.dumps("players"), self.addr)
            data, _ = self.client.recvfrom(2048*4)
            return pickle.loads(data)
        except socket.error as e:
            print(e)
            return None
        
    def update(self, plr):
        try:
            self.client.sendto(pickle.dumps(plr), self.addr)
        except socket.error as e:
            print(e)
            return None



