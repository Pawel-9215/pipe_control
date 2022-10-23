import pygame

from settings import *
from support import *

class Hud():
    def __init__(self, surface) -> None:
        self.client_name = "No client connected"
        self.screen = surface
        self.margins = 20
        self.bar_width = 16
        self.vertical_h = RESOLUTION[1] // 3
        self.border_thickness = 3


    def draw_acc(self, acc=0):
        pos_x = RESOLUTION[0] - self.bar_width - self.margins
        pos_y = RESOLUTION[1] - self.vertical_h - self.margins
        pygame.draw.rect(self.screen, 'white', (pos_x, pos_y, self.bar_width, self.vertical_h), width=self.border_thickness)

    def draw_hud(self):
        self.draw_acc()