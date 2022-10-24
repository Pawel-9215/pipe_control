import socket
import json
from json.decoder import JSONDecodeError
import datetime
import pickle

from settings import *
from support import *
import camera_01
import servo_control

import pygame
from pygame.locals import *
import sys

print('provide server ip or choose one from the list:\n')
server_ip = ""
port = PORT

pygame.init()

with open("./server_data.json", "r") as server_data_read:
    try:
        server_data = json.load(server_data_read)
        for no, known_server in enumerate(server_data.keys()):
            print(f"{known_server} adress: {server_data[known_server]}")
            last_server = no
        user_choice = input()
        if user_choice in server_data.keys():
            server_ip = server_data[user_choice]
        elif user_choice in server_data.values():
            server_ip = user_choice
        else:
            server_ip = user_choice
            server_data[str(last_server+1)] = user_choice
            #json.dump(server_data, server_data_write)


    except JSONDecodeError:
        server_data = {}
        print("no server adresses in memory, please provide server ip adress")
        server_data[0] = input()
        server_ip = server_data[0]
        #json.dump(server_data, server_data_write)

with open("./server_data.json", "w") as server_data_write:
    json.dump(server_data, server_data_write)

print(f"Connecting to server {server_ip}")


client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((server_ip, PORT))

def send_data(my_data):
    msg = my_data
    package = pickle.dumps(msg)
    package = bytes(f"{len(package):<{HEADERSIZE}}", 'utf-8')+package
    client_sock.send(package)

def recieve_data():
    package = b''
    new_input = True
    while True:
        buffer = client_sock.recv(DATA_CHUNK)
        if new_input:
            buffer_size = int(buffer[:HEADERSIZE])
            new_input = False

        package += buffer

        if len(package) - HEADERSIZE == buffer_size:
            return pickle.loads(package[HEADERSIZE:])

print(recieve_data()['message'])

if camera_01.camera_initiaized:
    camera_image = camera_01.get_frame()
    print('camera ok')
else:
    camera_image = 'no cam'
    print('camera not ok')

while True:
    
    if camera_01.camera_initiaized:
        camera_image = camera_01.get_frame()
    else:
        camera_image = 'no cam'
        # print('camera not ok')
    send_data({'cam_feed': camera_image})
    incoming = recieve_data()
    servo_control.set_input_params(incoming)
    """for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()"""
