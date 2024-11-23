import pygame

width = 300
height = 150
padding = 50

speaker_label_x = 50
speaker_label_y = 25

content_label_x = 50
content_label_y = 75

helper_label_x = 50
helper_label_y = 150

class DialogueView:
    def __init__(self, lines, npc, player, wid, hei, dialogue_box_sprite = "immagini/utility/messagge.png"):
        self.lines = lines
        self.npc = npc
        self.player = player

        pos_x = wid - width/2
        pos_y = hei - padding - height
        
    


