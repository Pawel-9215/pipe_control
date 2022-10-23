import pygame
from pygame.locals import *
import sys

from settings import *
from support import lerp
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

        # for some reason linux and windows chave different mappings
        self.gamepad_mapping = 'b'
        self.gamepad_mappings = {'a':{'direction':0, 'acceleration':5, 'reverse':2},
                                'b':{'direction':0, 'acceleration':5, 'reverse':4}}

        # keyboard support
        self.keys_pressed = []

    def getaxes(self):
        start_y_debug = 32
        all_axes = self.gamepad.get_numaxes()

        # acceleration
        acc_pos = self.gamepad.get_axis(self.gamepad_mappings[self.gamepad_mapping]['acceleration'])
        if acc_pos > GAMEPAD_DEADZONE-1:
            acceleration = int(lerp(0, 255, ((acc_pos+1)/2)))
        else:
            acceleration = 0

        # reverse
        rev_pos = self.gamepad.get_axis(self.gamepad_mappings[self.gamepad_mapping]['reverse'])
        if rev_pos > GAMEPAD_DEADZONE-1:
            reverse = int(lerp(0, 255, ((rev_pos+1)/2)))
        else:
            reverse = 0

        # steering
        ster_pos = self.gamepad.get_axis(self.gamepad_mappings[self.gamepad_mapping]['direction'])
        if abs(ster_pos) > GAMEPAD_DEADZONE:
            steering = int(lerp(-255, 255, ((ster_pos+1)/2)))
        else:
            steering = 0

        axes = {'steering': steering, 'acceleration': acceleration, 'reverse': reverse}

        # debug(f"steering: {steering:>5}, acceleration: {acceleration:>5}, reverse: {reverse:>5}", y=15, x=15)

        return axes

    def keyboard_input(self):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and pygame.K_SPACE not in self.keys_pressed:
            self.keys_pressed.append(pygame.K_SPACE)
            if self.gamepad_mapping == 'a':
                self.gamepad_mapping = 'b'
            else:
                self.gamepad_mapping = 'a'
        elif not keys[pygame.K_SPACE] and pygame.K_SPACE in self.keys_pressed:
            self.keys_pressed.remove(pygame.K_SPACE)

    