import socket
import sys
import json
import os

port = int(sys.argv[1])  # initiate port no above 1024
server_socket = socket.socket() 
server_socket.bind(('', port))
os.system("rm -rf chats")
os.system("mkdir chats")
while True:
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    data = conn.recv(1024).decode()
    data = json.loads(data)
    chatline=" -->> "+data["content"]+"\n"
    print("\n"+data["ip"]+data["content"])
    file = open("chats/"+str(data["ip"]),'a') 
    file.write(chatline) 
    file.close() 
    conn.close()  # close the connection
