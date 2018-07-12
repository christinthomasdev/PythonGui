from tkinter import *
from PIL import Image, ImageTk




Tf = ("Arial Rounded MT Bold", 20)
Bf = ("Arial Rounded MT Bold", 15)
Txf = ("Arial", 10)

dbpass ={'Tony':'Stark', 'Bruce':'Wayne', 'Clark':'Kent', 'Steve':'Jobs', 'Elon':'Musk', 'Donald':'Trump','Angela':'Merkel'}

dbname ={}
dbusername ={}

def home():
	
	global roota

	roota =Tk()

	roota.title("Booking.com - Home")

	Tlabel = Label(roota, text='Book it. Love it.', font=Tf).grid(row = 1,columnspan=2,sticky="nsew")
	#	self.label.pack(side = "bottom")

	flabel = Label(roota, text='From cosy country homes to funky city flats', font=Txf).grid(row = 2,columnspan=2,sticky="nsew")

	#	self.label.pack(side = 'bottom')

	img = PhotoImage(file ="logo.gif")
	panel = Label(roota, image = img).grid(row = 0,columnspan=2,sticky="nsew")

	#	self.panel.pack(side = 'top', fill = 'both', expand = 'true')

	regh = Button(height = 1, width = 10, text="Let's get started", relief='raised',font =Bf, fg='#1A4191', command= lambda: registration())
	regh.grid(row = 3,column=0,sticky="nsew")

	#	self.reg.pack(side='left', expand = 'true')

	regl = Button(height = 1, width = 7, text='Login', font=Bf, fg='#1A4191',command= lambda: dlogin())
	regl.grid(row = 3,column=1,sticky="nsew")
	roota.mainloop()





def registration():
	roota.destroy()
	global uname
	global pname
	global root

	root = Tk()
	root.title("Registration")



	aimg = PhotoImage(file ="logo.gif")
	bpanel = Label(root, image = aimg).grid(row = 0,columnspan=2,sticky="nsew")
	#	self.panel.pack(side = 'top', fill = 'both', expand = 'true')

	label = Label(root, text='New User Registration', font=Tf).grid(row = 1,columnspan=2,sticky="nsew")
	#	self.label.pack()

	nlabel = Label(root, text='Name', font=Txf).grid(row = 2,column=0,sticky="nsew")
	#	self.nlabel.pack(side = 'left', expand ='true')

	ename = Entry( bd =5).grid(row = 2,column=1,sticky="nsew")
	#	self.ename.pack(side = 'right', expand ='true')

	ulabel = Label(root, text='Username', font=Txf).grid(row = 3,column=0,sticky="nsew")
	#	self.ulabel.pack(side = 'left', expand ='true')

	uname = Entry( bd =5)
	uname.grid(row = 3,column=1,sticky="nsew")
	#	self.uname.pack(side = 'right', expand ='true')

	mlabel = Label(root, text='Email ID', font=Txf).grid(row = 4,column=0,sticky="nsew")
	#	self.mlabel.pack(side = 'left', expand ='true')

	mname = Entry( bd =5).grid(row = 4,column=1,sticky="nsew")
	#	self.mname.pack(side = 'right', expand ='true')

	plabel = Label(root, text='Password', font=Txf).grid(row = 5,column=0,sticky="nsew")
	#	self.plabel.pack(side = 'left', expand ='true')

	pname = Entry( bd =5,show="•")
	pname.grid(row = 5,column=1,sticky="nsew")
	#	self.pname.pack(side = 'right', expand ='true')

	clabel = Label(root, text='Phone', font=Txf).grid(row = 6,column=0,sticky="nsew")
	#	self.clabel.pack(side = 'left', expand ='true')

	cname = Entry( bd =5).grid(row = 6,column=1,sticky="nsew")
	#	self.cname.pack(side = 'right', expand ='true')
		
	reg = Button(height = 1, width = 10, text='Register', relief='raised',font =Bf, fg='#1A4191',command= addb)
	reg.grid(row = 7,columnspan=2,sticky="nsew")
	root.mainloop()


def addb():

	global u
	global p
	u=uname.get()
	#print(u)

	p =pname.get()
	#print(p)
	dbpass[u]=p
	#root.destroy()
	login()

	#print(dbpass)
	#	self.reg.pack(side ='bottom',)


def check():
	global c
	global d
	c = unameentry.get()
	d = passentry.get()

	if (dbpass[c] == d):
		rootb.destroy()
		success()
		print("Logged in")
	
	else: 
		rootb.destroy()
		failed()
		print("Unsuc")	



def dcheck():
	global e
	global f
	e = dunameentry.get()
	f = dpassentry.get()

	if (dbpass[e] == f):
		rootd.destroy()
		success()
		print("Logged in")
	
	else: 
		rootd.destroy()
		failed()
		print("Unsuc")	

def login():
	#roota.destroy()
	root.destroy()
	global rootb
	global unameentry
	global passentry

	rootb=Tk()
	rootb.title("Login")

	cimg = PhotoImage(file ="logo.gif")
	cpanel = Label(rootb, image = cimg).grid(row = 0,columnspan=2,sticky="nsew")
	#	self.panel.pack(side = 'top', fill = 'both', expand = 'true')

	loglabel = Label(rootb, text='User Login', font=Tf).grid(row = 1,columnspan=2,sticky="nsew")
	#	self.label.pack()

	unamelabel = Label(rootb, text='Username', font=Txf).grid(row = 2,column=0,sticky="nsew")
	#	self.nlabel.pack(side = 'left', expand ='true')

	unameentry = Entry( bd =5)
	unameentry.grid(row = 2,column=1,sticky="nsew")
	#	self.ename.pack(side = 'right', expand ='true')

	passlabel = Label(rootb, text='Password', font=Txf).grid(row = 3,column=0,sticky="nsew")
	#	self.ulabel.pack(side = 'left', expand ='true')

	passentry = Entry( bd =5,show="•")
	passentry.grid(row = 3,column=1,sticky="nsew")
	#	self.uname.pack(side = 'right', expand ='true')

	regb = Button(height = 1, width = 10, text='Login', relief='raised',font =Bf, fg='#1A4191', command = check)
	regb.grid(row = 4,columnspan = 2,sticky="nsew")
	#	self.reg.pack(side ='bottom',)
	rootb.mainloop()


def dlogin():
	#roota.destroy()
	roota.destroy()
	global rootd
	global dunameentry
	global dpassentry

	rootd=Tk()
	rootd.title("Login")

	dimg = PhotoImage(file ="logo.gif")
	dpanel = Label(rootd, image = dimg).grid(row = 0,columnspan=2,sticky="nsew")
	#	self.panel.pack(side = 'top', fill = 'both', expand = 'true')

	dloglabel = Label(rootd, text='User Login', font=Tf).grid(row = 1,columnspan=2,sticky="nsew")
	#	self.label.pack()

	dunamelabel = Label(rootd, text='Username', font=Txf).grid(row = 2,column=0,sticky="nsew")
	#	self.nlabel.pack(side = 'left', expand ='true')

	dunameentry = Entry( bd =5)
	dunameentry.grid(row = 2,column=1,sticky="nsew")
	#	self.ename.pack(side = 'right', expand ='true')

	dpasslabel = Label(rootd, text='Password', font=Txf).grid(row = 3,column=0,sticky="nsew")
	#	self.ulabel.pack(side = 'left', expand ='true')

	dpassentry = Entry( bd =5,show="•")
	dpassentry.grid(row = 3,column=1,sticky="nsew")
	#	self.uname.pack(side = 'right', expand ='true')

	dregb = Button(height = 1, width = 10, text='Login', relief='raised',font =Bf, fg='#1A4191', command = dcheck)
	dregb.grid(row = 4,columnspan = 2,sticky="nsew")
	#	self.reg.pack(side ='bottom',)
	rootd.mainloop()


def success():
	global rootc
	rootc =Tk()
	rootc.title("Successful Login")
	suclabel = Label(rootc, text="Successful Login", font =Tf).grid(row=0, columnspan=2)
	labelsucc= Label(rootc, text="Happy Holidays", font=Tf).grid(row=1, columnspan=2)
	regb = Button(height = 1, width = 10, text="Home", relief='raised',font =Bf, fg='#1A4191', command= lambda: back()).grid(row=2, columnspan=2)

def failed():
	global rootc
	rootc =Tk()
	rootc.title("Unsuccessful Login")
	suclabel = Label(rootc, text="Failed Login", font =Tf).grid(row=0, columnspan=2)
	labelsucc= Label(rootc, text="UnHappy Holidays", font=Tf).grid(row=1, columnspan=2)
	regb = Button(height = 1, width = 10, text="Home", relief='raised',font =Bf, fg='#1A4191', command= lambda: back()).grid(row=2, columnspan=2)
	

def back():
	rootc.destroy()
	home()	

home()

