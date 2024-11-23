import pygame


class Npc():

    def __init__(self, id, x, y):
        self.width = 55
        self.height = 55
        self.npcId = id

        self.x = x
        self.y = y

        self.winW = 650
        self.winH = 500
        self.offx = self.winW/2 - 25 #25 è la metà della larghezza del mio sprite (50x50 px)
        self.offy = self.winH/2 - 25

        self.conversazione = self.stabilisciConversazione()
        #print(self.conversazione)

        self.sprite = f"immagini/sprite/giocatore{id}/giu/1.png"
        

    def stabilisciConversazione(self):

        match self.npcId:
            case 1:
                prof = "Dagata"
            case 2:
                prof = "AmatoG"
            case 3:
                prof = "Intra"

        file = open(f"dialoghi/{prof}.txt", "r")
        data = file.read()
        file.close()
        return data.split("\n")
    
    def draw(self, win, primoX, primoY):
        imm = pygame.image.load(self.sprite)
        imm = pygame.transform.scale(imm, (self.width, self.height))
        win.blit(imm, (self.x + self.offx - primoX, self.y + self.offy - primoY))





