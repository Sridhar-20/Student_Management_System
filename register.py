from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install pillow
#import pymysql #pip install pymysql
import sqlite3
import os

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.bg_img=Image.open("images/b2.png")
        self.bg_img=self.bg_img.resize((1250,700))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        #self.root.config(bg="#ffffff")
        self.lbl_bg_img=Label(self.root,image=self.bg_img,bd=0).place(x=250,y=0,relheight=1,relwidth=1)

        self.left=Image.open("images/side.png") 
        #self.bg_img=self.bg_img.resize((1250,700))
        self.left=ImageTk.PhotoImage(self.left)
        #self.root.config(bg="#ffffff")
        self.lbl_left=Label(self.root,image=self.left).place(x=80,y=100,height=500,width=400)

        #=============register========
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame1,text="Contact",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        Email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_Email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_Email.place(x=370,y=200,width=250)

        question=Label(frame1,text="Sercurity Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
        self.cmb_quest['values']=("Select","Your first Pet Name","Your birth place","your Best frnd name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)

        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",15),bg="white").place(x=50,y=380)

        self.btn_img=ImageTk.PhotoImage(file="images/register.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)

        btn_log=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",20),bd=2,bg="lightgray",cursor="hand2").place(x=200,y=500,width=180)

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")
    
    def clear(self):
         self.txt_fname.delete(0,END)
         self.txt_lname.delete(0,END)
         self.txt_contact.delete(0,END)
         self.txt_Email.delete(0,END)
         self.txt_answer.delete(0,END)
         self.txt_password.delete(0,END)
         self.txt_cpassword.delete(0,END)
         self.cmb_quest.current(0)
    
    def register_data(self):
        if self.txt_fname.get()=="" or  self.txt_contact.get()=="" or self.txt_Email.get()=="" or self.cmb_quest.get()=="Select"or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Pass word and Confirm password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="sms.db")
                cur=con.cursor() 
                cur.execute("Select * from employee where email=?",(self.txt_Email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exist",parent=self.root)
                else:
                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",
                            (self.txt_fname.get(),
                             self.txt_lname.get(),
                             self.txt_contact.get(),
                             self.txt_Email.get(),
                             self.cmb_quest.get(),
                             self.txt_answer.get(),
                             self.txt_password.get()
                    ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Register Successful",parent=self.root)
                self.clear()
                self.login_window()
            except Exception as ex:
                #print(ex)
                messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
                
root=Tk()
obj=Register(root)
root.mainloop()