import pygame

class Board():

    def __init__(self, board, x, y, range):
        self.width = 55
        self.height = 20
        self.board = board

        self.x = x
        self.y = y

        self.winW = 650
        self.winH = 500
        self.offx = self.winW/2 - 25 #25 è la metà della larghezza del mio sprite (50x50 px)
        self.offy = self.winH/2 - 25

        self.range = range
        self.rect = pygame.Rect((self.x - range/2 , self.y - range/2), (self.width + range, self.height + range))

        self.immagine = f"./immagini/slide/{board}.png"

        self.sprite = f"immagini/board/board.png"
        self.interagisci = "immagini/npc/interagisci.png" #percorso tasti interazione
        self.grandInteragisci = (16, 16) #grandezza del tasto per interazione
        self.grand_slide = (605, 340)
        
        self.vicino = False # se è abbastanza vicino all'npc
        self.showSlide = False # se la conversazione è stata attivata
        self.goClick = 0 # a che punto della conversazione si è.
        self.showSlideDone = False

        self.lung_riga = 27
    
    def draw(self, win, primoX, primoY):
        imm = pygame.image.load(self.sprite)
        imm = pygame.transform.scale(imm, (self.width, self.height))
        win.blit(imm, (self.x + self.offx - primoX, self.y + self.offy - primoY))

    def drawCliccabile(self, win, primoX, primoY):
        imm = pygame.image.load(self.interagisci)
        imm = pygame.transform.scale(imm, self.grandInteragisci)
        
        self.draw_interact_text(win, "per  visualizzare", (255,255,255), imm, primoX, primoY, 14)

    def draw_interact_text(self, win, text, col, intr, primoX, primoY, size):
        font = pygame.font.Font("./immagini/utility/mojang.ttf", size)
        img = font.render(text, True, col)
        win.blit(img, (self.x + self.width/2 - (intr.get_width() + img.get_width() + 6)/2 + intr.get_width() + 3 +  (self.offx - primoX), self.y + self.height + 10 + (self.offy - primoY)))
        win.blit(intr, (self.x + self.width/2 - (intr.get_width() + img.get_width() + 6)/2 + (self.offx - primoX), self.y + self.height + 10 + (self.offy - primoY)))

    def abbastanzaVicino(self, pos, grandezza):
        tempRect = pygame.Rect(pos, grandezza)
        if tempRect.colliderect(self.rect):
            self.vicino = True
        else:
            self.vicino = False
            self.showSlide = False

#
    def controlla_conversazione(self, win, primoX, primoY):
        if(self.vicino):
            keys = pygame.key.get_pressed()
            #isKeyReleased = event.type == pygame.KEYDOWN

            self.drawCliccabile(win, primoX, primoY) 

            if keys[pygame.K_n]:
                self.showSlide = True
            if keys[pygame.K_x]:
                self.showSlide = False
            if keys[pygame.K_SPACE]:
                self.showSlide = False
            
            self.visione_board(win)
        
    def visione_board(self, win):
        if (self.showSlide):
            imm = pygame.image.load(self.immagine)
            imm = pygame.transform.scale(imm, self.grand_slide)
            pos = ((self.winW - imm.get_width()) / 2, (self.winH - imm.get_height()) /2)
            win.blit(imm, pos)