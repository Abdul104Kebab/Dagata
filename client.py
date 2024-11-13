import pygame
import sys
from network import Network
from player import Player
from pytmx.util_pygame import load_pygame

pygame.init()
width = 650
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

offx = width/2 - 25 #25 è la metà della larghezza del mio sprite (50x50 px)
offy = height/2 - 25

###########################################################
tmx_data = load_pygame("./immagini/tilemap/mappaProva.tmx")
sprite_group = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

for layer in tmx_data.visible_layers:
    if hasattr(layer, "data"):
        for x,y,surf in layer.tiles():
            pos = (x*50 + offx, y*50 + offy)
            Tile(pos = pos, surf = surf, groups = sprite_group)


print("#######")

cont = 1
for layer in tmx_data.visible_layers:
    for x,y,surf in layer.tiles():
        print(x, "-", y, "-", surf, "LAYER: ", cont)
    cont += 1

print("#######")

clientNumber = 0

def redrawWindow(win, player, players):
    win.fill((0, 128, 255))
    sprite_group.draw(win)
    #temp = sorted(players, key=lambda Player:Player.y)
    cont = 0
    for i in players:
        if i!="players":
            i.draw(win, player, players[player].x, players[player].y, players[cont].visibilita)
        cont += 1

    pygame.display.update()

def main():
    run = True

    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()
    plrs = n.send() #mi salvo l'intera lista dei giocatori

    plrs[p].definisciSpostamenti(offx, offy)
    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        
        
        plrs[p].move(sprite_group)
        redrawWindow(win, p, plrs)
        n.update(plrs[p])
        plrs = n.send()

main()



