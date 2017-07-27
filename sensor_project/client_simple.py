#!/usr/bin/python           # This is client.py file

import socket 
import time

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 5557               # Reserve a port for your service.

s.connect((host, port))
cmd = s.recv(1024)  # cmd is received
print 'cmd received',cmd

#time.sleep(120)
 

s.close()
#s.close                     # Close the socket when done
