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
        self.server_ip = self.get_ip()
        self.server_sock.bind((self.server_ip, PORT))

        print('awaiting connection...')
        self.server_sock.listen(5)
        self.client_sock, self.address = self.server_sock.accept()
        print(f"connection from {self.address} established")

        self.send_data({'message': "Welcome to the server"})

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
        self.hud.client_name = self.address

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.screen.fill('#3D897B')
            if self.gamepad.gamepad_connected:
                self.axes_data = self.gamepad.getaxes()
            self.gamepad.keyboard_input()
            self.display_feed(self.recieve_data())
            self.hud.draw_hud(self.axes_data)
            self.send_data(self.axes_data)
            #debug(self.clock.get_fps())
            pygame.display.update()
            #self.clock.tick(FPS)

    def get_ip(self):
        my_ip = ""
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        answer = ''
        while answer not in ['y', 'n']:
            answer = print(f"Is this your ip? [y/n]: {host_ip}")
            answer = input()
        if answer == 'y':
            my_ip = host_ip
            return my_ip
        elif answer == 'n':
            print('provide your ip:')
            answer = input()
            my_ip = answer
        return my_ip

    def recieve_data(self):
        package = b''
        new_input = True
        while True:
            buffer = self.client_sock.recv(DATA_CHUNK)
            if new_input:
                buffer_size = int(buffer[:HEADERSIZE])
                new_input = False

            package += buffer

            if len(package) - HEADERSIZE == buffer_size:
                return pickle.loads(package[HEADERSIZE:])

    def send_data(self, my_data: dict):
        msg = my_data
        package = pickle.dumps(msg)
        package = bytes(f"{len(package):<{HEADERSIZE}}", 'utf-8')+package
        self.client_sock.send(package)

    def display_feed(self, feed):

        all_data = feed
        #self.screen.fill('black')
        # print(all_data)
        img = pygame.image.fromstring(all_data['cam_feed'], 
                                     (640, 480),
                                     'RGB')
        #img_scaled = pygame.Surface(RESOLUTION)
        img_scaled = pygame.transform.scale(img, RESOLUTION)

        self.screen.blit(img_scaled, (0,0))

if __name__ == '__main__':
    engine = Engine()
    engine.run()