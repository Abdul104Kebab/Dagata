import pygame
import time

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
        self.interagisci = "immagini/npc/interagisci.png" #percorso tasti interazione
        self.grandInteragisci = (16, 16) #grandezza del tasto per interazione
        

    def stabilisciConversazione(self):

        file = open(f"dialoghi/{self.prof}.txt", "r")
        data = file.read()
        file.close()
        return data.split("\n")
    
    def draw(self, win, primoX, primoY):
        imm = pygame.image.load(self.sprite)
        imm = pygame.transform.scale(imm, (self.width, self.height))
        win.blit(imm, (self.x + self.offx - primoX, self.y + self.offy - primoY))

    def drawCliccabile(self, win, primoX, primoY):
        imm = pygame.image.load(self.interagisci)
        imm = pygame.transform.scale(imm, self.grandInteragisci)
        
        self.draw_text(win, "per interagire", (255,255,255), (100, 100), imm, primoX, primoY)

    def draw_text(self, win, text, col, pos, intr, primoX, primoY):
        font = pygame.font.Font("./immagini/utility/shiny.ttf", 17)
        img = font.render(text, True, col)
        win.blit(img, (self.x + self.width/2 - (intr.get_width() + img.get_width() + 6)/2 + intr.get_width() + 3 +  (self.offx - primoX), self.y + self.height + 10 + (self.offy - primoY)))
        win.blit(intr, (self.x + self.width/2 - (intr.get_width() + img.get_width() + 6)/2 + (self.offx - primoX), self.y + self.height + 10 + (self.offy - primoY)))

    def abbastanzaVicino(self, pos, grandezza, win, primoX, primoY):
        tempRect = pygame.Rect(pos, grandezza)
        if tempRect.colliderect(self.rect):
            self.drawCliccabile(win, primoX, primoY) 
            return self.conversazione
            

    def parlantina(self, listaStringhe, effetto1):
        if (listaStringhe != None):
            for stringa in listaStringhe:
                for l in stringa:
                    print(l, end="")
                    effetto1.play()
                    time.sleep(0.05)
                print("\n")
    

    




