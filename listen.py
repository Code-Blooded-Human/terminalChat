#This Listens for new messages on a port.
#The data recivied is JSON Structured
# {"ip":,"content":}  
#ip-> ip address of node sending the message.
#content-> content of message 
#added directional arrow
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
    data = json.loads(data)
    chatline="-->>"+data["content"]+"\n"
    print(data["content"])
    file = open("chats.txt",'a') 
    file.write(chatline) 
    file.close() 
    conn.close()  # close the connection
