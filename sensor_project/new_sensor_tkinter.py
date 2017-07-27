from Tkinter import *
import re
import Tkinter
import xml.etree.ElementTree as ET
import itertools
'''#!/usr/bin/python           # This is server.py file
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
port = 5557          # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)    
             # Now wait for client connection.
while True:
	c, addr = s.accept()     # Establish connection with client.
	print 'Got connection from', addr'''
class simpleapp_tk(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        
        self.initialize()
 
    def initialize(self):
        self.grid()
 
        frame = Frame(self, borderwidth=2, relief="sunken", width=1107, height=50)
        frame.grid(columnspan=3,row = 0)
 
        a = Label(frame,text = "Sensor_processing", fg = "red", font = 20)
        a.place(in_=frame, anchor="c", relx=.5, rely=.5)
        
        self.frame1 = Frame(self, borderwidth=2, relief="sunken", width = 1100, height=600)
        self.frame1.grid(column = 0,row = 1, sticky = "WN")
	self.k= Button(self.frame1,text="Waiting for connection",command=self.waitingfor_connection,fg="purple",font=15)
        self.k.place(in_=self.frame1,relx=.18,rely=.4)
       	self.button = Button(self.frame1, text="QUIT", fg="purple",command=quit)
        self.button.place(in_=self.frame1,relx=.67,rely=.23)
	#self.results=Label(self.frame1,text ="")
	#self.results.place(in_=self.frame1,relx=.1,rely=.6)
	self.Results = Label(self.frame1, text =" ")
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
	button = Button(self.frame1, text="Back", fg="purple",command=self.back)
        button.place(in_=self.frame1,relx=.45,rely=.8)
    def back(self):
	self.btn.destroy()
	self.Results.destroy()
    def waitingfor_connection(self):
	self.k.destroy()
	
	#self.btn = Button(self.frame1, text="MAC",command=self.Mac,fg="purple",font=15)
        #self.btn.place(in_=self.frame1,relx=.18,rely=.1	)
        #def Mac(self):
	tree = ET.parse('config.xml')
	root = tree.getroot()
	#print root.tag
	i = 0
	xml_list = []
	for child in root:
		xml_list.append(child.tag)
		xml_list.append(root[i].text)
	#	print dict(child.tag)
		i = i+1
	dct = dict(itertools.izip_longest(*[iter(xml_list)] * 2, fillvalue=""))
	for i in dct.keys():
	    v=dct[i]
	    k=v,i
	    print k
	    #r=Entry(self.frame1,height=20)
	    #r.pack()
	    #self.version_entry = Tkinter.Entry(self.frame)
            #self.version_entry.grid(row=1,column=1,padx=1, pady=1)
	    #self.Results = Label(self.frame1, text =k,font=15)
	    #self.Results.place(in_=self.frame1,relx=.33,rely=.1)
	    self.T = Text(self.frame1, height=2, width=30)
	    self.T.grid()
	    self.T.insert(END, k)
            #mainloop()
    	    
	    #userInput = Entry(self.frame1, width = 10) #the width refers to the number of characters
            #userInput.grid(row=0, column=0, padx=10, pady=2)

if __name__ == "__main__":
    sensor = simpleapp_tk(None)
    sensor.title('SENSOR')
    sensor.geometry("1107x650")
    sensor.mainloop()
 
