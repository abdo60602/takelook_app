from Tkinter import *
from PIL import Image, ImageTk
import home
import mysql.connector
import db_connection

class Application(Frame):

    def __init__(self, master=None):    	
        Frame.__init__(self, master)
        self.configure(bg='black')
        self.grid()
        self.createWidgets()

        self.im = Image.open("pic.jpg")
        self.photo = ImageTk.PhotoImage(self.im)

        self.w = Label(self, 
                     compound = CENTER, 
                     image=self.photo,bg='black').grid(row=4,sticky='N')


    def createWidgets(self):
    	self.user_name_ = Label(self,fg='#8bc900',bg='black', text='User Name',font=("Arial", 15),padx=10)
        self.user_name_.grid(sticky=W)
        
        self.user_name = Entry(self, font=("Arial", 15),fg='#041633',borderwidth=2,relief='sunken')
        self.user_name.grid(pady=10, row= 0,padx=125)
        self.user_name.bind("<Return>",self.test_login)
        

    	self.password_ = Label(self,bg='black', text='Password',font=("Arial", 15),fg='#8bc900',padx=13)
        self.password_.grid(sticky=W)
        
        self.password = Entry(self, font=("Arial", 15),show='*',fg='#041633',borderwidth=2,relief='sunken')
        self.password.grid(row=1,pady=10)
        self.password.bind("<Return>",self.test_login)

        self.login = Button(self, text='Login', fg='white',bg='#8aa306', command= self.test_login, font=("Arial", 15,'bold'),borderwidth=4,relief='raised')
        self.login.grid(ipadx =40)

        self.forget = Button(self, text='Forget Password',bg='#5a5767', fg='white', command= self.test_login, font=("Arial", 12),borderwidth=3,relief='raised')
        self.forget.grid(padx=3,row=2,sticky='W')

        self.copyright = Label(self,bg='black', text='Copyright (C) 2018 Author Abdallah Darweesh',font=("Arial", 8),fg='#8bc900',padx=13)
        self.copyright.grid(row=5)

        self.conn_error_ = Button(self, text='Create Account',font=("Arial", 12),fg='black',bg='#C2E3DC')
        self.conn_error_.grid(row=2,sticky='E',padx=30)

    def test_login(self, *event):
    	        
        profile_id = None
        try:
            db_connection.cur.execute(db_connection.query)
            for x in db_connection.cur.fetchall():
                if self.user_name.get() == x[1] and self.password.get()==x[2]: #Cheack user in db                
                    profile_id = x[0]                               
                    break               

            if profile_id == None:
                self.conn_error_ = Label(self,bg='black', text='Wrong Password Mother Fucker',font=("Arial", 8),fg='#08C5D1',padx=13)
                self.conn_error_.grid(row=3)

                
            else:
                self.activ_user()    

        except:
            self.conn_error()

    def activ_user(self):
        self.destroy()

        home.Application()

    def conn_error(self):
        self.copyright = Label(self,bg='black', text='Error with your connection!',font=("Arial", 10),fg='red',padx=13)
        self.copyright.grid(row=3)

    def test(self, *event):
    	u = self.user_name.get()
    	p = self.password.get()
    	print u+ '==>'+ p


