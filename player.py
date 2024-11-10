import pygame

class Player():

    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.vel = 3

        self.width = 50
        self.height = 50
        self.player = player

        self.definisciSprite(player)
        self.immagineAttuale = ""

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

        if keys[pygame.K_d]: #DESTRA
            self.x += self.vel

        if keys[pygame.K_w]: #ALTO
            self.y -= self.vel

        if keys[pygame.K_s]: #BASSO
            self.y += self.vel
        
        self.down = keys[pygame.K_s]
        self.up = keys[pygame.K_w]
        self.right = keys[pygame.K_d]
        self.left = keys[pygame.K_a]

        #se non si muove
        if (keys[pygame.K_a] == keys[pygame.K_s] == keys[pygame.K_d] == keys[pygame.K_w] == False):
            self.up = False

        self.update()

    def update(self):
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


        

