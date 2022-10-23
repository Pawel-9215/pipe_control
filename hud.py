import pygame

from settings import *
from support import *
from debug import debug

class Hud():
    def __init__(self, surface) -> None:
        self.client_name = "No client connected"
        self.screen = surface
        self.margins = 20
        self.bar_width = 16
        self.vertical_h = 255 # RESOLUTION[1] // 3
        self.border_thickness = 3


    def draw_acc(self, acc=0):
        pos_x = RESOLUTION[0] - self.bar_width - self.margins
        pos_y = RESOLUTION[1] - self.vertical_h - self.margins

        pygame.draw.rect(self.screen, 'white', (pos_x, pos_y+255-acc, self.bar_width, self.vertical_h-255+acc))
        pygame.draw.rect(self.screen, 'white', (pos_x, pos_y, self.bar_width, self.vertical_h), width=self.border_thickness)

        pygame.draw.line(self.screen, 'yellow', (pos_x-15, pos_y+255-acc), (pos_x+self.bar_width, pos_y+255-acc), 2)

        debug(acc, pos_y + 215, pos_x - 35) 


    def draw_hud(self, axes_data):
        self.draw_acc(axes_data['acceleration'])