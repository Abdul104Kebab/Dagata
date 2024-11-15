import socket
from _thread import *
import sys
from player import Player
import pickle

server = "172.22.20.132"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


try:
    s.bind((server, port))
except socket.error as e:
    str(e)

print("Waiting for a connection. SERVER STARTED")

players = [Player(0, 0, 1, False), Player(0, 0, 2, False), Player(0, 0, 3, False), Player(0, 0, 4, False)]
client_addresses = {}


def handle_client(data, addr):
    """ Gestisce i dati ricevuti da un client e invia la risposta. """
    if addr not in client_addresses:
        # Se il client non è ancora registrato, aggiungilo
        if len(client_addresses) < 4:
            player_id = len(client_addresses)
            client_addresses[addr] = player_id
            print(f"Nuovo giocatore {player_id + 1} connesso da {addr}")
        else:
            print("Massimo numero di giocatori raggiunto")
            return



    dati = pickle.loads(data)
    
    # RISPOSTE
    if (dati == "connect"):
        s.sendto(pickle.dumps(player_id), addr)

        players[player_id].visibilita = True

    elif (dati == "players"):
        s.sendto(pickle.dumps(players), addr)

    elif (type(dati) is Player):
        player_id = client_addresses[addr]
        players[player_id] = dati
        #print("PLAYER ", player_id, players[player_id].x, "--", players[player_id].y)

while True:
    try:
        data, addr = s.recvfrom(2048)
        
        handle_client(data, addr)
    except Exception as e:
        print(f"Errore durante la gestione della comunicazione: {e}")

