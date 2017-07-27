import Tkinter
from Tkinter import *
import Tkinter
import xml.etree.ElementTree as ET
import itertools
#from TableModels import TableModel 
class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
	#self.initialize_user_interface()
        self.initialize()
	#self.pack()
    def initialize(self):
        self.grid()

	self.frame = Frame(self, borderwidth=2, relief="sunken", width=1107, height=48)
        self.frame.grid(columnspan=3,row = 0)

	act = Label(self.frame,text = "NEW_GUI_FOR _INTEL", fg = "red", font = 20)
        act.place(in_=self.frame, anchor="c", relx=.5, rely=.5)
        btn2= Button(self.frame, text="QUIT", fg="purple",font=15,command=quit)
#        btn2.grid(row=3,column=1)
	btn2.place(in_=self.frame,relx=.8,rely=.2)
	self.frame1 = Frame(self, borderwidth=2, relief="sunken", width = 300, height=600)
        self.frame1.grid(column = 0,row = 1, sticky = "WN")
 	self.k= Button(self.frame1,text="Waiting for connection",command=self.waitingfor_connection,fg="purple",font=15)
        self.k.place(in_=self.frame1,relx=.18,rely=.4)
	#btn = Button(self.frame1, text="Logfile", fg="purple",font=15)
	#btn.place(in_=self.frame1,relx=.9,rely=.2)
     
	self.frame2=Frame(self,borderwidth=2,relief="sunken",width=798,height=600)
	self.frame2.grid(column = 1,row = 1, sticky = "WN")
	self.frame3 = Frame(self.frame2, borderwidth=2, relief="sunken", width = 300, height=600)
        self.frame3.place(column = 0,row = 1, sticky = "WN")
	#self.T=Text(self.frame2, borderwidth=1,relief="sunken",width=90,height=10)
	#self.T.place(in_=self.frame2)
	self.T = Text(self.frame2, height=12, width=43)
	self.T.pack()
	self.f=Button(self.T,text="click_to_proceed",fg="purple",font=15,command=self.click_to_proceed)
	self.f.place(in_=self.T,anchor="center",relx=.5,rely=.9)
	#self.T = Text(self.frame2, height=2, width=23)
	
	#self.T.insert(END, k)

    def waitingfor_connection(self):
	self.k.destroy()
	#self.frame3.destroy()
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
	    print k,type(k)
	    self.T.insert(END,k)
	    self.T.insert(END,'\n')
    def click_to_proceed(self):
            #height = 5
	    #width = 5
            #for i in range(height): #Rows
    		#for j in range(width): #Columns
                	#self.b = Entry(self.frame2, text="")
        		#self.b.grid(row=i, column=j)
	    '''l=[1,2,3,4,5]
	    k=[1,2,3,4,5]
	    rows = []
	    for i in l:
    		cols = []
    		for j in k:
        		e = Entry(relief=RIDGE)
        		e.grid(row=i, column=j,)
        		#e.insert(END, '%d.%d' % (i, j))
        	        cols.append(e)
    	    rows.append(cols)'''
	    self.frame3 = Frame(self.frame2, borderwidth=2, relief="sunken", width = 300, height=600)
            self.frame3.place(column = 0,row = 1, sticky = "WN")
            #self.frame2.title("RESULTS")   
	    self.act = Label(self.frame3,text = "RESULTS", fg = "red", font = 20)
            self.act.place(in_=self.frame3, anchor="c", relx=.5, rely=.5)    
            #self.frame2.grid_rowconfigure(0,weight=1)
            #self.frame2.grid_columnconfigure(0,weight=1)
            #self.frame2.config(background="lavender")
	    '''l=[1,2,3,4]
	    k=[6,7,8,9]

        # Define the different GUI widgets
	    for i in l:
        	self.dose_label = Tkinter.Label(self.parent, text = "Dose:")
        	self.dose_entry = Tkinter.Entry(self.parent)
		print i
		self.dose_entry.insert(i, '%d' %(i))
        	self.dose_label.grid(row = 0, column = 0, sticky = Tkinter.W)
        	self.dose_entry.grid(row = 0, column = 1)
	    for k in k:
        	self.modified_label = Tkinter.Label(self.parent, text = "Date Modified:")
        	self.modified_entry = Tkinter.Entry(self.parent)
        	self.modified_label.grid(row = 1, column = 0, sticky = Tkinter.W)
        	self.modified_entry.grid(row = 1, column = 1)
		self.modified_entry.insert(k,'%d'%(k))
            self.submit_button = Tkinter.Button(self.parent, text = "Insert", command = self.insert_data)
            self.submit_button.grid(row = 2, column = 1, sticky = Tkinter.W)
            self.exit_button = Tkinter.Button(self.parent, text = "Exit", command = self.parent.quit)
            self.exit_button.grid(row = 0, column = 3)

        # Set the treeview
            self.tree = ttk.Treeview( self.parent, columns=('Sensor_hub', 'Sensor_List','output'))
            self.tree.heading('#0', text='Sensor_hub')
            self.tree.heading('#1', text='Sensor_List')
            self.tree.heading('#2', text='expectedoutput')
	    self.tree.heading('#3', text='output')
            self.tree.column('#1', stretch=Tkinter.YES)
            self.tree.column('#2', stretch=Tkinter.YES)
            self.tree.column('#0', stretch=Tkinter.YES)
	    self.tree.column('#3', stretch=Tkinter.YES)
            self.tree.grid(row=5, columnspan=5, sticky='nsew')
            self.treeview = self.tree
        # Initialize the counter
            self.i = 0


    def insert_data(self):
        """
        Insertion method.
        """
	l=[1,2,3,4]
	for i in l:
		self.treeview.insert('', 'end', text=str(self.i), values=(self.dose_entry.get(), self.modified_entry.get()))
        # Increment counter
        	self.i = self.i + 1
		print self.i'''




	
    def OnButtonClick(self):
	pass
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('INTEL')
    app.geometry("1107x650")
    app.mainloop()
    
