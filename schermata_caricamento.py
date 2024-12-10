import pygame
import sys
import random
import time

class SchermataCaricamento:
    def __init__(self, win, width, height):
        self.win = win
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("Mojang-Regular", 20)
        self.white = (255, 255, 255)

        self.background_image = pygame.image.load("immagini/utility/manutenzione_image.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        self.loading_images = [
            pygame.image.load(f"immagini/sprite/giocatore6/destra/{i}.png") for i in range(1, 6)
        ]
        self.current_image = 0

        self.loading_text = "Caricamento del terreno..."

    def mostra(self):
        progress = 0
        clock = pygame.time.Clock()

        while progress < 100:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.win.blit(self.background_image, (0, 0))
            self.win.blit(self.loading_images[self.current_image], (self.width / 2 - self.loading_images[self.current_image].get_width() / 2, self.height / 3))

            self.current_image = (self.current_image + 1) % len(self.loading_images)

            text_surface = self.font.render(self.loading_text, True, self.white)
            self.win.blit(text_surface, (self.width / 2 - text_surface.get_width() / 2, self.height / 2 + 50))

            percent_text = f"{progress}%"
            percent_surface = self.font.render(percent_text, True, self.white)
            self.win.blit(percent_surface, (self.width / 2 - percent_surface.get_width() / 2, self.height / 2))

            pygame.display.update()

            progress += random.randint(2, 5)
            time.sleep(0.1)
            clock.tick(30)

        if progress > 100:
            progress = 100

        self.loading_text = "Caricamento completato!"
        self.win.blit(self.background_image, (0, 0))        
        self.win.blit(self.loading_images[0], (self.width / 2 - self.loading_images[0].get_width() / 2, self.height / 3))
        text_surface = self.font.render(self.loading_text, True, self.white)
        self.win.blit(text_surface, (self.width / 2 - text_surface.get_width() / 2, self.height / 2 + 50))

        percent_text = f"{progress}%"
        percent_surface = self.font.render(percent_text, True, self.white)
        self.win.blit(percent_surface, (self.width / 2 - percent_surface.get_width() / 2, self.height / 2))

        pygame.display.update()

        time.sleep(2)

        return True