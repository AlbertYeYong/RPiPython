#!/usr/bin/python3

# usage:  python3 tcpClt2.py 192.168.1.123
#              exit    to quit

import sys
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) == 1:
    host = socket.gethostbyname('localhost')
else:
    host = socket.gethostbyname(sys.argv[1])

port = 5150

print('enter text ''exit'' to quit')

server.connect((host, port))
data = server.recv(1024)
print(bytes.decode(data))
while True:
    data = input('Enter text to send:')
    server.send(str.encode(data))
    data = server.recv(1024)
    print('Received from server:', bytes.decode(data))
    if (bytes.decode(data) == 'exit'):
        break
print('Closing connection')
server.close()
