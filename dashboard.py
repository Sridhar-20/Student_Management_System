from tkinter import *
from tkinter import BOTTOM, X, Button, Label, LabelFrame, Place, Tk, Toplevel
from PIL import Image,ImageTk,ImageDraw #pip install pillow
from course import CourseClass
from Student import studentClass
from Result import ResultClass 
from report import ReportClass
from tkinter import messagebox
import os
from datetime import*
import time
from math import*
import sqlite3

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #===icons=====
        self.logo_dash=ImageTk.PhotoImage(file="images/download (2).png")

        title=Label(self.root,text="Student Result Management System",padx=10,compound="left",image=self.logo_dash,font=("Times New Roman",22,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        
        M_Frame=LabelFrame(self.root,text="Menus",font=("Times New Roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15),bg="#0B5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_Student=Button(M_Frame,text="Student",font=("goudy old style",15),bg="#0B5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_Result=Button(M_Frame,text="Result",font=("goudy old style",15),bg="#0B5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_View=Button(M_Frame,text="View Student Result",font=("goudy old style",15),bg="#0B5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_Logout=Button(M_Frame,text="Logout",font=("goudy old style",15),bg="#0B5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_Exit=Button(M_Frame,text="Exit",font=("goudy old style",15),bg="#0B5377",fg="white",cursor="hand2",command=self.exit).place(x=1120,y=5,width=200,height=40)

        self.bg_img=Image.open("images/download (1).png")
        self.bg_img=self.bg_img.resize((920,350))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief="ridge",bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),bd=10,relief="ridge",bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)
        
        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief="ridge",bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)

        #========clock========
        self.lbl=Label(self.root,text="\nClock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=10,y=180,width=350,height=450)
    
        self.working()

        footer=Label(self.root,text="SRMS-Student Result Management System/n Contact Us for any Techincal Issue: 9515xxxx14",font=("Times New Roman",15),bg="#033054",fg="white").pack(side=BOTTOM,fill=X)        
        self.update_details()

    #==========================================
    def update_details(self):
        con=sqlite3.connect(database="sms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            
            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
            
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
            
            self.lbl_course.after(200,self.update_details)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    
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

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)
    def add_report(self):
       self.new_win=Toplevel(self.root)
       self.new_obj=ReportClass(self.new_win)
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()