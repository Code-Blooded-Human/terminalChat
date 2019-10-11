#This Listens for new messages on a port and displays it on terminal.

import socket
import sys
import json
import os

port = int(sys.argv[1])  # initiate port no above 1024
server_socket = socket.socket() 
server_socket.bind(('', port))

while True:
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    data = conn.recv(1024).decode()
    print(str(data))
    conn.close()  # close the connection
