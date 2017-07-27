import Tkinter
from Tkinter import *
class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
	#self.pack()
    def initialize(self):
        self.grid()

	self.frame = Frame(self, borderwidth=2, relief="sunken", width=1107, height=48)
        self.frame.grid(columnspan=3,row = 0)

	act = Label(self.frame,text = "ANDROID COMMAND TOOL", fg = "red", font = 20)
        act.place(in_=self.frame, anchor="c", relx=.5, rely=.5)
        btn2= Button(self.frame, text="QUIT", fg="purple",font=15,command=quit)
#        btn2.grid(row=3,column=1)
	btn2.place(in_=self.frame,relx=.8,rely=.2)
	self.frame1 = Frame(self, borderwidth=2, relief="sunken", width = 300, height=600)
        self.frame1.grid(column = 0,row = 1, sticky = "WN")
 	self.k= Button(self.frame1,text="Waiting for connection",fg="purple",font=15)
        self.k.place(in_=self.frame1,relx=.18,rely=.4)
	#btn = Button(self.frame1, text="Logfile", fg="purple",font=15)
	#btn.place(in_=self.frame1,relx=.9,rely=.2)
     
	self.frame11 = Frame(self.frame1, borderwidth=1, relief="sunken", width = 300, height=700)
        self.frame11.grid(row=1)
	
	self.t=Text(self.frame11, borderwidth=1,bg='CadetBlue1',relief="sunken",width=90,height=27)
	self.t.place(in_=self.frame11)
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('ACT')
    app.geometry("1107x650")
    app.mainloop()
    
