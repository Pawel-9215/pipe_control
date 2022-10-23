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

        debug(f"{acc:03d}", pos_y + 255 - 26, pos_x - 45)

    def draw_rev(self, dec=0):
        pos_x = 0 + self.margins
        pos_y = RESOLUTION[1] - self.vertical_h - self.margins

        pygame.draw.rect(self.screen, 'white', (pos_x, pos_y+255-dec, self.bar_width, self.vertical_h-255+dec))
        pygame.draw.rect(self.screen, 'white', (pos_x, pos_y, self.bar_width, self.vertical_h), width=self.border_thickness)

        pygame.draw.line(self.screen, 'yellow', (pos_x, pos_y+255-dec), (pos_x+self.bar_width+15, pos_y+255-dec), 2)

        debug(f"{dec:03d}", pos_y + 255 - 26, pos_x + self.bar_width + 5)

    def draw_ster(self, ster=0):
        pos_x = RESOLUTION[0] // 2 - 255
        pos_y = RESOLUTION[1] - self.bar_width - self.margins

        if ster>0:
            pygame.draw.rect(self.screen, 'white', (RESOLUTION[0] // 2, pos_y, ster, self.bar_width))
        else:
            pygame.draw.rect(self.screen, 'white', (RESOLUTION[0] // 2 + ster, pos_y, -ster, self.bar_width))
        pygame.draw.rect(self.screen, 'white', (pos_x, pos_y, 255*2, self.bar_width), width=self.border_thickness)

        pygame.draw.line(self.screen, 'yellow', (RESOLUTION[0] // 2 + ster, pos_y), (RESOLUTION[0] // 2 + ster, pos_y+32), 2)

        debug(f"{abs(ster):03d}", pos_y - 31, RESOLUTION[0] // 2 - 21)


        

    def draw_hud(self, axes_data):
        self.draw_acc(axes_data['acceleration'])
        self.draw_rev(axes_data['reverse'])
        self.draw_ster(axes_data['steering'])
        debug(self.client_name, self.margins, self.margins)