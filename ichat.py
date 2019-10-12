import os
import sys


port=sys.argv[1]
os.system("python listen.py "+str(port)+" &")

while True:
    os.system("clear")
   
    os.system("ls  chats")
 
    inp=raw_input()
    if inp == "rr":
        continue
    if inp == "cc":
        ip=raw_input("Enter ip of host")
        mess=raw_input("Enter greeting message")
        os.system("echo \""+mess+"\" | python send.py "+str(ip)+" "+str(port))
        continue
    if inp == "ll":
        ip=raw_input("enter ip of host")
        while True:
            os.system("clear")
            os.system("cat chats/"+ip)
            inp2=raw_input(" Enter message to send, or ee to exit")
            if inp2 == "ee":
                break
            os.system("echo \""+inp2+"\" | python send.py "+str(ip)+" "+str(port))
        continue
                
