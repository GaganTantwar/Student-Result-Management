from tkinter import* 
from PIL import Image,ImageTk,ImageDraw #pip install Pillow
from datetime import* 
import time 
from math import*
# import pymysql
import sqlite3
from tkinter import messagebox, ttk
import os

class Login_window:
  def __init__(self,root):
    
    self.root=root 
    self.root.title("Login System")
    self.root.geometry("1350x700+0+0")
    self.root.config(bg="#021e2f")

    title=Label(self.root,text="Webcode Analog Clock",font=("times new roman",50,"bold"),bg="#04444a",fg="white").place(x=0,y=50,relwidth=1)


# background


    left_lbl=Label(self.root,bg="#08A3D2",bd=0,)
    left_lbl.place(x=0,y=0,relheight=1,width=600)

    right_lbl=Label(self.root,bg="#031F3C",bd=0,)
    right_lbl.place(x=600,y=0,relheight=1,relwidth=1)



  # FRAMES

    login_frame= Frame(self.root, bg="white")
    login_frame.place(x=250,y=100,width=800, height=500)
    # login frame widgets
    title=Label(login_frame,text="Login Here",font=("times new roman",30,"bold"), bg="white", fg="#08A3D2").place(x=250, y=50)

    email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"), bg="white", fg="gray").place(x=250, y=150)
    self.txt_email=Entry(login_frame, font=("times new roman", 18, "bold"), bg="lightgray")
    self.txt_email.place(x=250, y=190, width=350, height=35)

    pswd=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"), bg="white", fg="gray").place(x=250, y=250)
    self.txt_pswd=Entry(login_frame, font=("times new roman", 18, "bold"), bg="lightgray")
    self.txt_pswd.place(x=250, y=290, width=350, height=35)

    btn_reg = Button(login_frame, cursor="hand2", text="Register new Account?", command=self.register_window, font=("times new roman", 14), bg="white", bd=0, fg="#B00857").place(x=250, y=330)

    btn_fgt = Button(login_frame, cursor="hand2", text="Forget Password", command=self.forget_password_window, font=("times new roman", 14), bg="white", bd=0, fg="red").place(x=480, y=330)

    btn_lgn = Button(login_frame, cursor="hand2", text="Login", command=self.login, font=("times new roman", 20, "bold"), fg="white", bg="#B00857").place(x=250, y=380, width=180, height=40)




    # clock


    self.lbl=Label(self.root, text = "WebCode Clock", font=("Book Antiqua", 25, "bold"), compound=BOTTOM, fg="white",bg="#081923",bd=0,)
    self.lbl.place(x=90,y=120,height=450,width=350)
   
    
    self.working()


  def reset(self):
    self.cmb_ques.current(0)
    self.txt_new_pass.delete(0,END)
    self.txt_ans.delete(0,END)
    self.txt_pswd.delete(0,END)
    self.txt_email.delete(0,END)




  def forget_password(self):
    # self.txt_email.get(), self.cmb_ques.get(), self.txt_ans.get(), self.txt_pswd.get()

    if self.cmb_ques.get()=="" or self.txt_ans.get()=="" or self.txt_new_pass.get()=="":
      messagebox.showerror("Error", "Please fill all fields", parent=self.root2)

    else:
      try:
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        cur.execute("select * from employee where email=? and question = ? and answer = ?", (self.txt_email.get(), self.cmb_ques.get(), self.txt_ans.get()))
        row=cur.fetchone()
        if row!=None:
          cur.execute("update employee set password=? where email=?", (self.txt_new_pass.get(), self.txt_email.get()))
          con.commit()
          con.close()
          messagebox.showinfo("Success", "Password updated successfully", parent=self.root2)
          self.reset()
          self.root2.destroy()



        else:
          messagebox.showerror("Error","Please select the correct Security Question /  Enter Answer",parent=self.root2)

      except Exception as es:
        messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)



  def forget_password_window(self):
    if self.txt_email.get()=="":
        messagebox.showerror("Error", "Please enter the email address to reset your password", parent=self.root)
    else:
      try:
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        cur.execute("select * from employee where email=?", (self.txt_email.get(),))
        row=cur.fetchone()
        if row!=None:
          con.close()
          self.root2=Toplevel()
          self.root2.title("Forget Password")
          self.root2.geometry("400x400+450+150")
          self.root2.config(bg="white")
          self.root2.focus_force()
          self.root2.grab_set()

          t = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)

          question=Label(self.root2,text="Security Question",font=("Bahnschrift",15,"bold"),bg="white",fg="gray").place(x=50,y=100)

          self.cmb_ques=ttk.Combobox(self.root2,font=("Bahnschrift",13),state="readonly", justify=CENTER)

          self.cmb_ques['values']=("Select","Your Pet Name", "Your Bestfriend","Your Birth Place")
          self.cmb_ques.place(x=50,y=130,width=250)
          self.cmb_ques.current(0)


          answer=Label(self.root2,text="Answer",font=("Bahnschrift",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
          self.txt_ans=Entry(self.root2,font=("Bahnschrift",15),bg="lightgray")
          self.txt_ans.place(x=50,y=210,width=250)


          new_pass=Label(self.root2,text="New Password",font=("Bahnschrift",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
          self.txt_new_pass=Entry(self.root2,font=("Bahnschrift",15),bg="lightgray")
          self.txt_new_pass.place(x=50,y=290,width=250)

          btn_change_pswd = Button(self.root2, text="Reset Password", command=self.forget_password, bg="green", fg="white", font=("times new roman", 15, "bold")).place(x=80, y=340)

          # messagebox.showinfo("Success","Welcome",parent=self.root)
        else:
          messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root)

      except Exception as es:
        messagebox.showerror("Error", f"Error:{str(es)}",parent=self.root)
        # messagebox.showerror("Error", "Please enter the valid email address to reset your password", parent=self.root)
    


  def register_window(self):
    self.root.destroy()
    import Registration

  def login(self):
    if self.txt_email.get()=="" or self.txt_pswd.get()=="":
      messagebox.showerror("Error","All fields are required",parent=self.root)
    else:
      try:
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        cur.execute("select * from employee where email=? and password=?", (self.txt_email.get(), self.txt_pswd.get()))
        row=cur.fetchone()
        if row!=None:
          messagebox.showinfo("Success",f"Welcome: {self.txt_email.get()}",parent=self.root)
          self.root.destroy()
          os.system("python dashboard.py")
        else:
          messagebox.showerror("Error","Invalid Email or Password",parent=self.root)
        con.close()

      except Exception as es:
        messagebox.showerror("Error", f"Error:{str(es)}",parent=self.root)






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



root=Tk()
obj=Login_window(root)
root.mainloop()
