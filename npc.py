import pygame

class Npc():

    def __init__(self, prof, x, y, range):
        self.width = 55
        self.height = 55
        self.prof = prof

        self.x = x
        self.y = y

        self.winW = 650
        self.winH = 500
        self.offx = self.winW/2 - 25 #25 è la metà della larghezza del mio sprite (50x50 px)
        self.offy = self.winH/2 - 25

        self.range = range
        self.rect = pygame.Rect((self.x - range/2 , self.y - range/2), (self.width + range, self.height + range))

        self.conversazione = self.stabilisciConversazione()
        #print(self.conversazione)

        self.sprite = f"immagini/npc/{prof}.png"
        

    def stabilisciConversazione(self):

        file = open(f"dialoghi/{self.prof}.txt", "r")
        data = file.read()
        file.close()
        return data.split("\n")
    
    def draw(self, win, primoX, primoY):
        imm = pygame.image.load(self.sprite)
        imm = pygame.transform.scale(imm, (self.width, self.height))
        win.blit(imm, (self.x + self.offx - primoX, self.y + self.offy - primoY))

    def abbastanzaVicino(self, pos, grandezza):
        tempRect = pygame.Rect(pos, grandezza)
        if tempRect.colliderect(self.rect): return self.conversazione
    




