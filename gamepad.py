import pygame
from pygame.locals import *
import sys

from settings import *
from debug import debug


class Engine:
    """Main game class sitting on top of everything else
    """

    def __init__(self) -> None:

        # general setup for pygameq
        self.screen = pygame.display.set_mode(RESOLUTION, HWSURFACE|DOUBLEBUF|RESIZABLE|SCALED)
        self.clock = pygame.time.Clock()
        self.running = True

        pygame.display.set_caption(TITLE)

        #gamepad
        print(pygame.joystick.get_count())
        self.gamepad = pygame.joystick.Joystick(0)
        print(self.gamepad.get_name())
        print(self.gamepad.get_numaxes())

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.screen.fill('#3D897B')
            self.getaxes()
            
            debug(self.clock.get_fps())
            pygame.display.update()
            self.clock.tick(FPS)

    def getaxes(self):
        start_y_debug = 32
        all_axes = self.gamepad.get_numaxes()

        for i in range(all_axes):
            debug(f"axin no: {i}, position: {self.gamepad.get_axis(i)}", y=start_y_debug+i*30, x=15)


if __name__ == '__main__':
    game = Engine()
    game.run()