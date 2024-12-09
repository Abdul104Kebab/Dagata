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
        self.box_dialogo = "immagini/utility/dialogue.png"
        self.grand_dialogo = (600, 330)
        
        self.vicino = False # se è abbastanza vicino all'npc
        self.conv = False # se la conversazione è stata attivata
        self.goClick = 0 # a che punto della conversazione si è.

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
        
        self.draw_interact_text(win, "per interagire", (255,255,255), imm, primoX, primoY, 17)

    def draw_interact_text(self, win, text, col, intr, primoX, primoY, size):
        font = pygame.font.Font("./immagini/utility/shiny.ttf", size)
        img = font.render(text, True, col)
        win.blit(img, (self.x + self.width/2 - (intr.get_width() + img.get_width() + 6)/2 + intr.get_width() + 3 +  (self.offx - primoX), self.y + self.height + 10 + (self.offy - primoY)))
        win.blit(intr, (self.x + self.width/2 - (intr.get_width() + img.get_width() + 6)/2 + (self.offx - primoX), self.y + self.height + 10 + (self.offy - primoY)))

    def abbastanzaVicino(self, pos, grandezza):
        tempRect = pygame.Rect(pos, grandezza)
        if tempRect.colliderect(self.rect):
            self.vicino = True
        else:
            self.vicino = False
            self.conv = False
            self.goClick = 0

#
    def controlla_conversazione(self, win, primoX, primoY):
        if(self.vicino):
            keys = pygame.key.get_pressed()
            #isKeyReleased = event.type == pygame.KEYDOWN

            self.drawCliccabile(win, primoX, primoY) 

            if keys[pygame.K_n]:
                self.conv = True
            if keys[pygame.K_x]:
                self.conv = False
                self.goClick = 0
            if keys[pygame.K_SPACE]:
                self.goClick += 1
            
            self.parte_conversazione(win, primoX, primoY)
        
    def parte_conversazione(self, win, primoX, primoY):
        if (self.conv):
            imm = pygame.image.load(self.box_dialogo)
            imm = pygame.transform.scale(imm, self.grand_dialogo)
            pos = ((self.winW - imm.get_width()) / 2, self.winH - imm.get_height() + 30)
            win.blit(imm, pos)

            self.draw_conversation_text(win, (0, 0, 0), pos, 24)

    def draw_conversation_text(self, win, col, pos, size):
        font = pygame.font.Font("./immagini/utility/shiny.ttf", 30)
        nome_npc = font.render(self.prof, True, (255, 255, 255))
        win.blit(nome_npc, (pos[0] + 120, pos[1] + 83))

        try:
            stringa = self.conversazione[self.goClick]
            for l in range ( len(stringa) ):
                win.blit( self.ridai_lettera(stringa[l], col), (pos[0] + 100 + size*l, pos[1] + 200))
                #effetto1.play()
        except:
            self.conv = False
            self.goClick = 0

        print("\n")
    
    def ridai_lettera(self, l, col):
        font = pygame.font.SysFont("./immagini/utility/shiny.ttf", 30)
        lettera = font.render(l, True, col)
        return lettera
#
            
    ##PROVA##
    def parlantina(self, listaStringhe, effetto1):
        if (listaStringhe != None):
            for stringa in listaStringhe:
                for l in stringa:
                    print(l, end="")
                    effetto1.play()
                    time.sleep(0.05)
                print("\n")
    

    




