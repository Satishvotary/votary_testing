from Tkinter import *
import re
import Tkinter
import xml.etree.ElementTree as ET
import itertools
import ttk
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
	self.frame11 = Frame(self, borderwidth=2, relief="sunken", width = 200, height=60)
        self.frame11.grid(column = 0,row = 1, sticky = "WN")
	self.frame12 = Frame(self, borderwidth=2, relief="sunken", width = 100, height=60)
        self.frame12.grid(column = 0,row = 1, sticky = "NE")
	self.frame13= ttk.Frame(self.frame12)
	self.frame13.pack()
        
	self.k= Button(self.frame1,text="Waiting for connection",command=self.waitingfor_connection,fg="purple",font=15)
        self.k.place(in_=self.frame1,relx=.18,rely=.4)
       	self.button = Button(self.frame1, text="QUIT", fg="purple",command=quit)
        self.button.place(in_=self.frame1,relx=.87,rely=.23)
	self.button = Button(self.frame11, text="QUIT", fg="purple",command=quit)
        self.button.place(in_=self.frame11,relx=.8,rely=.2)
	#self.results=Label(self.frame1,text ="")
	#self.results.place(in_=self.frame1,relx=.1,rely=.6)
	self.Results = Label(self.frame1, text =" ")
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
	button = Button(self.frame1, text="Back", fg="purple",command=self.back)
        button.place(in_=self.frame1,relx=.45,rely=.8)
    def back(self):
	self.frame11.destroy()
	#self.Results.destroy()
	tree = ET.parse('config.xml')
	root = tree.getroot()
	
	#self.b.grid(row=i, column=j)
	
	#print root.tag
	i = 0
	xml_list = []
	for child in root:
		xml_list.append(child.tag)
		xml_list.append(root[i].text)
	#	print dict(child.tag)
		i = i+1
	dct = dict(itertools.izip_longest(*[iter(xml_list)] * 2, fillvalue=""))
       	l=dct.keys()
	k=dct.values()
	'''for i in range(len(l)):
    		for j in range(len(k)):
        		l = Label(self.frame12,text='%s.%s' % (l[i], k[j]), relief=RIDGE)
        		l.grid(row=i, column=j, sticky=NSEW)
			print l[i],k[j]'''
	tree=ttk.Treeview(self.frame12)

	style = ttk.Style()
	style.configure(".", font = ("Helvetica", 14))
	style.configure("Treeview.Heading", font = ("Helvetica", 16) )

	tree["columns"] = ("one", "two", "three", "four")
	tree.column("one", width=170)
	tree.column("two", width=255)
	tree.column("three", width=510)
	tree.column("four", width=85)

	tree.heading('#0', text = "Type")
	tree.heading("one", text = "Category")
	tree.heading("two", text = "Display Name")
	tree.heading("three", text = "GUID")
	tree.heading("four", text = "Delete")

	tree.insert("" , 0,    text = "Line 1", values = ("1A","1b"), tag = "orow")
    def waitingfor_connection(self):
	self.k.destroy()
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
	    self.T = Text(self.frame11, height=2, width=23)
	    self.T.pack()
	    self.T.insert(END, k)
    	    
if __name__ == "__main__":
    sensor = simpleapp_tk(None)
    sensor.title('SENSOR')
    sensor.geometry("1107x650")
    sensor.mainloop()
 
