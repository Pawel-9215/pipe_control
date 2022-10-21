import socket
import pickle
from struct import pack

HEADERSIZE = 10
my_ip = ""

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
my_ip = str(host_ip)
port = 9998

print(my_ip)

server_sock.bind((host_ip, port))
server_sock.listen(5)

client_sock, address = server_sock.accept()
print(f"connection from {address} established")

def send_text_message(message):
    message = f"{len(message):<{HEADERSIZE}}"+message
    client_sock.send(bytes(message, 'utf-8'))

send_text_message("Welcome to the server")

def recieve_data():
    package = b''
    new_input = True
    while True:
        buffer = client_sock.recv(16)
        if new_input:
            buffer_size = int(buffer[:HEADERSIZE])
            new_input = False

        package += buffer

        if len(package) - HEADERSIZE == buffer_size:
            return pickle.loads(package[HEADERSIZE:])

while True:
    incoming = recieve_data()
    print(f"{incoming['name']} | {incoming['date']} : \n {incoming['message']}")