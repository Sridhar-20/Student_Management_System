from tkinter import *
from PIL import Image,ImageTk,ImageDraw #pip install pillow
from datetime import*
import time
from math import*
import sqlite3
#import pymysql  # pip install pymysql
from tkinter import messagebox,ttk
import os

class loginWindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#012e2f")

        left_lbl=Label(self.root,bg="#08A3D2",bd=0) 
        left_lbl.place(x=0,y=0,width=600,relheight=1)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relwidth=1,relheight=1)
          
        #========frame=============
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE",font=("TIMES NEW ROMAN",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        
        email=Label(login_frame,text="EMAIL ADDRESS",font=("TIMES NEW ROMAN",18,"bold"),bg="white",fg="GRAY").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("TIMES NEW ROMAN",15),bg="LIGHTGRAY")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        pass_=Label(login_frame,text="PASSWORD",font=("TIMES NEW ROMAN",18,"bold"),bg="white",fg="GRAY").place(x=250,y=250)
        self.txt_pass_=Entry(login_frame,font=("TIMES NEW ROMAN",15),bg="LIGHTGRAY")
        self.txt_pass_.place(x=250,y=280,width=350,height=35)

        btn_reg=Button(login_frame,command=self.register_window,text="Register new Account",font=("TIMES NEW ROMAN",14),bg="white",bd=0,fg="#B00857",cursor="hand2").place(x=250,y=320)
        btn_forget=Button(login_frame,command=self.forget_password,text="Forget Password",font=("TIMES NEW ROMAN",14),bg="white",bd=0,fg="red",cursor="hand2").place(x=450,y=320)

        btn_login=Button(login_frame,text="Login",command=self.login,font=("TIMES NEW ROMAN",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=250,y=380,width=180,height=40)

        #========clock========
        self.lbl=Label(self.root,text="\nClock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=90,y=120,width=350,height=450)
    
        self.working()

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)

    def forgetpassword(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con=sqlite3.connect(database="sms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and question=? and answe?",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select the correct Sercurity Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=? ",(self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","your password has been reset,Please login with new password",parent=self.root2)    
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)

    def forget_password(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="sms.db")
    
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid email to email address to reset your password",parent=self.root)
                else:
                    con.close() 
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
        
                    t=Label(self.root2,text="Forget Password",font=("TIMES NEW ROMAN",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
                    #------Forget Password-----#         
                    question=Label(self.root2,text="Sercurity Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)

                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state="readonly",justify=CENTER)
                    self.cmb_quest['values']=("Select","Your first Pet Name","Your birth place","your Best frnd name")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)

                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=180)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_answer.place(x=50,y=210,width=250)

                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=260)
                    self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_new_pass.place(x=50,y=290,width=250)

                    btn_change_password=Button(self.root2,text="Reset Password",command=self.forgetpassword,bg="green",fg="white",font=("TIMES NEW ROMAN",15,"bold")).place(x=90,y=340)
   
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="sms.db")
    
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)

                else:
                    messagebox.showinfo("Success",f"Welcome: {self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()    
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)

    def clock_img(self,hr,min,sec):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #====For clk img===
        bg=Image.open("images/c.png")
        bg=bg.resize((300,300)) 
        clock.paste(bg,(50,50))
        #====hr line img====
        origin=(200,200)
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
         #====min line img====
        draw.line((origin,200+80*sin(radians(min)),200-80*cos(radians(min))),fill="white",width=3)
         #====sec line img====
        draw.line((origin,200+100*sin(radians(sec)),200-100*cos(radians(sec))),fill="yellow",width=2)
        draw.ellipse((195,195,205,205),fill="lightblue")
        clock.save("clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min=(m/60)*360
        sec=(s/60)*360
        #print(h,m,s)
        #print(hr,min,sec)
        self.clock_img(hr,min,sec)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

root=Tk()
obj=loginWindow(root)
root.mainloop()