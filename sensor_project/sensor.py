from Tkinter import *
import re
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
	self.k= Button(self.frame1,text="Click here to send command",command=self.Click_heretosendcommand,fg="purple",font=15)
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
	self.btn1.destroy()                                   
	self.btn2.destroy() 
	self.btn3.destroy() 
	self.btn4.destroy()
	self.acc1.destroy()                                   
	self.acc2.destroy() 
	self.acc3.destroy()
	self.gyr1.destroy()                                   
	self.gyr2.destroy() 
	self.gyr3.destroy()
	self.mag1.destroy()                                   
	self.mag2.destroy() 
	self.mag3.destroy()
	self.gps1.destroy()                                   
	self.gps2.destroy()
	self.Results.destroy() 
	#self.button.destroy()
    def Click_heretosendcommand(self):
	self.k.destroy()
	
	self.btn = Button(self.frame1, text="sensors_list",command=self.sensors_list,fg="purple",font=15)
        self.btn.place(in_=self.frame1,relx=.18,rely=.1)
    def sensors_list(self):
        print "sensors_list"
	#self.btn.destroy()
	self.btn1 = Button(self.frame1, text="Accelerometer",command=self.Acceleromter,fg="purple",font=15)
        self.btn1.place(in_=self.frame1,relx=.18,rely=.2)
	self.btn2 = Button(self.frame1, text="Gyroscope",command=self.Gyroscope,fg="purple",font=15)
        self.btn2.place(in_=self.frame1,relx=.18,rely=.3)
	self.btn3 = Button(self.frame1, text="Magnetometer",command=self.magnetometer,fg="purple",font=15)
        self.btn3.place(in_=self.frame1,relx=.18,rely=.4)
	self.btn4 = Button(self.frame1, text="Gps",command=self.Gps,fg="purple",font=15)
        self.btn4.place(in_=self.frame1,relx=.18,rely=.5)
	self.Results.destroy()
	
	#btn = Button(self.frame1, text="Back",fg="purple",font=15)
       #btn.place(in_=self.frame1,relx=12,rely=5)
	#btn.pack()
    def Acceleromter(self):
	print "Accelerometer"
	self.acc1 = Button(self.frame1, text="X",command=self.X,fg="purple",font=15)
        self.acc1.place(in_=self.frame1,relx=.32,rely=.2)
	self.acc2 = Button(self.frame1, text="Y",command=self.Y,fg="purple",font=15)
        self.acc2.place(in_=self.frame1,relx=.36,rely=.2)
	self.acc3 = Button(self.frame1, text="Z",command=self.Z,fg="purple",font=15)
        self.acc3.place(in_=self.frame1,relx=.40,rely=.2)
	
    def X(self):
	
	print "Accele"
	fh=open("/home/ravuljyo/Downloads/scripts/file1.txt",'r')
	l=[]
	k=[]
	l=fh
	for i in l:
		if re.match("ACC X", i):
		       k.append(i)
	#self.results.destroy()
	self.Results.destroy()
	#self.results=Label(self.frame1,text ="X value")
	#self.results.place(in_=self.frame1,relx=.1,rely=.6)
	self.Results = Label(self.frame1, text =k[0])
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
    def Y(self):
	#self.results.destroy()
	self.Results.destroy()
	print "Accele_Y"
	fh=open("/home/ravuljyo/Downloads/scripts/file1.txt",'r')
	l=[]
	l=fh
	k=[]
	for i in l:
		if re.match("ACC Y", i):
			k.append(i)
	print k
	#self.results=Label(self.frame1,text ="Y value")
	#self.results.place(in_=self.frame1,relx=.2,rely=.6)
	self.Results = Label(self.frame1, text =k[0])
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
	
    def Z(self):
	#self.results.destroy()
	self.Results.destroy()
	print "Accele_Z"
	fh=open("/home/ravuljyo/Downloads/scripts/file1.txt",'r')
	l=[]
	l=fh
	k=[]
	for i in l:
		if re.match("ACC Z", i):
			k.append(i)
	print k
	#self.results=Label(self.frame1,text ="Z value")
	#self.results.place(in_=self.frame1,relx=.3,rely=.6)
	self.Results = Label(self.frame1, text =k[0])
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
    def Gyroscope(self):
	'''self.results=Label(self.frame1,text ="  ")
	self.results.place(in_=self.frame1,relx=.3,rely=.6)
	self.Results = Label(self.frame1, text =" ")
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)'''
	#self.results.destroy()
	self.Results.destroy()
	print "Gyroscope"
	self.gyr1 = Button(self.frame1, text="GyroX",command=self.GyroX,fg="purple",font=15)
        self.gyr1.place(in_=self.frame1,relx=.28,rely=.3)
	self.gyr2 = Button(self.frame1, text="GyroY",command=self.GyroY,fg="purple",font=15)
        self.gyr2.place(in_=self.frame1,relx=.36,rely=.3)
	self.gyr3 = Button(self.frame1, text="GyroZ",command=self.GyroZ,fg="purple",font=15)
        self.gyr3.place(in_=self.frame1,relx=.42,rely=.3)
	#self.results=Label(self.frame1,text ="")
	#self.results.place(in_=self.frame1,relx=.1,rely=.6)
	self.Results = Label(self.frame1, text =" ")
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
    def GyroX(self):
	
	print "Accele"
	fh=open("/home/ravuljyo/Downloads/scripts/file1.txt",'r')
	l=[]
	k=[]
	l=fh
	for i in l:
		if re.match("Gyro X", i):
		       k.append(i)
	#self.results.destroy()
	self.Results.destroy()
	#self.results=Label(self.frame1,text ="X value")
	#self.results.place(in_=self.frame1,relx=.1,rely=.6)
	self.Results = Label(self.frame1, text =k[0])
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
    def GyroY(self):
	#self.results.destroy()
	self.Results.destroy()
	print "Gyro Y"
	fh=open("/home/ravuljyo/Downloads/scripts/file1.txt",'r')
	l=[]
	l=fh
	k=[]
	for i in l:
		if re.match("Gyro Y", i):
			k.append(i)
	print k
	#self.results=Label(self.frame1,text ="Y value")
	#self.results.place(in_=self.frame1,relx=.2,rely=.6)
	self.Results = Label(self.frame1, text =k[0])
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
	
    def GyroZ(self):
	#self.results.destroy()
	self.Results.destroy()
	print "Gyro Z"
	fh=open("/home/ravuljyo/Downloads/scripts/file1.txt",'r')
	l=[]
	l=fh
	k=[]
	for i in l:
		if re.match("Gyro Z", i):
			k.append(i)
	print k
	#self.results=Label(self.frame1,text ="Z value")
	#self.results.place(in_=self.frame1,relx=.3,rely=.6)
	self.Results = Label(self.frame1, text =k[0])
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
    def magnetometer(self):
	print "Magnetometer"
	self.mag1 = Button(self.frame1, text="X",command = self.MagX,fg="purple",font=15)
        self.mag1.place(in_=self.frame1,relx=.32,rely=.4)
	self.mag2 = Button(self.frame1, text="Y",command = self.MagY,fg="purple",font=15)
        self.mag2.place(in_=self.frame1,relx=.40,rely=.4)
	self.mag3 = Button(self.frame1, text="Z",command = self.MagZ,fg="purple",font=15)
        self.mag3.place(in_=self.frame1,relx=.46,rely=.4)
	self.Results.destroy()
    def MagX(self):
	self.Results.destroy()
	fh=open("/home/ravuljyo/Downloads/scripts/file1.txt",'r')
	l=[]
	l=fh
	k=[]
	for i in l:
		if re.match("Mag X", i):
			k.append(i)
	print k
	#self.results=Label(self.frame1,text ="Z value")
	#self.results.place(in_=self.frame1,relx=.3,rely=.6)
	self.Results = Label(self.frame1, text =k[0])
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
    def MagY(self):
	self.Results.destroy()
	fh=open("/home/ravuljyo/Downloads/scripts/file1.txt",'r')
	l=[]
	l=fh
	k=[]
	for i in l:
		if re.match("Mag Y", i):
			k.append(i)
	print k
	#self.results=Label(self.frame1,text ="Z value")
	#self.results.place(in_=self.frame1,relx=.3,rely=.6)
	self.Results = Label(self.frame1, text =k[0])
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
    def MagZ(self):
	self.Results.destroy()
	fh=open("/home/ravuljyo/Downloads/scripts/file1.txt",'r')
	l=[]
	l=fh
	k=[]
	for i in l:
		if re.match("Mag Z", i):
			k.append(i)
	print k
	#self.results=Label(self.frame1,text ="Z value")
	#self.results.place(in_=self.frame1,relx=.3,rely=.6)
	self.Results = Label(self.frame1, text =k[0])
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
    def Gps(self):
	print "Gps"
	self.Results.destroy()
	self.gps1 = Button(self.frame1, text="Latitude",command=self.Latitude,fg="purple",font=15)
        self.gps1.place(in_=self.frame1,relx=.32,rely=.5)
	self.gps2 = Button(self.frame1, text="Longitude",command=self.Longitude,fg="purple",font=15)
        self.gps2.place(in_=self.frame1,relx=.44,rely=.5)
	'''T = Text(self.frame1,height=5,width=30)
	T.place(in_=self.frame1,relx=.28,rely=.6)
        T.insert(END,"xvalue:")
	T.insert(END,fh.read())
	fh.close()'''
    def Latitude(self):
	self.Results.destroy()
	fh=open("/home/ravuljyo/Downloads/scripts/file1.txt",'r')
	l=[]
	l=fh
	k=[]
	for i in l:
		if re.match("latitude",i):
			k.append(i)
	print k
	self.Results=Label(self.frame1,text=k[0])
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
    def Longitude(self):
	self.Results.destroy()
	fh=open("/home/ravuljyo/Downloads/scripts/file1.txt",'r')
	l=[]
	l=fh
	k=[]
	for i in l:
		if re.match("longitude",i):
			k.append(i)
	print k
	self.Results=Label(self.frame1,text=k[0])
	self.Results.place(in_=self.frame1,relx=.35,rely=.6)
   	
if __name__ == "__main__":
    sensor = simpleapp_tk(None)
    sensor.title('SENSOR')
    sensor.geometry("1107x650")
    sensor.mainloop()
 
