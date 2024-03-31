from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import numpy as np
import mysql.connector
from register import register
from Page import Face_Recognization_system


class login:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        #self.root.geometry("1530x790+0+0")
        self.root.title("Login Page")

        self.Email=StringVar()
        self.Password=StringVar()
        self.Security_Question=StringVar()
        self.Security_Answer=StringVar()
        self.New_Password=StringVar()
        self.VConfirm_Password=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\img1.jpg")
        label_bg=Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relwidth=1,relheight=2)

        Frame1 = Frame(self.root, bg="white")
        Frame1.place(x=610, y=170, width=340, height=450)

        Frame0 = Frame(Frame1,bd=2,bg="white",relief=RIDGE)
        Frame0.place(x=5, y=70, width=325, height=370)


        title = Label(Frame1, text="Login In", font=("liquid crystal", 38), bg="Darkred", fg="white")
        title.place(x=0, y=0, relwidth=1)

        Email = Label(Frame1,text= "Email : ",font=("liquid crystal", 15, "bold"))
        Email.place(x=60,y=175)

        self.Email_box = ttk.Entry(Frame1,width=20,textvariable=self.Email,font=("liquid crystal", 12, "bold"))
        self.Email_box.place(x=30,y=200,width=270)

        password = Label(Frame1,text= "Password : ",font=("liquid crystal", 15, "bold"))
        password.place(x=60,y=245)

        self.password_box = ttk.Entry(Frame1,width=20,textvariable=self.Password,font=("liquid crystal", 12, "bold"))
        self.password_box.place(x=30,y=270,width=270)

        img2 = Image.open(r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\img2.png")
        img2=img2.resize((30,30),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lb1 = Label(image=self.photoimage2,bg="black",borderwidth=0)
        lb1.place(x=640,y=345,width=30,height=25)

        img3 = Image.open(r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\img3.png")
        img3=img3.resize((30,30),Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lb1 = Label(image=self.photoimage3,bg="black",borderwidth=0)
        lb1.place(x=640,y=415,width=30,height=25)

        img4 = Image.open(r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\1920x1080-icon-symbol-or-website-admin-social-login-element-concept-3d-rendering-png.png")
        img4=img4.resize((90,90),Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img4)
        lb1 = Label(image=self.photoimage4,bg="white",borderwidth=0)
        lb1.place(x=700,y=255,width=150,height=75)

        #login in button
        login_button = Button(Frame1,command=self.login,text="Login",font=("liquid crystal", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activebackground="red",activeforeground="white")
        login_button.place(x=110,y=320,width=120,height=35)

        #Exit
        Exit = Button(self.root,command=self.exit,text="Exit",font=("liquid crystal", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activebackground="red",activeforeground="white")
        Exit.place(x=0,y=0,width=120,height=35)

        #Register
        login_button = Button(Frame1,text="Register New User",command = self.reg_window ,font=("liquid crystal", 12, "bold"),borderwidth=0,fg="black",bg="white",activebackground="white",activeforeground="black")
        login_button.place(x=15,y=370,width=160)

        #Forgot
        login_button = Button(Frame1,text="Forgot Password",command= self.forgot,font=("liquid crystal", 12, "bold"),borderwidth=0,fg="black",bg="white",activebackground="white",activeforeground="black")
        login_button.place(x=10,y=400,width=160)

    def exit(self):
            self.root.destroy()

    def login(self):
        if self.Email.get()=="" or self.Password.get()=="":
            messagebox.showerror("Error","All fields required")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="Ur password",database="register")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where Email=%s and Password=%s",(
            self.Email.get(),
            self.Password.get()
            ))

            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Email/Password")
            else:
                self.new_window = Toplevel(self.root)  
                self.app = Face_Recognization_system(self.new_window)
            
            conn.commit()
            conn.close()
    
    def forgot(self):
        if self.Email.get()=="":
            messagebox.showerror("Error","Email field is required")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="Ur password",database="register")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where Email=%s",(
            self.Email.get(),
            ))

            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Email")
            else:
                self.new_window = Toplevel(self.root)
                self.new_window.title("Forget Password") 
                self.new_window.geometry("335x375+610+260")

                Frame_ = Frame(self.new_window,bd=2,bg="white",relief=RIDGE)
                Frame_.place(x=5, y=0, width=320, height=370)

                title_ = Label(Frame_, text="Forgot Password", font=("liquid crystal", 19,"bold"), bg="Darkred", fg="white")
                title_.place(x=0, y=0, relwidth=1)

                #Security Question
                Security_Question = Label( Frame_,text= "Security Question ",font=("liquid crystal",15))
                Security_Question.place(x=0, y=50, relwidth=1)
                Security_Question=ttk.Combobox( Frame_,textvariable=self.Security_Question,font=("liquid crystal",15),width=17)
                Security_Question["values"]=("SELECT","Favourite Number","Favourite Colour","Favourite Food","Other")
                Security_Question.current(0)
                Security_Question.place(x=0, y=80, relwidth=1)

                #Security_Answer
                Security_Answer = Label( Frame_,text= "Security Answer : ",font=("liquid crystal",15))
                Security_Answer.place(x=0, y=110 ,relwidth=1)

                Security_Answer_box = ttk.Entry( Frame_,width=20,textvariable=self.Security_Answer,font=("liquid crystal",15))
                Security_Answer_box.place(x=0, y=140, relwidth=1)

                #New Password
                New_Password = Label( Frame_,text= "New Password : ",font=("liquid crystal",15))
                New_Password.place(x=0, y=170 ,relwidth=1)

                New_Password_box = ttk.Entry( Frame_,width=20,textvariable=self.New_Password,font=("liquid crystal",15))
                New_Password_box.place(x=0, y=200, relwidth=1)

                #Verify New Password
                VNew_Password = Label( Frame_,text= "Confirm New Password : ",font=("liquid crystal",15))
                VNew_Password.place(x=0, y=230 ,relwidth=1)

                VNew_Password_box = ttk.Entry( Frame_,width=20,textvariable=self.VConfirm_Password,font=("liquid crystal",15))
                VNew_Password_box.place(x=0, y=260, relwidth=1)

                save_button = Button(Frame_,command=self.new_password,text="Save",font=("liquid crystal", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activebackground="red",activeforeground="white")
                save_button.place(x=50,y=290,width=120,height=35)

                conn.commit()
                conn.close()


    def new_password(self):
        if self.New_Password.get() != self.VConfirm_Password.get():
            messagebox.showerror("Error","Password and Verify Password must be same",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="Ur password",database="register")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where Security_Question=%s and Security_Answer= %s",(
            self.Security_Question.get(),
            self.Security_Answer.get()
            ))

            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Security Answer")
            else:
                querry = ("Update register set Password=%s where Email=%s")
                value = (self.New_Password.get(),self.Email.get()) 
                my_cursor.execute(querry,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Password Saved",parent=self.root)

            

    def reg_window(self):
        self.new_window = Toplevel(self.root)  
        self.app = register(self.new_window)


if __name__ == "__main__":

    root = Tk()
    obj = login(root)
    root.mainloop()
