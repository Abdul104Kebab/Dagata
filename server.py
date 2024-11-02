import socket
from _thread import *
import sys

server = "192.168.178.104"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)

print("Waiting for a connection. SERVER STARTED")

def threaded_client(conn):
    conn.send(str.encode("connected"))

    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("disconnected")
                break
            else:
                print("received: ", reply)
                print("sending: ", reply)

            conn.sendall(str.encode(reply))

        except:
            break
    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connecting to:", addr)

    start_new_thread(threaded_client, (conn, ))

