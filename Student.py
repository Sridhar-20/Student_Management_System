from tkinter import *
from typing import Text
from PIL import Image, ImageTk # type: ignore #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_Email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        self.var_address=StringVar()
    
        title=Label(self.root,text="Student Details",font=("Times New Roman",15,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)

        #=======Column1=======#
        lbl_Roll=Label(self.root,text="Roll No",font=("Times New Roman",15,"bold"),bg="white").place(x=10,y=60)
        lbl_Name=Label(self.root,text="Name",font=("Times New Roman",15,"bold"),bg="white").place(x=10,y=100)
        lbl_Email=Label(self.root,text="Email",font=("Times New Roman",15,"bold"),bg="white").place(x=10,y=140)
        lbl_Gender=Label(self.root, text="Gender",font=("Times New Roman", 15,"bold"),bg="white").place( x=10,y=180)
        lbl_State=Label(self.root, text="State",font=("Times New Roman", 15,"bold"),bg="white").place( x=10,y=220)
        txt_State=Entry(self.root,textvariable=self.var_state,font=("Times New Roman",15,"bold"),bg="lightyellow").place(x=150,y=220,width=150)
        lbl_city=Label(self.root, text="City",font=("Times New Roman", 15,"bold"),bg="white").place( x=320,y=220)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("Times New Roman",15,"bold"),bg="lightyellow").place(x=380,y=220,width=100)     
        lbl_pin=Label(self.root, text="Pin",font=("Times New Roman", 15,"bold"),bg="white").place( x=500,y=220)
        txt_pin=Entry(self.root,textvariable=self.var_pin,font=("Times New Roman",15,"bold"),bg="lightyellow").place(x=550,y=220,width=120)

        lbl_Address=Label(self.root, text="Address",font=("Times New Roman", 15,"bold"),bg="white").place( x=10,y=260)

        #lbl_Gender=ttk.Label(self.root, text="Enter your comment :",font=("Times New Roman", 15)).grid(column=0, row=15, padx=10, pady=25)

        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("Times New Roman",15,"bold"),bg="lightyellow")
        self.txt_roll.place(x=150,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("Times New Roman",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        txt_Email=Entry(self.root,textvariable=self.var_Email,font=("Times New Roman",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.txt_Gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),font=("Times New Roman",15,"bold"),state='readonly',justify=CENTER)
        self.txt_Gender.place(x=150,y=180,width=200)
        self.txt_Gender.current(0)
                
        #====column2=====#
        lbl_DOB=Label(self.root,text="D.O.B",font=("Times New Roman",15,"bold"),bg="white").place(x=360,y=60)
        lbl_contact=Label(self.root,text="Contact",font=("Times New Roman",15,"bold"),bg="white").place(x=360,y=100)
        lbl_admission=Label(self.root,text="Admission",font=("Times New Roman",15,"bold"),bg="white").place(x=360,y=140)
        lbl_course=Label(self.root, text="Course",font=("Times New Roman", 15,"bold"),bg="white").place( x=360,y=180)

        #========Entry==========
        self.course_list=[]
        #========Function call==============
        self.fetch_course()
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("Times New Roman",15,"bold"),bg="lightyellow").place(x=480,y=60,width=200)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("Times New Roman",15,"bold"),bg="lightyellow").place(x=480,y=100,width=200)
        txt_=Entry(self.root,textvariable=self.var_a_date,font=("Times New Roman",15,"bold"),bg="lightyellow").place(x=480,y=140,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("Times New Roman",15,"bold"),state='readonly',justify=CENTER)
        self.txt_course.place(x=480,y=180,width=200)
        self.txt_course.set("Select")

        #self.txt_address=Text(self.root, width=20, height=3)
        #self.txt_address.grid(column=1, row=15)
        txt_address=Entry(self.root,textvariable=self.var_address,font=("Times New Roman",15,"bold"),bg="lightyellow").place(x=150,y=260,width=530)
        #self.txt_address =Text(self.root,width=40,height=4)
        #self.txt_address.grid(row=1,column=2)
        
        #self.txt_description=Text(self.root)
        #self.txt_description.grid(column=1,row=15)

        #self.txt_description.place(x=150,y=180,width=500,height=130)
        #self.txt_address = Text(self.root, font=("Times New Roman", 15, "bold"), bg="lightyellow")
        #self.txt_address.place(x=150, y=260, width=500, height=100)
        #self.txt_description = Text(self.root,width=500,height=100)

        self.btn_add=Button(self.root,text="save",font=("goudy old style",15),bg="#0B5377",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15),bg="#0B5377",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg="#0B5377",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="#0B5377",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        #===========Search Panel========
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root,text="Roll No",font=("Times New Roman",15,"bold"),bg="white").place(x=720,y=60)
        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("Times New Roman",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        btn_search=Button(self.root,text="search",font=("goudy old style",15),bg="#0B5377",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
                
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollz=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollz.set,yscrollcommand=scrolly.set)
        scrollz.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollz.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("roll",text="Roll No")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("admission",text="admission")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="Citty")
        self.CourseTable.heading("pin",text="PIN")
        self.CourseTable.heading("address",text="Address")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("roll",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("email",width=100)
        self.CourseTable.column("gender",width=100)
        self.CourseTable.column("dob",width=100)
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("admission",width=100)
        self.CourseTable.column("course",width=100)
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("city",width=100)
        self.CourseTable.column("pin",width=100)
        self.CourseTable.column("address",width=200)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set(""),
        self.var_Email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set("Select"),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.var_address.set("")
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll no should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Pleasde select the student from list",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted Succesfully",parent=self.root)
                        self.clear()                        
        except Exception as ex:
                    messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from student where roll=?",(self.var_search.get(),))
            rows=cur.fetchone()
            if rows!=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('',END,values=rows)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        # print(row)
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_Email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.var_address.set(row[11])

    def add(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll no already present",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_Email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.var_address.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll number should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
                        self.var_name.get(),
                        self.var_Email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.var_address.get(),
                        self.var_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student update Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def show(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
    def fetch_course(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            self.course_list=[]
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
            #print(v)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
