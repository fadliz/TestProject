import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 2120)
socket_server.bind(server_address)
socket_server.listen(1)

print("sedang menunggu sambugan")

f = open("Terima_Fajari.txt", "wb")

conn, addr = socket_server.accept()

while True:
    data = conn.recv(1024)
    f.write(data)
    if not data :
        break
    
    
