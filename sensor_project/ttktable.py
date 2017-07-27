import Tkinter
import ttk



class Begueradj(Tkinter.Frame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        self.parent.title("RESULTS")       
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")
	l=[1,2,3,4]
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
		print self.i






def main():
    root=Tkinter.Tk()
    d=Begueradj(root)
    root.mainloop()

if __name__=="__main__":
    main()
