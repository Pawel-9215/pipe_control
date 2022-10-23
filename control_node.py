#this is a control node and server

import pygame
from pygame.locals import *
import sys
import gamepad

from settings import *
from debug import debug


class Engine:
    """Main game class sitting on top of everything else
    """

    def __init__(self) -> None:

        # general setup for pygameq
        self.screen = pygame.display.set_mode(RESOLUTION, HWSURFACE|DOUBLEBUF|RESIZABLE|SCALED)
        #self.clock = pygame.time.Clock()
        self.running = True
        pygame.display.set_caption(TITLE)

        #gamepad
        self.gamepad = gamepad.GamePad()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.screen.fill('#3D897B')
            if self.gamepad.gamepad_connected:
                self.gamepad.getaxes()
            self.gamepad.keyboard_input()
            
            #debug(self.clock.get_fps())
            pygame.display.update()
            #self.clock.tick(FPS)

    


if __name__ == '__main__':
    engine = Engine()
    engine.run()