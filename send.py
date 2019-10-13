import socket
import sys
import json
import os

host = sys.argv[1]  # ip of reciver
port = int(sys.argv[2])  # port 

ip = os.popen("hostname -I | awk '{print $1}'").read()




client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

message = raw_input("")  # take input
file = open("chats/"+host ,"a")
file.write("<<--"+message+"\n")
file.close()

data={"ip":ip,"content":message}
data=json.dumps(data)
client_socket.send(data.encode())  # send message


client_socket.close()  # close the connection
