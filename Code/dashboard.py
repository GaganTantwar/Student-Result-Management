from tkinter import *
from PIL import Image,ImageTk
from course import CourseClass 
from student import StudentClass
from result import ResultClass
from report import ReportClass
from tkinter import messagebox, ttk
from PIL import Image,ImageTk,ImageDraw #pip install Pillow
import os
from datetime import* 
import time 
import sqlite3 
from math import*
class Result_Management:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1950x750+0+0")
        self.root.config(bg="Skyblue")
        
        '''^^^^ Icons ^^^^'''
        self.logo=ImageTk.PhotoImage(file="images/logo_p.png")
        '''****Title****'''
        title=Label(self.root,text="Welcome to Student Result Management System",padx=15,compound=LEFT,image=self.logo,font=("Bookman Old Style",25,"bold"),bg="Hotpink",fg="Black").place(x=0,y=0,relwidth=1,height=50)
        '''&&&& Menus &&&&'''
        M_Frame=LabelFrame(self.root,text="Menus",font=("Nyala",15),bg="Grey",fg="Yellow")
        M_Frame.place(x=0,y=70,width=1950,height=80)

        '''$$$$ Buttons in Menus $$$$'''
        btn_course=Button(M_Frame,text="Course",font=("Bahnschrift",18,"bold"),bg="Red",fg="Black",cursor="hand2", command=self.add_course).place(x=15,y=5,width=150,height=40)
        btn_student=Button(M_Frame,text="Student",font=("Bahnschrift",18,"bold"),bg="Red",fg="Black",cursor="hand2", command=self.add_student).place(x=275,y=5,width=150,height=40)
        btn_result=Button(M_Frame,text="Result",font=("Bahnschrift",18,"bold"),bg="Red",fg="Black",cursor="hand2",command=self.add_result).place(x=530,y=5,width=150,height=40)
        btn_view=Button(M_Frame,text="View Result",font=("Bahnschrift",18,"bold"),bg="Red",fg="Black",cursor="hand2", command=self.add_report).place(x=800,y=5,width=180,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("Bahnschrift",18,"bold"),bg="Red",fg="Black",cursor="hand2").place(x=1100,y=5,width=150,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("Bahnschrift",18,"bold"),bg="Red",fg="Black",cursor="hand2").place(x=1350,y=5,width=150,height=40)

        # content
        
        self.bg_img=Image.open("images/background1.png")
        self.bg_img=self.bg_img.resize((920, 350))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        '''#### Update Details ####'''

        self.lbl_course=Label(self.root,text="Total Courses \n[0]",font=("Bookman Old Style",20),bd=10,relief=RIDGE,bg="Blue",fg="White").place(x=400,y=530,width=300,height=100)
        self.lbl_cstudent=Label(self.root,text="Total Students \n[0]",font=("Bookman Old Style",20),bd=10,relief=RIDGE,bg="Purple",fg="White").place(x=710,y=530,width=300,height=100)
        self.lbl_course=Label(self.root,text="Total Courses \n[0]",font=("Bookman Old Style",20),bd=10,relief=RIDGE,bg="Green",fg="White").place(x=1020,y=530,width=300,height=100)


        '''---clock---'''
        self.lbl=Label(self.root, text = "Clock", font=("Book Antiqua", 25, "bold"), compound=BOTTOM, fg="white",bg="#081923",bd=0,)
        self.lbl.place(x=50,y=180,height=450,width=350)
    
        self.working()

        '''----Footer----'''

        footer=Label(self.root,text="S.R.M.S-Student Result Management System \n Contact Us for any Technical Issue:89xxxxxx71",font=("Bookman Old Style",15,),bg="White",fg="Black").pack(side=BOTTOM,fill=X)

        self.update_detail()

    def update_detail(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses \n[{len(cr)}]")
            self.lbl_course.after(200, self.update_detail)

            cur.execute("Select * from student")
            st=cur.fetchall()
            self.lbl_cstudent.config(text=f"Total Students \n[{len(st)}]")
            self.lbl_cstudent.after(200, self.update_detail)

            cur.execute("Select * from result")
            re=cur.fetchall()
            self.lbl_result.config(text=f"Total Results \n[{len(re)}]")
            self.lbl_result.after(200, self.update_detail)

            con.close()
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")



    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)

        #==== for clock image

        bg=Image.open("images/c.png")
        bg=bg.resize((300,300),Image.Resampling.LANCZOS)
        clock.paste(bg,(50,50))

        #Formula To Rotate the Clock
        #angle_in_radians = angle_in_degrees * math.pi / 180
        #line_length = 100
        #center_x = 250
        #center_y = 250
        # end_x = center_x + line_length * math.cos(angle_in_radians)
        #end_y = center_y + line_length * math.sin(angle_in_radians)

        #== Hour line image===

        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)

        #== Min line image===
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)

        #== Sec line image===
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)

        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("images/clock_new.png")



    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second 

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        # print(h,m,s)
        # print(hr,min_,sec_)

        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)



    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = ReportClass(self.new_win)
    
    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def Exit(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op==True:
            self.root.destroy()


if __name__=='__main__':
    root=Tk()
    obj=Result_Management(root)
    root.mainloop()
    