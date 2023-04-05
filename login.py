from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import random
import mysql.connector
from smenu import *
from menu import *

config = {
  'user': 'root',
  'password': 'Enter-Your-Password-Here',
  'host': 'localhost',
  'database': 'library',
}

image1=r'c:\Users\ruins\Desktop\LibraryManagementSystem\show.jpg'
image2=r'c:\Users\ruins\Desktop\LibraryManagementSystem\show.jpg'
image3=r'c:\Users\ruins\Desktop\LibraryManagementSystem\show.jpg'

class login:
    
    def __init__(self):
        self.abc = Tk()
        self.abc.title("LOGIN")
        self.canvas=self.canvases(image3)
        self.USERNAME = StringVar()
        self.PASSWORD = StringVar()
        lbs_title = Label(self.canvas, text = "LIBRARY MANAGEMENT SYSTEM", font=('Calibri', 30,'bold', ), bg= 'black', fg='white')
        lbs_title.place(x=450,y=50)
        lbl_title = Label(self.canvas, text = "WELCOME", font=('Calibri', 25,'bold', ), bg= 'black', fg='white')
        lbl_title.place(x=650,y=150)
        lbl_username = Label(self.canvas, text = "Username:", font=('Calibri', 15,'bold'),bd=4,bg='black', fg='white')
        lbl_username.place(x=500,y=230)
        lbl_password = Label(self.canvas, text = "Password :", font=('Calibri', 15,'bold'),bd=3, bg='black', fg='white')
        lbl_password.place(x=500, y=330)
        btn_login = Button(self.canvas, text="LOG IN", font=('Calibri 15 bold'),width=25,command=self.oklogin, bg='black', fg='white')
        btn_login.place(x=575,y=420)
        btn_login = Button(self.canvas, text="SIGN UP", font=('Calibri 15 bold'),width=25,command=self.oksignup, bg='black', fg='white')
        btn_login.place(x=575,y=480)

        username = Entry(self.canvas, textvariable=self.USERNAME, font=(14), bg='#1f1d1d', fg='white',bd=6)
        username.place(x=650, y=230,)
        username.focus_set()
        password = Entry(self.canvas, textvariable=self.PASSWORD, show="*", font=(14),bg='#1f1d1d', fg='white',bd=6)
        password.place(x=650, y=330)

        password.bind('<Return>', self.oklogin)

        #==============================BUTTON WIDGETS=================================
        
        btn_login.bind('<Return>', self.oklogin)
        self.abc.mainloop()    

    def oksignup(self):
        set
        self.sname=StringVar()
        self.sid=StringVar()
        self.sphone=StringVar()

        self.f1=Frame(self.canvas,height=500,width=650,bg='black')
        self.f1.place(x=410,y=120)

        lb2_title = Label(self.f1, text = "SIGN UP", font=('Calibri', 25,'bold', ), bg= 'black', fg='white')
        lb2_title.place(x=260,y=20)
        lbl_username = Label(self.f1, text = "Student ID :", font=('Calibri', 15,'bold'),bd=4,bg='black', fg='white')
        lbl_username.place(x=140,y=100)
        id3 = Entry(self.f1, textvariable=self.sid, font=(14), bg='#1f1d1d', fg='white',bd=6)
        id3.place(x=260, y=100,)
        lbl_username = Label(self.f1, text = "Name :", font=('Calibri', 15,'bold'),bd=4,bg='black', fg='white')
        lbl_username.place(x=140,y=150)
        id = Entry(self.f1, textvariable=self.sname, font=(14), bg='#1f1d1d', fg='white',bd=6)
        id.place(x=260, y=150,)
        lbl_username = Label(self.f1, text = "Phone :", font=('Calibri', 15,'bold'),bd=4,bg='black', fg='white')
        lbl_username.place(x=140,y=200)
        id = Entry(self.f1, textvariable=self.sphone, font=(14), bg='#1f1d1d', fg='white',bd=6)
        id.place(x=260, y=200,)
        id3.focus_set()

        

        b1=Button(self.f1,text='Register',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.registerstud).place(x=150,y=400)
        b2=Button(self.f1,text='Back',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.rm).place(x=350,y=400)


        self.f1.grid_propagate(0)

    def registerstud(self):
        name=self.sname.get()
        studid=self.sid.get()
        sph=self.sphone.get()

        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()

        self.cursor.execute("select * from student where studentid='{}'".format(studid))
        sres=self.cursor.fetchall()


        if sres==[]:

            self.cursor.execute("insert into student values('{}','{}','{}','jss123')".format(studid,name.upper(),sph,))
            self.conn.commit()
            messagebox.showinfo("Success","Registered Successfully\nPlease Login")
            self.rm()
        else:
            messagebox.showinfo("Error","Student with this ID already exists")




    def rm(self):
        self.f1.destroy()

    def canvases(self,images):
        w = self.abc.winfo_screenwidth()
        h = self.abc.winfo_screenheight()
        photo=Image.open(images)
        photo1=photo.resize((w,h),Image.ANTIALIAS)
        photo2=ImageTk.PhotoImage(photo1)

        #photo2 = ImageTk.PhotoImage(Image.open(images).resize((w, h)),Image.ANTIALIAS)
        canvas = Canvas(self.abc, width='%d'%w, height='%d'%h)
        canvas.grid(row = 0, column = 0)
        canvas.grid_propagate(0)
        
        canvas.create_image(0, 0, anchor = NW, image=photo2)
        canvas.image=photo2
        return canvas
        

    def Database(self):
        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM `ADMIN` WHERE `username` = 'admin' AND `passwd` = 'root'")
        if self.cursor.fetchone() is None:
            self.cursor.execute("INSERT INTO `ADMIN` (username, passwd) VALUES('admin', 'root')")
            self.conn.commit()

    def oklogin(self,event=None):
        self.Database()

        self.cursor.execute("select * from student where studentid='{}' and passwd='{}'".format(self.USERNAME.get(), self.PASSWORD.get()))
        astud = self.cursor.fetchall()

        self.cursor.execute("SELECT * FROM ADMIN WHERE username = '{}' AND passwd = '{}'".format(self.USERNAME.get(), self.PASSWORD.get()))
        aadmin = self.cursor.fetchall()




        if self.USERNAME.get() == "" or self.PASSWORD.get() == "":
            messagebox.showinfo("Error","Please complete the required field!")
            #lbl_text.config(text="Please complete the required field!", fg="red")
        else:

            if astud!=[]:
                if self.PASSWORD.get()=='jss123':
                    self.abc.destroy()
                    a=studmenu(True,self.USERNAME.get())
                else:
                    self.abc.destroy()
                    a=studmenu(False,self.USERNAME.get())
            
            elif aadmin!=[]:
                #HomeWindow()
                #Top.destroy()
                self.abc.destroy()

                a=menu()
                #USERNAME.set("")
                #PASSWORD.set("")
                #lbl_text.config(text="")
            else:
                messagebox.showinfo("Error","Invalid username or password.")
                #lbl_text.config(text="Invalid username or password", fg="red")
                self.USERNAME.set("")
                self.PASSWORD.set("")

        self.cursor.close()
        self.conn.close()




login()

