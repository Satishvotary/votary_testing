#!/usr/bin/python           # This is server.py file
import socket               # Import socket module
import json
from ctypes import cdll
import os
#from Tkinter import *
import sensor as sk
from sensor import *
#os.system('python sensor.py')

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 5555           # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)    
             # Now wait for client connection.
while True:
	c, addr = s.accept()     # Establish connection with client.
	print 'Got connection from', addr
	
	pk=sk.simpleapp_tk(None)
	pk.k.bind("<1>", c.send("hi"))
	pk.mainloop()
	
	

	'''with open('data.json','r') as f:
		dct = json.load(f) #will reults in dict format
		lst = dct.values() #will results in list format
		ip1 = str(lst[0])
		ip2 = str(lst[1])
		c.send(ip1)
		#print 'cmd sent'
		data = c.recv(4096)
		#print 'file buf reveived'
		fp = open('file.txt','a')
		fp.write(ip2)
		fp.write('\n')
		fp.write(data)
		fp.close()
		#print 'file written completed'
		stdc=cdll.LoadLibrary("libc.so.6")  #library for c
		stdcpp=cdll.LoadLibrary("libstdc++.so.6")
		obj = cdll.LoadLibrary("/home/kathirah/Desktop/source code/py2c/libproj.so")
		obj.main()'''
		
		#c.close()                # Close the connection
