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
            pos = (x*50, y*50)
            Tile(pos = pos, surf = surf, groups = sprite_group)


print("#######")

clientNumber = 0

def redrawWindow(win, player, players):
    win.fill((0, 128, 255))
    sprite_group.draw(win)
    temp = sorted(players, key=lambda Player:Player.y)
    for i in temp:
        if i!="players":
            i.draw(win)

    pygame.display.update()

def main():
    run = True

    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()
    plrs = n.send() #mi salvo l'intera lista dei giocatori

    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        plrs[p].move()
        n.update(plrs[p])
        plrs = n.send()
        
        redrawWindow(win, p, plrs)

main()



