from Tkinter import *
l=[1,2,3,4,5]
k=[1,2,3,4,5]
rows = []
for i in l:
    cols = []
    for j in k:
        e = Entry(relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, '%d.%d' % (i, j))
        cols.append(e)
    rows.append(cols)

def onPress():
 	for row in rows:
        	for col in row:
           	 print col.get(),
       

Button(text='Fetch', command=onPress).grid()
mainloop()

