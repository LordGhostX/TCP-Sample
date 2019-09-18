# client.py

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
name = input('welcome, client name >> ')
try:
    while True:
        # Send data
        message = "[ * ] " + name.upper() + " >> " + input("[ * ] " + name.upper() + " >> ")
        sock.sendall(message.encode('utf-8'))

        # Look for the response
        # amount_received = 0
        # amount_expected = len(message)

        data = sock.recv(4096)
        if len(data.decode()) > 0:
            print(data.decode())
        else:
            print('no data')
            break

finally:
    print('closing socket')
    sock.close()
    exit()

