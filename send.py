import socket
import sys
import json

host = sys.argv[1]  # ip of reciver
port = int(sys.argv[2])  # port 
host_name = socket.gethostname() 
ip = socket.gethostbyname(host_name) 
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
