import socket
from _thread import *
import sys
from player import Player
from npc import Npc
from board import Board
import pickle

server = "172.22.0.159"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


try:
    s.bind((server, port))
except socket.error as e:
    str(e)

print("Waiting for a connection. SERVER STARTED")

spawn_point = (100, 70)
use_range = 40
grand_tile = 32

npcs = [Npc("Beppe", 205, 310, use_range), Npc("Dagata", 285, 32, use_range)] #Npc("Gaffuri", 250, 100, use_range)
boards = [Board(0, 0*grand_tile, 11*grand_tile, use_range, True),
            Board(1, 15*grand_tile, 1*grand_tile, use_range, False),
            Board(5, 33*grand_tile, 1*grand_tile, use_range, False),
            Board(7, 43*grand_tile, 1*grand_tile, use_range, False),
            Board(2, 21*grand_tile,  18*grand_tile, use_range, True),
            Board(3, 28*grand_tile,  3*grand_tile, use_range, True),
            Board(4, 29*grand_tile,  18*grand_tile, use_range, True),
            Board(6, 39*grand_tile,  18*grand_tile, use_range, True),
            Board(8, 48*grand_tile,  18*grand_tile, use_range, True)]

players = [Player(spawn_point, 1), Player(spawn_point, 2), Player(spawn_point, 3), Player(spawn_point, 4), Player(spawn_point, 5), Player(spawn_point, 6)]
client_addresses = {}


def handle_client(data, addr):
    """ Gestisce i dati ricevuti da un client e invia la risposta. """
    if addr not in client_addresses:
        # Se il client non è ancora registrato, aggiungilo
        if len(client_addresses) < 6:
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

    elif (dati == "npc"):
        s.sendto(pickle.dumps(npcs), addr)

    elif (dati == "boards"):
        s.sendto(pickle.dumps(boards), addr)

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

