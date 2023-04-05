from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import random
import time
import mysql.connector

config = {
  'user': 'root',
  'password': 'Enter-Your-Password-Here',
  'host': 'localhost',
  'database': 'library',
}

image1=r'c:\Users\ruins\Desktop\LibraryManagementSystem\show.jpg'


class studmenu:

    def __init__(self,aa,stud):
        self.root=Tk()
        self.root.title('Library')
        self.root.state('zoomed')
        self.a=self.canvases(image1)
        self.check_notice()
        self.student=stud
        l2=Button(self.a,text='Search Books',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.search).place(x=12,y=100)
        l3=Button(self.a,text='View Activity',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.activity).place(x=12,y=200)
        l3=Button(self.a,text='Change Password',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.changepass1).place(x=12,y=300)
        self.putnotice()
        if aa:
            self.changepass(stud)

        self.root.mainloop()

    def canvases(self,images):
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        #photo=PhotoImage(file=images)
        photo=Image.open(images)
        photo1=photo.resize((w,h),Image.ANTIALIAS)
        photo2=ImageTk.PhotoImage(photo1)

        #photo2 = ImageTk.PhotoImage(Image.open(images).resize((w, h)),Image.ANTIALIAS)
        self.canvas = Canvas(self.root, width='%d'%w, height='%d'%h)
        self.canvas.grid(row = 0, column = 0)
        self.canvas.grid_propagate(0)
        self.canvas.create_image(0, 0, anchor = NW, image=photo2)
        self.canvas.image=photo2
        return self.canvas

    def check_notice(self):
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        cursor.execute("""delete from notice where 
            noticeid in(select noticeid from events where
            termination < curdate())""")
        conn.commit()

    def changepass(self,sid):

        self.passwd1=StringVar()
        self.passwd2=StringVar()
        
        self.f1=Frame(self.a,height=400,width=650,bg='black')
        self.f1.place(x=500,y=50)
        l0=Label(self.f1,text='CHANGE PASSWORD',font='Calibri 22 bold',fg='white',bg='Black',pady=1).place(x=190,y=20)
        l2=Label(self.f1,text='New Password : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=120,y=150)
        e2=Entry(self.f1,width=45,bg='white',show='*',fg='black',textvariable=self.passwd1).place(x=240,y=150)
        l3=Label(self.f1,text='Re-enter : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=120,y=200)
        e3=Entry(self.f1,width=45,bg='white',show='*',fg='black',textvariable=self.passwd2).place(x=240,y=200)
        
        self.f1.grid_propagate(0)
        b1=Button(self.f1,text='Change',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.change).place(x=260,y=300)
        #b2=Button(self.f1,text='Back',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.rm).place(x=380,y=300)

    def changepass1(self):

        self.passwd1=StringVar()
        self.passwd2=StringVar()
        
        self.f1=Frame(self.a,height=400,width=650,bg='black')
        self.f1.place(x=500,y=50)
        l0=Label(self.f1,text='CHANGE PASSWORD',font='Calibri 22 bold',fg='white',bg='Black',pady=1).place(x=190,y=20)
        l2=Label(self.f1,text='New Password : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=120,y=150)
        e2=Entry(self.f1,width=45,bg='white',show='*',fg='black',textvariable=self.passwd1).place(x=240,y=150)
        l3=Label(self.f1,text='Re-enter : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=120,y=200)
        e3=Entry(self.f1,width=45,bg='white',show='*',fg='black',textvariable=self.passwd2).place(x=240,y=200)
        
        self.f1.grid_propagate(0)
        b1=Button(self.f1,text='Change',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.change).place(x=380,y=300)
        b2=Button(self.f1,text='Back',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.rm).place(x=200,y=300)

    def change(self):
        p1=self.passwd1.get()
        p2=self.passwd2.get()
        if p1 == "" or p2 == "":
            messagebox.showinfo("Error","Password can't be empty")
        elif p1!=p2:
            messagebox.showinfo("Error","New password and re-entered password don't match")
            self.passwd1.set("")
            self.passwd2.set("")
        else:
            try:
                conn=mysql.connector.connect(**config)
                cursor=conn.cursor()
                cursor.execute('''update student set passwd="{}" where studentid="{}"'''.format(p1,self.student))
                conn.commit()
                messagebox.showinfo("Success","Password changed")
                self.passwd1.set("")
                self.passwd2.set("")
                #time.sleep(5)
                self.rm()

            except:
                messagebox.showinfo("Error","There was an error in changing the password")
                self.passwd1.set("")
                self.passwd2.set("")
    
    def search(self):
        #self.search.state('zoomed')
        self.sid=StringVar()
        self.f1=Frame(self.a,height=400,width=650,bg='black')
        self.f1.place(x=500,y=50)
        l1=Label(self.f1,text='Book Title/Author/Department/Publisher : ',font=('Calibri 10 bold'),bd=2, fg='white',bg='black').place(x=90,y=42)
        e1=Entry(self.f1,width=25,bd=5,bg='white',fg='black',textvariable=self.sid).place(x=345,y=40)
        b1=Button(self.f1,text='Search',bg='black',fg='white',font='Calibri 10 bold',width=9,bd=2,command=self.serch1).place(x=350,y=360)
        b1=Button(self.f1,text='Back',bg='black',fg='white',font='Calibri 10 bold',width=10,bd=2,command=self.rm).place(x=250,y=360)

    def create_tree(self,plc,lists,h,w):
        self.tree=ttk.Treeview(plc,height=h,column=(lists),show='headings')
        n=0
        while n is not len(lists):
            self.tree.heading("#"+str(n+1),text=lists[n])
            self.tree.column(""+lists[n],width=w,anchor=CENTER)
            n=n+1
        return self.tree


    def serch1(self):
        k=self.sid.get()
        if k!="":
            self.list4=("TITLE","AUTHOR","PUBLISHER","DEPARTMENT")
            self.trees=self.create_tree(self.f1,self.list4,12,130)
            self.trees.place(x=70,y=80)
            conn=mysql.connector.connect(**config)
            cursor=conn.cursor()

            c=cursor.execute('''select B.TITLE, A.NAME, B.PUB_NAME, D.NAME
                from BOOK B, DEPARTMENT D, AUTHOR A
                WHERE B.DEPTID=D.DEPTID AND B.AUTHORID=A.AUTHORID
                AND (B.TITLE='{}' OR A.NAME='{}' OR D.NAME='{}' OR B.PUB_NAME='{}')'''.format(k.upper(),k.upper(),k.upper(),k.upper(),k.upper(),))
            a=cursor.fetchall()
            if len(a)!=0:
                for row in a:

                    self.trees.insert("",END,values=row)
                conn.commit()
                conn.close()
                self.trees.bind('<<TreeviewSelect>>')
                self.variable = StringVar(self.f1)
                #self.variable.set("Select Action:")


            else:
                messagebox.showinfo("Error","Data not found")



        else:
            messagebox.showinfo("Error","Search field cannot be empty.")

    def activity(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()
        self.f1=Frame(self.a,height=400,width=650,bg='black')
        self.f1.place(x=500,y=50)
        self.list2=("BOOK TITLE","STUDENT NAME","ISSUE DATE","RETURN DATE","SUBMITTED")
        self.trees=self.create_tree(self.f1,self.list2,13,110)
        self.trees.place(x=50,y=50)
        self.searchact()
        b1=Button(self.f1,text='Back',bg='black',fg='white',font='Calibri 10 bold',width=10,bd=3,command=self.rm).place(x=500,y=450)
        self.f1.grid_propagate(0)

    def searchact(self):
        self.list2=("BOOK TITLE","STUDENT NAME","ISSUE DATE","RETURN DATE","SUBMITTED")
        self.trees=self.create_tree(self.f1,self.list2,13,110)
        self.trees.place(x=50,y=50)
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        bid=self.aidd.get()
        #sid=self.astudentt.get()
        try:
            c=cursor.execute('''SELECT B.TITLE, S.NAME, L.ISSUE_DATE, L.DUE_DATE, L.SUBM
                FROM BOOK B, STUDENT S, STUDENT_LENDING L
                WHERE B.BOOKID=L.BOOKID AND S.STUDENTID=L.STUDENTID
                AND L.STUDENTID="{}"'''.format(self.student,))
            d=cursor.fetchall()
            if len(d)!=0:
                for row in d:
                    self.trees.insert("",END,values=row)
            else:
                messagebox.showinfo("Error","Data not found.")
            conn.commit()

        except Exception as e:
            messagebox.showinfo(e)
        conn.close()


    def rm(self):
        self.f1.destroy()

    def create_tree1(self,plc,lists,h):
        self.tree=ttk.Treeview(plc,height=h,column=(lists),show='headings')
        n=0
        while n is not len(lists):
            #self.tree.heading("#"+str(n+1),text=lists[n])
            self.tree.column(""+lists[n],width=900,anchor=CENTER)
            n=n+1
        return self.tree

    def putnotice(self):
        
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute("select body from notice")
        content = cursor.fetchall()

        self.f1=Frame(self.a,height=300,width=1000,bg='black')
        self.f1.place(x=260,y=470)
        l0=Label(self.f1,text='NOTICE',font='Calibri 22 bold',fg='white',bg='Black',pady=1).place(x=440,y=5)
        self.list5=("NOTICE",)
        self.trees=self.create_tree1(self.f1,self.list5,10)
        self.trees.place(x=50,y=45)
        if len(content)!=0:
            for row in content:
                self.trees.insert("",END,values=row)
    


#studmenu(False,'200401')
