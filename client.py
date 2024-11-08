import pygame
from network import Network
from player import Player

width = 650
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

def redrawWindow(win, player, players):
    win.fill((255,0,0))
    for i in players:
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



