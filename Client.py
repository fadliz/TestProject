import socket
server_address = ('localhost', 2120)

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect(server_address)

print("Pesan Sudah Terkirim")

f = open("Kirim_Fajari.txt", "rb")

try:
    byte = f.read(1)
    while byte != b'':
        socket_client.send(byte)
        byte = f.read(1)
finally:
    f.close()

    
