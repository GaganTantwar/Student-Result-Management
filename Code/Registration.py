from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
import os
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="Hotpink")
    
        '''=== Side  Image ==='''
        
        self.left=ImageTk.PhotoImage(file="images/registernow.png")
        left=Label(self.root,image=self.left).place(x=100,y=50,width=500,height=600)
        
        '''&&&& FRAME &&&&'''
        frame1=Frame(self.root,bg="Navyblue")
        frame1.place(x=580,y=50,width=700,height=600)
        
        title=Label(frame1,text="Register Here",font=("Bahnschrift",20,"bold"),bg="Skyblue",fg="Red").place(x=50,y=30)

        f_name=Label(frame1,text="First Name",font=("Bahnschrift",15,"bold"),bg="yellow",fg="Red").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("Bahnschrift",15),bg="lightgray")
        self.txt_fname.place(x=50,y=150,width=250)

        l_name=Label(frame1,text="Last Name",font=("Bahnschrift",15,"bold"),bg="yellow",fg="Red").place(x=400,y=100)
        self.txt_lname=Entry(frame1,font=("Bahnschrift",15),bg="lightgray")
        self.txt_lname.place(x=400,y=150,width=250)

        contact=Label(frame1,text="Contact",font=("Bahnschrift",15,"bold"),bg="yellow",fg="Red").place(x=50,y=190)
        self.txt_contact=Entry(frame1,font=("Bahnschrift",15),bg="lightgray")
        self.txt_contact.place(x=50,y=240,width=250)

        email=Label(frame1,text="Email",font=("Bahnschrift",15,"bold"),bg="yellow",fg="Red").place(x=400,y=190)
        self.txt_email=Entry(frame1,font=("Bahnschrift",15),bg="lightgray")
        self.txt_email.place(x=400,y=240,width=250)

        question=Label(frame1,text="Security Question",font=("Bahnschrift",15,"bold"),bg="yellow",fg="Red").place(x=50,y=290)
         
        self.cmb_ques=ttk.Combobox(frame1,font=("Bahnschrift",13),state="readonly")
         
        self.cmb_ques['values']=("Select","Your Pet Name", "Your Bestfriend","Your Dog Name")
        self.cmb_ques.place(x=50,y=340,width=250)
        self.cmb_ques.current(0)


        answer=Label(frame1,text="Answer",font=("Bahnschrift",15,"bold"),bg="yellow",fg="Red").place(x=400,y=290)
        self.txt_ans=Entry(frame1,font=("Bahnschrift",15),bg="lightgray")
        self.txt_ans.place(x=400,y=340,width=250)

        password=Label(frame1,text="Password",font=("Bahnschrift",15,"bold"),bg="yellow",fg="Red").place(x=50,y=390)
        self.txt_password=Entry(frame1,font=("Bahnschrift",15),bg="lightgray")
        self.txt_password.place(x=50,y=430,width=250)

        c_pass=Label(frame1,text="Confirm Password",font=("Bahnschrift",15,"bold"),bg="yellow",fg="Red").place(x=400,y=390)
        self.txt_cpass=Entry(frame1,font=("Bahnschrift",15),bg="lightgray")
        self.txt_cpass.place(x=400,y=430,width=250)

        self.var_chk = IntVar()
        chk=Checkbutton(frame1,text='I Agree the Terms and Conditions',variable=self.var_chk,onvalue=1,offvalue=0,bg='white',font=('times new roman',12)).place(x=50,y=480)
        
        self.btn_img=ImageTk.PhotoImage(file="images/register.png")

        self.btn_register=Button(frame1,image=self.btn_img, bd=0, cursor="hand2", command=self.register_data).place(x=50, y=520),

        '''btn_register=Button(frame1,image=self.btn_img,bd=0,cursor='hand2',command=self.register_data).place(x=50,y=520)'''

        btn_login=Button(self.root,text="Sign In", font=("times new roman", 20),bg='Green',bd=0,cursor='hand2').place(x=300,y=520)

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpass.delete(0,END)
        self.cmb_ques.current(0)

    def register_data(self):
        if self.txt_fname.get()==""or self. txt_lname.get()=="" or self.txt_email.get()=="" or self.txt_contact.get()=="" or self.cmb_ques.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpass.get()=="":
            messagebox.showerror("Error","All Fields are Required", parent=self.root)
        elif self.txt_password.get()!=self.txt_cpass.get():
            messagebox.showerror("Error","Password and Confirm Password should be same", parent = self.root )
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please Agree", parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=?", (self.txt_email.get(),))
                row = cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error", "User Already Exists, Please try with another Email", parent=self.root)
                else:
                    cur.execute("INSERT INTO employee(f_name,l_name,contact,email,question,answer,password) VALUES(?,?,?,?,?,?,?)", (self.txt_fname.get(),self.txt_lname.get(),self.txt_contact.get(),self.txt_email.get(), self.cmb_ques.get(),self.txt_answer.get(), self.txt_password.get()
                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successfull", parent=self.root)
                    self.clear()
                    self.login_window()
                    # self.root.destroy()
                    # os.system("python login.py")
                            
            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}", parent=self.root)
                            
        




root=Tk()
obj=Register(root)
root.mainloop()