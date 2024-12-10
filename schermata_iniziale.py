import pygame
import sys

testo = "Volume:  ON"

class SchermataIniziale:
    def __init__(self, win, width, height):
        self.win = win
        self.width = width
        self.height = height

        # self.font = pygame.font.SysFont("Byte Bounce", 128)
        self.small_font = pygame.font.SysFont("Mojang-Regular", 20)
        # self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.gray = (111, 111, 111)
        self.hover_color = (169, 169, 169)
        self.normal_color = self.gray
        self.outline_color = (0, 0, 0)

        self.button_width = 400
        self.button_height = 40

        self.small_button_width = 195

        self.button_gap = 15
        self.button_gappone = 10

        # self.button_playtarocco = pygame.Rect((self.width - self.button_width) / 2, 205, self.button_width, self.button_height)
        self.button_play = pygame.Rect((self.width - self.button_width) / 2, 245, self.button_width, self.button_height)

        total_buttons_width = self.small_button_width * 2 + self.button_gappone
        
        self.button_settings = pygame.Rect((self.width - total_buttons_width) / 2, self.button_play.bottom + self.button_gap, self.small_button_width, self.button_height)
        self.button_exit = pygame.Rect(self.button_settings.right + self.button_gappone, self.button_settings.top, self.small_button_width, self.button_height)

        self.background_image = pygame.image.load("immagini/utility/background_image.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        try:
            self.title_image = pygame.image.load("immagini/utility/nome_gioco.png")
            self.title_image = pygame.transform.scale(self.title_image, (self.width, 200))
        except pygame.error as e:
            print(f"Errore nel caricare l'immagine del titolo: {e}")
            sys.exit(1)

    def disegna_pulsanti(self):
        global testo

        self.win.blit(self.background_image, (0, 0))

        self.win.blit(self.title_image, (self.width / 2 - self.title_image.get_width() / 2, 50))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # self.disegna_pulsante(self.button_playtarocco, "Singleplayer", mouse_x, mouse_y)
        self.disegna_pulsante(self.button_play, "Multiplayer", mouse_x, mouse_y)
        self.disegna_pulsante(self.button_settings, testo, mouse_x, mouse_y)
        self.disegna_pulsante(self.button_exit, "Quit  Game", mouse_x, mouse_y)

        pygame.display.update()

    def disegna_volume(self):
        global testo
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if (testo == "Volume:  ON"):
            testo = "Volume:  OFF"
        else:
            testo = "Volume:  ON"

        self.disegna_pulsante(self.button_settings, testo, mouse_x, mouse_y)

        pygame.display.update()

    def disegna_pulsante(self, button_rect, text, mouse_x, mouse_y):
        if button_rect.collidepoint(mouse_x, mouse_y):
            color = self.hover_color
        else:
            color = self.normal_color

        pygame.draw.rect(self.win, self.outline_color, button_rect.inflate(3, 3))
        pygame.draw.rect(self.win, color, button_rect)

        text_surface = self.small_font.render(text, True, self.white)
        self.win.blit(text_surface, (button_rect.x + button_rect.width / 2 - text_surface.get_width() / 2, button_rect.y + button_rect.height / 2 - text_surface.get_height() / 2))

    def gestisci_eventi(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if self.button_playtarocco.collidepoint(event.pos):
                #     return "manutenzione"
                if self.button_play.collidepoint(event.pos):
                    return True
                elif self.button_settings.collidepoint(event.pos):
                    return "opzione"
                elif self.button_exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        return False

    def mostra(self):
        while True:
            self.disegna_pulsanti()
            
            azione = self.gestisci_eventi()
            if azione:
                return azione
            elif azione == "manutenzione":
                return "manutenzione"