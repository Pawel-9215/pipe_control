import socket

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

while True:
    client_sock, address = server_sock.accept()
    print(f"connection from {address} established")
    client_sock.send(bytes("Welcome to the server", 'utf-8'))
    client_sock.send(bytes("New message", 'utf-8'))
    new_msg = client_sock.recv(1024)
    print(new_msg.decode('utf-8'))