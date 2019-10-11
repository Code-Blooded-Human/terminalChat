#sends data to a ip address and port

import socket
import sys


host = sys.argv[1]  # ip of reciver
port = int(sys.argv[2])  # port 
ip="127.0.0.1"
client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

message = raw_input("")  # take input

client_socket.send(message.encode())  # send message


client_socket.close()  # close the connection
