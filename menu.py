from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import random
import mysql.connector
import pandas as pd



#pip install Pillow

config = {
  'user': 'root',
  'password': 'Enter-Your-Password-Here',
  'host': 'localhost',
  'database': 'library',
}

image1=r'c:\Users\ruins\Desktop\LibraryManagementSystem\show.jpg'
image2=r'c:\Users\ruins\Desktop\LibraryManagementSystem\show.jpg'
image3=r'c:\Users\ruins\Desktop\LibraryManagementSystem\show.jpg'

class menu:

    def __init__(self):

        self.root=Tk()
        self.root.title('Library')
        self.root.state('zoomed')

        self.a=self.canvases(image1)
        l1=Button(self.a,text='BOOK DATA',font='Calibri 22 bold',fg='white',bg='Black',width=19,padx=10,borderwidth=3,command=self.book).place(x=200,y=400)
        l2=Button(self.a,text='STUDENT DATA',font='Calibri 22 bold',fg='white',bg='Black',width=19,padx=10,borderwidth=3,command=self.student).place(x=600,y=400)
        l3=Button(self.a,text='EVENT & NOTICE',font='Calibri 22 bold',fg='white',bg='Black',width=19,padx=10,borderwidth=3,command=self.evno).place(x=1000,y=400)
        
        

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
        
    def book(self):
        self.a.destroy()
        self.a=self.canvases(image2)
        l1=Button(self.a,text='Add Books',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.addbook).place(x=12,y=100)
        l2=Button(self.a,text='Search Books',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.search).place(x=12,y=200)

        l3=Button(self.a,text='All Books',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.all).place(x=12,y=300)
        l5=Button(self.a,text='Delete Books',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.delbook).place(x=12,y=400)
        l6=Button(self.a,text='Add Author',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.addauthor).place(x=12,y=500)
        l4=Button(self.a,text='<< Main Menu',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.mainmenu).place(x=12,y=600)
        self.bookcount = Label(self.a,font='Calibri 20 bold',fg='white',bg='Black',width=15,padx=10)
        self.bookcount.place(x=630,y=700)
        self.bookset()

    def bookset(self):
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("select total from total_count where entity = 'book'")
        res = cursor.fetchone()
        disp = "Total Books : {}".format(res[0])
        self.bookcount.config(text=disp)

    def addauthor(self):
        self.authorid=StringVar()
        self.authorname=StringVar()
        self.authormail=StringVar()
        self.f1=Frame(self.a,height=500,width=650,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Author ID : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=50)
        e1=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.authorid).place(x=150,y=50)
        l2=Label(self.f1,text='Name : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=100)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.authorname).place(x=150,y=100)
        l3=Label(self.f1,text='Email : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=150)
        e3=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.authormail).place(x=150,y=150)
        
        self.f1.grid_propagate(0)
        b1=Button(self.f1,text='Add',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.addauthdata).place(x=150,y=400)
        b2=Button(self.f1,text='Back',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.rm).place(x=350,y=400)

    def rm(self):
        self.f1.destroy()
    def mainmenu(self):
        self.root.destroy()
        #self.a.destroy()
        #self.a=self.canvases(image1)
        a=menu()

    def addauthdata(self):
        a=self.authorid.get()
        b=self.authorname.get()
        c=self.authormail.get()
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        try:
            if (a and b )=="":
                messagebox.showinfo("Error","Fields cannot be empty.")
            else:
                cursor.execute("insert into author \
                values ('{}','{}','{}')".format(a.upper(),b.upper(),c.upper(),))
                conn.commit()
                messagebox.showinfo("Success","Author added successfully")
        except mysql.connector.IntegrityError:
            messagebox.showinfo("Error","Author is already present.")


        conn.close()



    def delbook(self):
        self.adid=StringVar()

        self.f1=Frame(self.a,height=500,width=650,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=50)
        e1=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.adid).place(x=150,y=50)
        
        self.f1.grid_propagate(0)
        b1=Button(self.f1,text='Delete',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.deldata).place(x=150,y=400)
        b2=Button(self.f1,text='Back',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.rm).place(x=350,y=400)
    
    def deldata(self):
        a=self.adid.get()
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        try:
            if a=="":
                messagebox.showinfo("Error","Field cannot be empty.")
            else:
                cursor.execute("delete from book \
                where bookid = '{}'".format(a,))
                conn.commit()
                messagebox.showinfo("Success","Book deleted successfully")
                self.bookset()
        except mysql.connector.IntegrityError:
            messagebox.showinfo("Error","Book is not present.")


        conn.close()

    def addbook(self):
        self.bookid=StringVar()
        self.aauthor=StringVar()
        self.pubname=StringVar()
        self.title=StringVar()
        self.adeptid=StringVar()
        self.authname=StringVar()
        self.cop=IntVar()
        self.f1=Frame(self.a,height=500,width=650,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=50)
        e1=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.bookid).place(x=175,y=50)
        l2=Label(self.f1,text='Author ID : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=100)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.aauthor).place(x=175,y=100)
        l3=Label(self.f1,text='Publisher : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=150)
        e3=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.pubname).place(x=175,y=150)
        l4=Label(self.f1,text='Title : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=200)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.title).place(x=175,y=200)
        l4=Label(self.f1,text='Department ID : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=250)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.adeptid).place(x=175,y=250)
        l5=Label(self.f1,text='Author Name : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=300)
        e3=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.authname).place(x=175,y=300)
        l6=Label(self.f1,text='Copies : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=350)
        e3=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.cop).place(x=175,y=350)

        self.f1.grid_propagate(0)
        b1=Button(self.f1,text='Add',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.adddata).place(x=150,y=450)
        b2=Button(self.f1,text='Back',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.rm).place(x=350,y=450)

    # def rm(self):
    #     self.f1.destroy()
    # def mainmenu(self):
    #     self.root.destroy()
    #     a=menu()

    def adddata(self):
        a=self.bookid.get()
        b=self.aauthor.get()
        c=self.pubname.get()
        d=self.title.get()
        e=self.adeptid.get()
        f=self.authname.get()
        g=self.cop.get()
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        
        
        
        try:
            if (a and b and c and d  and e and f and g)=="":
                messagebox.showinfo("Error","Fields cannot be empty.")
            
            else:
                com1 = cursor.execute("select * from author where authorid='{}' and name='{}'".format(b,f))
                res1 = cursor.fetchall()
                if (res1==[]):
                    cursor.execute("insert into author (authorid,name) values('{}','{}')".format(b,f.upper(),))

                com2 = cursor.execute("select * from publisher where name='{}'".format(c,))
                res2 = cursor.fetchall()
                if (res2==[]):
                    cursor.execute("insert into publisher (name) values('{}')".format(c.upper(),))
                    
                com3 = cursor.execute("select * from department where deptid='{}'".format(e,))
                res3 = cursor.fetchall()
                if (res3==[]):
                    messagebox.showinfo("Error","No such department exists")
                    self.adeptid.set("")
            
                else:
                    cursor.execute("insert into book \
                        values ('{}','{}','{}','{}','{}')".format(a.upper(),d.upper(),e.upper(),c.upper(),b.upper(),))
                    conn.commit()
                    cursor.execute("insert into book_copies values('{}',{},0)".format(a.upper(),g,))
                    conn.commit()
                    messagebox.showinfo("Success","Book added successfully")
                    self.bookset()

        except mysql.connector.IntegrityError:
            messagebox.showinfo("Error","Book is already present.")


        conn.close()

    def search(self):
        #self.search.state('zoomed')
        self.sid=StringVar()
        self.f1=Frame(self.a,height=500,width=1000,bg='black')
        self.f1.place(x=300,y=100)
        l1=Label(self.f1,text='Book ID/Title/Author ID/Department ID/Publisher: ',font=('Calibri 10 bold'),bd=2, fg='white',bg='black').place(x=220,y=42)
        e1=Entry(self.f1,width=25,bd=5,bg='white',fg='black',textvariable=self.sid).place(x=520,y=40)
        b1=Button(self.f1,text='Search',bg='black',fg='white',font='Calibri 10 bold',width=9,bd=2,command=self.serch1).place(x=700,y=40)
        b1=Button(self.f1,text='Back',bg='black',fg='white',font='Calibri 10 bold',width=10,bd=2,command=self.rm).place(x=460,y=450)

    def create_tree(self,plc,lists,h):
        self.tree=ttk.Treeview(plc,height=h,column=(lists),show='headings')
        n=0
        while n is not len(lists):
            self.tree.heading("#"+str(n+1),text=lists[n])
            self.tree.column(""+lists[n],width=110,anchor=CENTER)
            n=n+1
        return self.tree


    def serch1(self):
        k=self.sid.get()
        if k!="":
            self.list4=("BOOK ID","TITLE","AUTHOR ID","AUTHOR","PUBLISHER","DEPARTMENT","AVAILABLE COPIES","RENTED COPIES")
            self.trees=self.create_tree(self.f1,self.list4,13)
            self.trees.place(x=55,y=150)
            conn=mysql.connector.connect(**config)
            cursor=conn.cursor()

            c=cursor.execute('''select B.BOOKID, B.TITLE, B.AUTHORID, A.NAME, B.PUB_NAME, D.NAME, 
            C.COPIES_AVAIL, C.COPIES_RENTD  from BOOK B, DEPARTMENT D, AUTHOR A, BOOK_COPIES C
            WHERE B.BOOKID=C.BOOKID AND B.DEPTID=D.DEPTID AND B.AUTHORID=A.AUTHORID
            AND (B.BOOKID='{}' OR B.TITLE='{}' OR B.AUTHORID='{}' OR B.DEPTID='{}' OR B.PUB_NAME='{}')'''.format(k.upper(),k.upper(),k.upper(),k.upper(),k.upper(),))
            a=cursor.fetchall()
            if len(a)!=0:
                for row in a:

                    self.trees.insert("",END,values=row)
                conn.commit()
                conn.close()
                self.trees.bind('<<TreeviewSelect>>')
                self.variable = StringVar(self.f1)
                self.variable.set("Select Action:")


                self.cm =ttk.Combobox(self.f1,textvariable=self.variable ,state='readonly',font='Calibri 15 bold',height=50,width=15,)
                self.cm.config(values =('Add Copies', 'Delete Copies'))

                self.cm.place(x=50,y=100)
                self.cm.pack_propagate(0)


                self.cm.bind("<<ComboboxSelected>>",self.combo)
                self.cm.selection_clear()
            else:
                messagebox.showinfo("Error","Data not found")



        else:
            messagebox.showinfo("Error","Search field cannot be empty.")


    def combo(self,event):
        self.var_Selected = self.cm.current()
        #l7=Label(self.f1,text='copies to update: ',font='Calibri 10 bold',bd=1).place(x=250,y=700)
        if self.var_Selected==0:
            self.copies(self.var_Selected)
        elif self.var_Selected==1:
            self.copies(self.var_Selected)
        elif self.var_Selected==2:
            self.deleteitem()

            
    # def deleteitem(self):
    #     try:
    #         self.curItem = self.trees.focus()

    #         self.c1=self.trees.item(self.curItem,"values")[0]
    #         b1=Button(self.f1,text='Update',bg='black',fg='white',font='Calibri 10 bold',width=9,bd=3,command=self.delete2).place(x=500,y=97)

    #     except:
    #         messagebox.showinfo("Empty","Please select something.")


    # def delete2(self):
    #     conn=mysql.connector.connect(**config)
    #     cd=cursor.execute("select * from book_issued where BOOK_ID='{}'",(self.c1,))
    #     ab=cd.fetchall()
    #     if ab!=0:
    #         cursor.execute("DELETE FROM book_info where ID='{}'",(self.c1,));
    #         conn.commit()
    #         messagebox.showinfo("Successful","Book Deleted sucessfully.")
    #         self.trees.delete(self.curItem)
    #     else:
    #         messagebox.showinfo("Error","Book is Issued.\nBook cannot be deleted.")
    #     conn.commit()
    #     conn.close()


    def copies(self,varr):
        try:
            curItem = self.trees.focus()
            self.c1=self.trees.item(curItem,"values")[0]
            self.c2=self.trees.item(curItem,"values")[6]
            self.scop=IntVar()
            self.e5=Entry(self.f1,width=20,textvariable=self.scop)
            self.e5.place(x=310,y=100)
            if varr==0:
                b5=Button(self.f1,text='Update',font='Calibri 10 bold',bg='black',fg='white',width=9,bd=3,command=self.copiesadd).place(x=500,y=97)
            if varr==1:
                b6=Button(self.f1,text='Update',font='Calibri 10 bold',bg='black',fg='white',width=9,bd=3,command=self.copiesdelete).place(x=500,y=97)
        except:
            messagebox.showinfo("Empty","Please select something.")

    def copiesadd(self):
        no=self.e5.get()
        if int(no)>=0:

            conn=mysql.connector.connect(**config)
            cursor=conn.cursor()

            cursor.execute("update book_copies set COPIES_AVAIL=COPIES_AVAIL+{} where BOOKID='{}'".format(no,self.c1,))
            conn.commit()

            messagebox.showinfo("Updated","Copies added sucessfully.")
            self.serch1()
            conn.close()

        else:
            messagebox.showinfo("Error","No. of copies cannot be negative.")

    def copiesdelete(self):
        no1=self.e5.get()
        if int(no1)>=0:
            if int(no1)<=int(self.c2):
                conn=mysql.connector.connect(**config)
                cursor=conn.cursor()

                cursor.execute("update book_copies set COPIES_AVAIL=COPIES_AVAIL-{} where BOOKID='{}'".format(no1,self.c1,))
                conn.commit()
                conn.close()

                messagebox.showinfo("Updated","Deleted sucessfully")
                self.serch1()

            else:
                messagebox.showinfo("Maximum","No. of copies to delete exceed available copies.")
        else:
            messagebox.showinfo("Error","No. of copies cannot be negative.")

    def all(self):
        self.f1=Frame(self.a,height=560,width=1000,bg='black')
        self.f1.place(x=300,y=100)
        b1=Button(self.f1,text='Back',bg='black' ,fg='white',width=10,bd=3,command=self.rm).place(x=460,y=520)
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        self.list3=("BOOK ID","TITLE","AUTHOR ID","AUTHOR","PUBLISHER","DEPARTMENT","AVAILABLE COPIES","RENTED COPIES")
        self.treess=self.create_tree(self.f1,self.list3,22)
        self.treess.place(x=55,y=30)
        c=cursor.execute('''select B.BOOKID, B.TITLE, B.AUTHORID, A.NAME, B.PUB_NAME, D.NAME, 
            C.COPIES_AVAIL, C.COPIES_RENTD  from BOOK B, DEPARTMENT D, AUTHOR A, BOOK_COPIES C
            WHERE B.BOOKID=C.BOOKID AND B.DEPTID=D.DEPTID AND B.AUTHORID=A.AUTHORID''')
        g=cursor.fetchall()
        if len(g)!=0:
            for row in g:
                self.treess.insert('',END,values=row)
        conn.commit()
        conn.close()


    def student(self):
        self.a.destroy()
        self.a=self.canvases(image2)
        l1=Button(self.a,text='Issue book',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.issue).place(x=12,y=100)
        l2=Button(self.a,text='Return Book',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.returnn).place(x=12,y=200)
        l6=Button(self.a,text='Renew Book',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.renew).place(x=12,y=300)
        l3=Button(self.a,text='Student Activity',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.activity).place(x=12,y=400)
        l5=Button(self.a,text='Add Student',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.addstudent).place(x=12,y=500)
        l4=Button(self.a,text='<< Main Menu',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.mainmenu).place(x=12,y=600)
        self.studcount = Label(self.a,font='Calibri 20 bold',fg='white',bg='Black',width=15,padx=10)
        self.studcount.place(x=630,y=700)
        self.studset()

    def studset(self):
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("select total from total_count where entity = 'student'")
        res = cursor.fetchone()
        disp = "Total Students : {}".format(res[0])
        self.studcount.config(text=disp)        


    def addstudent(self):
        self.studentid=StringVar()
        self.studentname=StringVar()
        self.studentphone=StringVar()
        self.f1=Frame(self.a,height=500,width=650,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Student ID : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=130,y=50)
        e1=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.studentid).place(x=230,y=50)
        l2=Label(self.f1,text='Name : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=130,y=100)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.studentname).place(x=230,y=100)
        l3=Label(self.f1,text='Phone : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=130,y=150)
        e3=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.studentphone).place(x=230,y=150)
        
        self.f1.grid_propagate(0)
        b1=Button(self.f1,text='Add',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.addstudentdata).place(x=180,y=400)
        b2=Button(self.f1,text='Back',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.rm).place(x=380,y=400)


    def addstudentdata(self):
        a=self.studentid.get()
        b=self.studentname.get()
        c=self.studentphone.get()
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        try:
            if (a and b )=="":
                messagebox.showinfo("Error","Fields cannot be empty.")
            else:
                cursor.execute("insert into student \
                values ('{}','{}','{}','jss123')".format(a.upper(),b.upper(),c.upper(),));
                conn.commit()
                messagebox.showinfo("Success","Student added successfully")
                self.studset()
        except mysql.connector.IntegrityError:
            messagebox.showinfo("Error","Student is already present.")


        conn.close()



    def issue(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()
        self.f1=Frame(self.a,height=550,width=500,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='Calibri 15 bold',bg='black',fg='white').place(x=50,y=100)
        e1=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.aidd).place(x=180,y=100)
        l2=Label(self.f1,text='Student Id : ',font='Calibri 15 bold',bg='black',fg='white').place(x=50,y=150)
        e2=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.astudentt).place(x=180,y=150)
        b1=Button(self.f1,text='Back',font='Calibri 10 bold',fg='white',bg='black',width=10,bd=3,command=self.rm).place(x=50,y=250)
        b1=Button(self.f1,text='Issue',font='Calibri 10 bold',bg='black',fg='white',width=10,bd=3,command=self.issuedbook).place(x=200,y=250)

    def issuedbook(self):
        bookid=self.aidd.get()
        studentid=self.astudentt.get()
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        cursor.execute("select BOOKID,COPIES_AVAIL from BOOK_COPIES where BOOKID='{}'".format(bookid.upper(),))
        an=cursor.fetchall()
        cursor.execute("select STUDENTID from student where STUDENTID='{}'".format(studentid,))
        af=cursor.fetchall()
        if (bookid and studentid!=""):
            if an!=[]:
                if af!=[]:
                    for i in an:
                        if i[1]>0:
                            try:
                                cursor.execute("insert into STUDENT_LENDING (issue_date,studentid,bookid,due_date) \
                                values (curdate(),'{}','{}',DATE_ADD(curdate(), INTERVAL 7 DAY))".format(studentid.upper(),bookid.upper(),));
                                conn.commit()
                                cursor.execute("update BOOK_COPIES set COPIES_AVAIL=COPIES_AVAIL-1,COPIES_RENTD=COPIES_RENTD+1 where BOOKID='{}'".format(bookid.upper(),))
                                conn.commit()
                                conn.close()
                                messagebox.showinfo("Updated","Book Issued sucessfully.")
                            except:
                                messagebox.showinfo("Error","Book is already issued by student.")

                        else:
                            messagebox.showinfo("Unavailable","Book unavailable.\nThere are 0 copies of the book.")
                else:
                    messagebox.showinfo("Error","No such student in Database.")
            else:
                messagebox.showinfo("Error","No such Book in Database.")
        else:
            messagebox.showinfo("Error","Fields cannot be blank.")

    def returnn(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()

        self.f1=Frame(self.a,height=550,width=500,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='Calibri 15 bold',fg='white', bg='black').place(x=50,y=100)
        e1=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.aidd).place(x=180,y=100)
        l2=Label(self.f1,text='Student Id : ',font='Calibri 15 bold',fg='white', bg='black').place(x=50,y=150)
        e2=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.astudentt).place(x=180,y=150)
        b1=Button(self.f1,text='Back',font='Calibri 10 bold',bg='black',fg='white',width=10,bd=3,command=self.rm).place(x=50,y=250)
        b1=Button(self.f1,text='Return',font='Calibri 10 bold',bg='black',fg='white',width=10,bd=3,command=self.returnbook).place(x=200,y=250)
        self.f1.grid_propagate(0)

    def returnbook(self):
        a=self.aidd.get()
        b=self.astudentt.get()

        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()

        fg=cursor.execute("select BOOKID from BOOK where BOOKID='{}'".format(a.upper(),))
        fh=cursor.fetchall()
        conn.commit()
        if fh!=[]:
            c=cursor.execute("select * from student_lending where BOOKID='{}' and STUDENTID='{}'".format(a.upper(),b.upper(),))
            d=cursor.fetchall()
            conn.commit()
            if len(d)!=0:
                cursor.execute("update student_lending set subm='y', due_date=curdate() where BOOKID='{}' and STUDENTID='{}'".format(a.upper(),b.upper(),));
                conn.commit()
                cursor.execute("update book_copies set COPIES_AVAIL=COPIES_AVAIL+1, COPIES_RENTD=COPIES_RENTD-1 where BOOKID='{}'".format(a.upper(),))
                conn.commit()

                messagebox.showinfo("Success","Book Returned sucessfully.")
            else:
                messagebox.showinfo("Error","Data not found.")
        else:
            messagebox.showinfo("Error","No such book.\nPlease add the book in database.")
        conn.commit()
        conn.close()

    def renew(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()

        self.f1=Frame(self.a,height=550,width=500,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='Calibri 15 bold',fg='white', bg='black').place(x=50,y=100)
        e1=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.aidd).place(x=180,y=100)
        l2=Label(self.f1,text='Student Id : ',font='Calibri 15 bold',fg='white', bg='black').place(x=50,y=150)
        e2=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.astudentt).place(x=180,y=150)
        b1=Button(self.f1,text='Back',font='Calibri 10 bold',bg='black',fg='white',width=10,bd=3,command=self.rm).place(x=50,y=250)
        b1=Button(self.f1,text='Renew',font='Calibri 10 bold',bg='black',fg='white',width=10,bd=3,command=self.renewbook).place(x=200,y=250)
        self.f1.grid_propagate(0)

    def renewbook(self):
        a=self.aidd.get()
        b=self.astudentt.get()

        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()

        fg=cursor.execute("select BOOKID from BOOK where BOOKID='{}'".format(a.upper(),))
        fh=cursor.fetchall()
        conn.commit()
        if fh!=[]:
            c=cursor.execute("select * from student_lending where BOOKID='{}' and STUDENTID='{}'".format(a.upper(),b.upper(),))
            d=cursor.fetchall()
            conn.commit()
            if len(d)!=0:
                cursor.execute("update student_lending set due_date=date_add(due_date,interval 7 day) where BOOKID='{}' and STUDENTID='{}'".format(a.upper(),b.upper(),));
                conn.commit()
                

                messagebox.showinfo("Success","Book Renewed sucessfully.")
            else:
                messagebox.showinfo("Error","Data not found.")
        else:
            messagebox.showinfo("Error","No such book.\nPlease add the book in database.")
        conn.commit()
        conn.close()

    def activity(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()
        self.f1=Frame(self.a,height=550,width=700,bg='black')
        self.f1.place(x=400,y=80)
        self.list2=("BOOK ID","STUDENT ID","ISSUE DATE","RETURN DATE","SUBMITTED")
        self.trees=self.create_tree(self.f1,self.list2,13)
        self.trees.place(x=70,y=130)


        l1=Label(self.f1,text='Book/Student ID : ',font='Calibri 15 bold',fg='white',bg='black').place(x=170,y=32)
        e1=Entry(self.f1,width=20,bd=4,bg='white',textvariable=self.aidd).place(x=360,y=35)
        #l2=Label(self.f1,text='Student Id : ',font='Calibri 15 bold',fg='white',bg='black').place(x=50,y=80)
        #e2=Entry(self.f1,width=20,bd=4,bg='white',textvariable=self.astudentt).place(x=180,y=80)
        b1=Button(self.f1,text='Search',bg='black',fg='white',font='Calibri 10 bold',width=10,bd=3,command=self.searchact).place(x=80,y=450)
        b1=Button(self.f1,text='All',bg='black',fg='white',font='Calibri 10 bold',width=10,bd=3,command=self.searchall).place(x=230,y=450)
        b1=Button(self.f1,text='Export',bg='black',fg='white',font='Calibri 10 bold',width=10,bd=3,command=self.csvexport).place(x=380,y=450)
        b1=Button(self.f1,text='Back',bg='black',fg='white',font='Calibri 10 bold',width=10,bd=3,command=self.rm).place(x=530,y=450)
        self.f1.grid_propagate(0)

    def csvexport(self):
        conn=mysql.connector.connect(**config)
        q = "select bookid,studentid,issue_date,due_date,subm from student_lending"
        try:
            df = pd.read_sql(q,conn)
            df.to_excel("lending_report.xlsx", index=False)
            messagebox.showinfo("Success","The data is exported successfully\nCheck lending_report.xlsx")
        except:
            messagebox.showinfo("Error","There was some problem in exporting the data")


    def searchact(self):
        self.list2=("BOOK ID","STUDENT ID","ISSUE DATE","RETURN DATE","SUBMITTED")
        self.trees=self.create_tree(self.f1,self.list2,13)
        self.trees.place(x=70,y=130)
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        bid=self.aidd.get()
        #sid=self.astudentt.get()
        try:
            c=cursor.execute("select bookid,studentid,issue_date,due_date,subm from student_lending where BOOKID='{}' or STUDENTID='{}'".format(bid.upper(),bid.upper(),))
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

    def searchall(self):
        self.list2=("BOOK ID","STUDENT ID","ISSUE DATE","RETURN DATE","SUBMITTED")
        self.trees=self.create_tree(self.f1,self.list2,13)
        self.trees.place(x=70,y=130)
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        try:
            c=cursor.execute("select bookid,studentid,issue_date,due_date,subm from student_lending")
            d=cursor.fetchall()
            for row in d:
                self.trees.insert("",END,values=row)

            conn.commit()

        except Exception as e:
            messagebox.showinfo(e)
        conn.close()

    def evno(self):
        self.a.destroy()
        self.a=self.canvases(image2)
        l1=Button(self.a,text='Add Notice',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.addnot).place(x=12,y=100)
        l2=Button(self.a,text='Delete Notice',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.delnot).place(x=12,y=200)
        l3=Button(self.a,text='Add Event',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.addevent).place(x=12,y=300)
        l3=Button(self.a,text='Search Event',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.evsearch).place(x=12,y=400)
        l4=Button(self.a,text='<< Main Menu',font='Calibri 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.mainmenu).place(x=12,y=500)

    def evsearch(self):
        self.idd=StringVar()
        self.f1=Frame(self.a,height=550,width=700,bg='black')
        self.f1.place(x=400,y=80)
        self.list2=("EVENT ID","DEPT ID","DEPT NAME","EVENT NAME","EVENT DATE")
        self.trees=self.create_tree(self.f1,self.list2,13)
        self.trees.place(x=70,y=130)


        l1=Label(self.f1,text='DEPT ID/EVENT ID : ',font='Calibri 15 bold',fg='white',bg='black').place(x=170,y=32)
        e1=Entry(self.f1,width=20,bd=4,bg='white',textvariable=self.idd).place(x=360,y=35)
        #l2=Label(self.f1,text='Student Id : ',font='Calibri 15 bold',fg='white',bg='black').place(x=50,y=80)
        #e2=Entry(self.f1,width=20,bd=4,bg='white',textvariable=self.astudentt).place(x=180,y=80)
        b1=Button(self.f1,text='Search',bg='black',fg='white',font='Calibri 10 bold',width=10,bd=3,command=self.searchev).place(x=100,y=450)
        b1=Button(self.f1,text='All',bg='black',fg='white',font='Calibri 10 bold',width=10,bd=3,command=self.searchallev).place(x=300,y=450)
        b1=Button(self.f1,text='Back',bg='black',fg='white',font='Calibri 10 bold',width=10,bd=3,command=self.rm).place(x=500,y=450)
        self.f1.grid_propagate(0)

    def searchev(self):
        self.list2=("EVENT ID","DEPT ID","DEPT NAME","EVENT NAME","EVENT DATE")
        self.trees=self.create_tree(self.f1,self.list2,13)
        self.trees.place(x=70,y=130)
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        bid=self.idd.get()
        #sid=self.astudentt.get()
        try:
            c=cursor.execute("""select e.eventid,e.deptid,d.name,e.ename,e.edate
                from events e join department d on e.deptid=d.deptid
                where e.DEPTID='{}' or e.EVENTID='{}'""".format(bid.upper(),bid.upper(),))
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

    def searchallev(self):
        self.list2=("EVENT ID","DEPT ID","DEPT NAME","EVENT NAME","EVENT DATE")
        self.trees=self.create_tree(self.f1,self.list2,13)
        self.trees.place(x=70,y=130)
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        try:
            c=cursor.execute("""select e.eventid,e.deptid,
                d.name,e.ename,e.edate
                from events e
                join department d 
                on e.deptid=d.deptid""")
            d=cursor.fetchall()
            for row in d:
                self.trees.insert("",END,values=row)

            conn.commit()

        except Exception as e:
            messagebox.showinfo("Error","There was a problem in finding the data")
        conn.close()

    def addnot(self):
        self.adminid=StringVar()
        self.noticeid=StringVar()
        self.boddy=StringVar()
        #self.termdate=StringVar()
        self.f1=Frame(self.a,height=500,width=650,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Admin ID : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=50)
        e1=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.adminid).place(x=150,y=50)
        l2=Label(self.f1,text='Notice ID : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=100)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.noticeid).place(x=150,y=100)
        l3=Label(self.f1,text='Body : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=150)
        e3=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.boddy).place(x=150,y=150)
        
        self.f1.grid_propagate(0)
        b1=Button(self.f1,text='Add',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.addnotdata).place(x=150,y=400)
        b2=Button(self.f1,text='Back',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.rm).place(x=350,y=400)

    def rm(self):
        self.f1.destroy()
    def mainmenu(self):
        self.root.destroy()
        #self.a.destroy()
        #self.a=self.canvases(image1)
        a=menu()

    def addnotdata(self):
        a=self.adminid.get()
        b=self.noticeid.get()
        c=self.boddy.get()
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        try:
            if (a and b and c)=="":
                messagebox.showinfo("Error","Fields cannot be empty.")
            else:
                cursor.execute("insert into notice \
                values ('{}','{}','{}',DATE_ADD(curdate(), INTERVAL 7 DAY))".format(a.upper(),b.upper(),c.upper(),))
                conn.commit()
                messagebox.showinfo("Success","Notice added successfully")
        except mysql.connector.IntegrityError:
            messagebox.showinfo("Error","Notice is already present.")


        conn.close()

    def addevent(self):
        self.eventid=StringVar()
        self.deptid=StringVar()
        self.ename=StringVar()

        self.f1=Frame(self.a,height=500,width=650,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Event ID : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=50)
        e1=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.eventid).place(x=150,y=50)
        l2=Label(self.f1,text='Dept ID : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=100)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.deptid).place(x=150,y=100)
        l2=Label(self.f1,text='Event Name : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=150)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.ename).place(x=150,y=150)

        
        self.f1.grid_propagate(0)
        b1=Button(self.f1,text='Add',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.addeventdata).place(x=150,y=400)
        b2=Button(self.f1,text='Back',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.rm).place(x=350,y=400)
    
    def addeventdata(self):
        a=self.eventid.get()
        b=self.deptid.get()
        c=self.ename.get()
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        try:
            if (a and b and c)=="":
                messagebox.showinfo("Error","Fields cannot be empty.")
            else:
                cursor.execute("insert into events \
                values ('{}','{}',curdate(),'{}')".format(a.upper(),b.upper(),c.upper(),))
                conn.commit()
                messagebox.showinfo("Success","Event added successfully")
        except mysql.connector.IntegrityError:
            messagebox.showinfo("Error","Event is already present.")


        conn.close()


    def delnot(self):
        self.adid=StringVar()

        self.f1=Frame(self.a,height=500,width=650,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Notice ID : ',font='Calibri 12 bold',fg='white',bg='Black',pady=1).place(x=50,y=50)
        e1=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.adid).place(x=150,y=50)
        
        self.f1.grid_propagate(0)
        b1=Button(self.f1,text='Delete',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.delnotdata).place(x=100,y=400)
        b2=Button(self.f1,text='Delete all',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.dellall).place(x=250,y=400)
        b2=Button(self.f1,text='Back',font='Calibri 10 bold',fg='white',bg='black',width=15,bd=3,command=self.rm).place(x=400,y=400)
    
    def dellall(self):
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        try:
            cursor.execute("delete from notice")
            conn.commit()
            messagebox.showinfo("Success","Notices deleted successfully")
        except:
            messagebox.showinfo("Error","There was some problem deleting the notices")

    def delnotdata(self):
        a=self.adid.get()
        conn=mysql.connector.connect(**config)
        cursor=conn.cursor()
        try:
            if a=="":
                messagebox.showinfo("Error","Field cannot be empty.")
            else:
                cursor.execute("delete from notice \
                where noticeid = '{}'".format(a,))
                conn.commit()
                messagebox.showinfo("Success","Notice deleted successfully")
        except mysql.connector.IntegrityError:
            messagebox.showinfo("Error","Notice is not present.")


        conn.close()






