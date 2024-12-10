import pygame
import sys
from network import Network
from player import Player
from pytmx.util_pygame import load_pygame
import time
from schermata_iniziale import SchermataIniziale
from schermata_caricamento import SchermataCaricamento

pygame.init()
pygame.mixer.init()
width = 650
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

offx = width/2 - 25 #25 è la metà della larghezza del mio sprite (50x50 px)
offy = height/2 - 25

##################################SUONI##########################
muto = False
volume = 0.5

effetto1 = pygame.mixer.Sound("sound/npcSpeech/text-speech.mp3")

#----------------------------------------------------------------#


pygame.mixer.music.load("sound/sottofondo.mp3") #carica la canzone
pygame.mixer.music.play(loops=-1, fade_ms=2000) #loops quante volte si ripete (-1 infinite volte), fade_ms il dafe iniziale



###########################################################
tmx_data = load_pygame("./immagini/tilemap/mappa.tmx")
sprite_group = pygame.sprite.Group()
sprite_group_primo = pygame.sprite.Group()
sprite_group_secondo = pygame.sprite.Group()
map_rects = {}

class Tile(pygame.sprite.Sprite):
    def __init__(self, plrX, plrY, pos, surf, groups, groupTot, Templist):
        super().__init__(groups)
        super().__init__(groupTot)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        tempRect = pygame.Rect((pos[0]-offx + plrX, pos[1]-offy + plrY), (32, 32))
        Templist.append(tempRect)

#print(map_rects)

"""
print("#######")

cont = 1
for layer in tmx_data.visible_layers:
    for x,y,surf in layer.tiles():
        print(x, "-", y, "-", surf, "LAYER: ", cont)
    cont += 1

print("#######")
"""

clientNumber = 0

def creaMappa(plrX, plrY):
    cont = 1
    for layer in tmx_data.visible_layers:
        temp = []
        if hasattr(layer, "data"):
            for x,y,surf in layer.tiles():
                pos = (x*32 + offx - plrX, y*32 + offy - plrY)
                if(cont == 1):
                    Tile(plrX, plrY, pos = pos, surf = surf, groups = sprite_group_primo, groupTot = sprite_group, Templist = temp)
                else:
                    Tile(plrX, plrY, pos = pos, surf = surf, groups = sprite_group_secondo, groupTot = sprite_group, Templist = temp)
            map_rects[cont] = temp
            cont += 1

def redrawWindow(win, player, players, npcs, boards):
    win.fill((0, 128, 255))
    
    sprite_group.draw(win)
    #temp = sorted(players, key=lambda Player:Player.y)
    cont = 0
    for npc in npcs:
        npc.draw(win, players[player].x, players[player].y)

    for i in players:
        if i!="players":
            i.draw(win, player, players[player].x, players[player].y, players[cont].visibilita)
        cont += 1
    sprite_group_secondo.draw(win)
    
    players[player].updateP(sprite_group, map_rects, npcs, win, players[player].x, players[player].y, boards)

    pygame.display.update()

def main():
    global muto, volume, booleano

    while True:
        schermata = SchermataIniziale(win, width, height)
        schermata_caricamento = SchermataCaricamento(win, width, height)

        risultato = schermata.mostra()

        if risultato == "opzione":
            if muto:
                pygame.mixer.music.set_volume(volume)
                muto = False
            else:
                volume = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(0)
                muto = True
            schermata.disegna_volume()

        elif risultato == True:
            schermata_caricamento.mostra()

            run = True

            n = Network()
            p = n.getP()
            print(p, "-----")
            clock = pygame.time.Clock()
            plrs = n.send() #mi salvo l'intera lista dei giocatori
            npcs = n.getNpc() 
            boards = n.getBoards()  

            creaMappa(plrs[p].x, plrs[p].y)
            
            plrs[p].definisciSpostamenti(offx, offy)
            while run:
                clock.tick(40)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()


                #plrs[p].updateP(sprite_group, map_rects, npcs)
                redrawWindow(win, p, plrs, npcs, boards)
                n.update(plrs[p])
                plrs = n.send()

main()



