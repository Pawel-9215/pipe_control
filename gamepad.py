import pygame
from pygame.locals import *
import sys

from settings import *
from debug import debug


class GamePad():
    def __init__(self) -> None:

        if not pygame.joystick.get_init:
            pygame.joystick.init()
        if pygame.joystick.get_count() > 0:
            self.gamepad_connected = True
            self.gamepad = pygame.joystick.Joystick(0)
            print(self.gamepad.get_name())
            print(self.gamepad.get_numaxes())

        self.gamepad_mapping = 'a'
        self.gamepad_mappings = {'a':{'direction':0, 'acceleration':5, 'reverse':2},
                                'b':{'direction':0, 'acceleration':5, 'reverse':4}}

    def getaxes(self):
        start_y_debug = 32
        all_axes = self.gamepad.get_numaxes()

        for i in range(all_axes):
            debug(f"axin no: {i}, position: {self.gamepad.get_axis(i)}", y=start_y_debug+i*30, x=15)

    