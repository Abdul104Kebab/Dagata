import pygame
import time
from npc import Npc

pygame.mixer.init()
effetto1 = pygame.mixer.Sound("sound/npcSpeech/text-speech.mp3")

class Player():

    def __init__(self, spawn, player):
        self.x = spawn[0] #ascisse x
        self.y = spawn[1] #ordinate y
        self.vel = 4

        self.width = 55
        self.height = 55
        self.player = player

        self.definisciSprite(player)
        self.immagineAttuale = ""

        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.walkCount = 1

        self.spostDestra = 0
        self.spostSinistra = 0

        self.visibilita = False

        self.layer = 1

##############################################
    def updateP(self, sprite_group, map_rects, npcs, win, primoX, primoY, boards):
        self.move(sprite_group, map_rects)
        self.controlloNpc(npcs, win, primoX, primoY)
        self.controlloBoard(boards, win, primoX, primoY)

    def definisciSpostamenti(self, d, s):
        self.spostDestra = d
        self.spostSinistra = s

    def draw(self, win, p, primoX, primoY, vis):
        imm = pygame.image.load(self.camminaGiu[0])

        if self.walkCount == 9:
            self.walkCount = 1
        if self.up:
            imm = pygame.image.load(self.camminaSu[self.walkCount-1])
            self.walkCount += 1
        elif self.down:
            imm = pygame.image.load(self.camminaGiu[self.walkCount-1])
            self.walkCount += 1
        elif self.right:
            imm = pygame.image.load(self.camminaDestra[self.walkCount-1])
            self.walkCount += 1
        elif self.left:
            imm = pygame.image.load(self.camminaSinistra[self.walkCount-1])
            self.walkCount += 1

        imm = pygame.transform.scale(imm, (self.width, self.height))
        if (p+1 != self.player and vis):
            win.blit(imm, (self.x + self.spostDestra - primoX, self.y + self.spostSinistra - primoY))

        elif (vis or p+1 == self.player):
            win.blit(imm, (self.spostDestra, self.spostSinistra))
            

    def controlloNpc(self, npcs, win, primoX, primoY):
        
        #if keys[pygame.K_n]: #SINISTRA
        for n in npcs:
            n.abbastanzaVicino((self.x, self.y), (self.width, self.height))
            n.controlla_conversazione(win, primoX, primoY)
                #n.parlantina(n.abbastanzaVicino((self.x, self.y), (self.width, self.height), win), effetto1)

    def controlloBoard(self, boards, win, primoX, primoY):
        for b in boards:
            b.abbastanzaVicino((self.x, self.y), (self.width, self.height))
            b.controlla_conversazione(win, primoX, primoY)
                #n.parlantina(n.abbastanzaVicino((self.x, self.y), (self.width, self.height), win), effetto1)

    def move(self, mapTiles, mapRects):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: #SINISTRA
            tempRect = pygame.Rect((self.x - self.vel, self.y), (self.width, self.height))

            if self.controllaCollisioni(mapRects, tempRect):
                self.x -= self.vel
                for sprite in mapTiles:
                    sprite.rect.x += self.vel
            
        if keys[pygame.K_d]: #DESTRA
            tempRect = pygame.Rect((self.x + self.vel, self.y), (self.width, self.height))

            if self.controllaCollisioni(mapRects, tempRect):
                self.x += self.vel
                for sprite in mapTiles:
                    sprite.rect.x -= self.vel

        if keys[pygame.K_w]: #ALTO
            tempRect = pygame.Rect((self.x, self.y - self.vel), (self.width, self.height))

            if self.controllaCollisioni(mapRects, tempRect):
                self.y -= self.vel
                for sprite in mapTiles:
                    sprite.rect.y += self.vel

        if keys[pygame.K_s]: #BASSO
            tempRect = pygame.Rect((self.x, self.y + self.vel), (self.width, self.height))
            
            if self.controllaCollisioni(mapRects, tempRect):
                self.y += self.vel
                for sprite in mapTiles:
                    sprite.rect.y -= self.vel
        
        self.down = keys[pygame.K_s]
        self.up = keys[pygame.K_w]
        self.right = keys[pygame.K_d]
        self.left = keys[pygame.K_a]

        #se non si muove
        if (keys[pygame.K_a] == keys[pygame.K_s] == keys[pygame.K_d] == keys[pygame.K_w] == False):
            self.up = False

        self.update(mapTiles)


    def controllaCollisioni(self, mapRects, tempRect):
        for rectLayer in mapRects:
            if rectLayer > self.layer:
                for rect in mapRects[rectLayer]:
                    if tempRect.colliderect(rect):
                        #print(rect.x, rect.y, "-", tempRect.x, tempRect.y)
                        return False
        return True
    def update(self, map):
        self.rect = (self.x, self.y, self.width, self.height)

    def immagineGiocatore(self):
        return self.immagineAttuale
    
    def definisciSprite(self, p):
        self.camminaSu = []
        self.camminaGiu = []
        self.camminaDestra = []
        self.camminaSinistra = []

        self.salvaSpriteCamminata(p, self.camminaSu, "su")
        self.salvaSpriteCamminata(p, self.camminaGiu, "giu")
        self.salvaSpriteCamminata(p, self.camminaDestra, "destra")
        self.salvaSpriteCamminata(p, self.camminaSinistra, "sinistra")

    def salvaSpriteCamminata(self, p, lis, dir): #lis=lista dir=direzione
        for i in range(1,10):
            stringa = f"./immagini/sprite/giocatore{p}/{dir}/{i}.png"
            lis.append(stringa)




        

