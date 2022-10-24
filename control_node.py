#this is a control node and server

import pygame
from pygame.locals import *
import sys
import socket
import pickle

import gamepad
from settings import *
from debug import debug
import hud


class Engine:
    """Main game class sitting on top of everything else
    """

    def __init__(self) -> None:

        #set the server
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        # general setup for pygameq
        self.screen = pygame.display.set_mode(RESOLUTION, HWSURFACE|DOUBLEBUF|RESIZABLE|SCALED)
        #self.clock = pygame.time.Clock()
        self.running = True
        pygame.display.set_caption(TITLE)

        #gamepad
        self.gamepad = gamepad.GamePad()
        self.axes_data = {'steering': 0, 'acceleration': 0, 'reverse': 0}

        #hud
        self.hud = hud.Hud(self.screen)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.screen.fill('#3D897B')
            if self.gamepad.gamepad_connected:
                self.axes = self.gamepad.getaxes()
            self.gamepad.keyboard_input()
            self.hud.draw_hud(self.axes)
            #debug(self.clock.get_fps())
            pygame.display.update()
            #self.clock.tick(FPS)

    def get_ip(self):
        my_ip = ""
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Is this your ip?: ")



    


if __name__ == '__main__':
    engine = Engine()
    engine.run()