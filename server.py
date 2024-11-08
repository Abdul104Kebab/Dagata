import socket
from _thread import *
import sys
from player import Player
import pickle

server = "192.168.178.104"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


try:
    s.bind((server, port))
except socket.error as e:
    str(e)

print("Waiting for a connection. SERVER STARTED")

players = [Player(0, 0, (255,0,0), 1), Player(100, 100, (0,0,255), 2)]
client_addresses = {}


def handle_client(data, addr):
    """ Gestisce i dati ricevuti da un client e invia la risposta. """
    if addr not in client_addresses:
        # Se il client non è ancora registrato, aggiungilo
        if len(client_addresses) < 2:
            player_id = len(client_addresses)
            client_addresses[addr] = player_id
            print(f"Nuovo giocatore {player_id + 1} connesso da {addr}")
        else:
            print("Massimo numero di giocatori raggiunto")
            return

    # Recupera il player_id del client e aggiorna i suoi dati
    player_id = client_addresses[addr]
    player_data = pickle.loads(data)  # Decodifica i dati inviati dal client
    players[player_id] = player_data  # Aggiorna i dati del giocatore

    # Determina l'avversario e invia i suoi dati al client
    opponent_id = 1 - player_id  # Se il giocatore è 0, l'avversario sarà 1, e viceversa
    reply = players[opponent_id]

    # Invia la risposta con i dati dell'avversario al client
    s.sendto(pickle.dumps(reply), addr)

while True:
    try:
        data, addr = s.recvfrom(2048)
        
        handle_client(data, addr)
    except Exception as e:
        print(f"Errore durante la gestione della comunicazione: {e}")

