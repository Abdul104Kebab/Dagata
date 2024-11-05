import pygame

class Player():

    def __init__(self, x, y, color, player):
        self.x = x
        self.y = y
        self.color = color
        self.vel = 3

        self.width = 50
        self.height = 50
        self.player = player

        self.definisciSprite(player)
        self.immagineAttuale = self.stazionario

        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.walkCount = 1


    def draw(self, win):
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
        win.blit(imm, (self.x, self.y))




    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: #SINISTRA
            self.x -= self.vel
            self.immagineAttuale = self.movimento

        if keys[pygame.K_d]: #DESTRA
            self.x += self.vel
            self.immagineAttuale = self.movimento
            

        if keys[pygame.K_w]: #ALTO
            self.y -= self.vel
            self.immagineAttuale = self.movimento

        if keys[pygame.K_s]: #BASSO
            self.y += self.vel
            self.immagineAttuale = self.movimento
        
        self.down = keys[pygame.K_s]
        self.up = keys[pygame.K_w]
        self.right = keys[pygame.K_d]
        self.left = keys[pygame.K_a]

        #se non si muove
        if (keys[pygame.K_a] == keys[pygame.K_s] == keys[pygame.K_d] == keys[pygame.K_w] == False):
            self.immagineAttuale = self.stazionario
            self.up = False


        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def immagineGiocatore(self):
        return self.immagineAttuale
    
    def definisciSprite(self, p):
        self.stazionario = "./sprite/giocatore"+str(p)+"/gioc.png"
        self.movimento = "./sprite/giocatore"+str(p)+"/gioc_mov.png"

        self.camminaSu = [
            f"./sprite/giocatore{p}/su/1.png",
            f"./sprite/giocatore{p}/su/2.png",
            f"./sprite/giocatore{p}/su/3.png",
            f"./sprite/giocatore{p}/su/4.png",
            f"./sprite/giocatore{p}/su/5.png",
            f"./sprite/giocatore{p}/su/6.png",
            f"./sprite/giocatore{p}/su/7.png",
            f"./sprite/giocatore{p}/su/8.png",
            f"./sprite/giocatore{p}/su/9.png"
        ]

        self.camminaGiu = [
            f"./sprite/giocatore{p}/giu/1.png",
            f"./sprite/giocatore{p}/giu/2.png",
            f"./sprite/giocatore{p}/giu/3.png",
            f"./sprite/giocatore{p}/giu/4.png",
            f"./sprite/giocatore{p}/giu/5.png",
            f"./sprite/giocatore{p}/giu/6.png",
            f"./sprite/giocatore{p}/giu/7.png",
            f"./sprite/giocatore{p}/giu/8.png",
            f"./sprite/giocatore{p}/giu/9.png"
        ]

        self.camminaDestra = [
            f"./sprite/giocatore{p}/destra/1.png",
            f"./sprite/giocatore{p}/destra/2.png",
            f"./sprite/giocatore{p}/destra/3.png",
            f"./sprite/giocatore{p}/destra/4.png",
            f"./sprite/giocatore{p}/destra/5.png",
            f"./sprite/giocatore{p}/destra/6.png",
            f"./sprite/giocatore{p}/destra/7.png",
            f"./sprite/giocatore{p}/destra/8.png",
            f"./sprite/giocatore{p}/destra/9.png"
        ]

        self.camminaSinistra = [
            f"./sprite/giocatore{p}/sinistra/1.png",
            f"./sprite/giocatore{p}/sinistra/2.png",
            f"./sprite/giocatore{p}/sinistra/3.png",
            f"./sprite/giocatore{p}/sinistra/4.png",
            f"./sprite/giocatore{p}/sinistra/5.png",
            f"./sprite/giocatore{p}/sinistra/6.png",
            f"./sprite/giocatore{p}/sinistra/7.png",
            f"./sprite/giocatore{p}/sinistra/8.png",
            f"./sprite/giocatore{p}/sinistra/9.png"
        ]

        

