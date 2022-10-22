import socket
import json
from json.decoder import JSONDecodeError
import datetime
import pickle

HEADERSIZE = 10
print('provide server ip or choose one from the list:\n')
server_ip = ""
port = 9998

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
client_sock.connect((server_ip, port))

def recieve_text_message():
    full_msg = ''
    new_msg = True
    while True:
        msg = client_sock.recv(16)
        if new_msg:
            print('new msg recieving:  ---  ', msg[:HEADERSIZE].decode('utf-8'))
            msg_len = int(msg[:HEADERSIZE])
            new_msg = False
            #print(f"new message len is --- {msg_len}")

        full_msg += msg.decode('utf-8')

        #print(full_msg)

        if len(full_msg) - HEADERSIZE == msg_len:
            #print("got full mesage")
            #print(full_msg)
            new_msg = True
            return full_msg

def send_data(my_data):
    msg = {"name": socket.gethostname(), "date": str(datetime.datetime.today()), "message": my_data}
    package = pickle.dumps(msg)
    package = bytes(f"{len(package):<{HEADERSIZE}}", 'utf-8')+package
    client_sock.send(package)

print(recieve_text_message())

while True:
    message = "All engines stop"
    send_data(message)