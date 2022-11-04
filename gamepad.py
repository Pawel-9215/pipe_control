import pygame
from pygame.locals import *
import sys

from settings import *
from support import *
from support import lerp
from debug import debug


class GamePad():
    def __init__(self) -> None:

        # smooth movement
        self.current_steering = 0
        self.current_acceleration = 0
        self.current_reverse = 0
        self.uni_step = 20

        if not pygame.joystick.get_init:
            pygame.joystick.init()
        if pygame.joystick.get_count() > 0:
            self.gamepad_connected = True
            self.gamepad = pygame.joystick.Joystick(0)
            print(self.gamepad.get_name())
            print(self.gamepad.get_numaxes())
        else:
            self.gamepad_connected = False
            print("no gamepad detected!")

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
        
        self.current_steering = move_towards(self.current_steering, steering, self.uni_step, self.uni_step*2)
        self.current_acceleration = move_towards(self.current_acceleration, acceleration, self.uni_step, self.uni_step*2)
        self.current_reverse = move_towards(self.current_reverse, reverse, self.uni_step, self.uni_step*2)

        axes = {'steering': self.current_steering, 'acceleration': self.current_acceleration, 'reverse': self.current_reverse}

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

    