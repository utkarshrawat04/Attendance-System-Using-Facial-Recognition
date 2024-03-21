from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime


class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")
        self.root.title("Register Page")


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\img1.jpg")
        label_bg=Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.First_Name=StringVar()
        self.Last_Name=StringVar()
        self.Contact_NO=StringVar()
        self.Email=StringVar()
        self.Password=StringVar()
        self.Confirm_Password=StringVar()
        self.Security_Question=StringVar()
        self.Security_Answer=StringVar()


        Frame1 = Frame(self.root, bd=2, relief=RIDGE)
        Frame1.place(x=570, y=170, width=440, height=490)

        Frame2 = Frame(Frame1, bd=2, relief=RIDGE)
        Frame2.place(x=10, y=60, width=410, height=400)

        title = Label(self.root, text="Register", font=("liquid crystal", 40), bg="darkred", fg="white")
        title.place(x=0, y=0, relwidth=1)

        title1 = Label(Frame1, text="Enter Details", font=("liquid crystal", 30), bg="darkred", fg="white")
        title1.place(x=0, y=0, relwidth=1)

        #First Name
        First_Name = Label(Frame2,text= "First Name : ",font=("liquid crystal", 12, "bold"))
        First_Name.grid(row=2,column=0,padx=10,pady =5)

        First_Name_box = ttk.Entry( Frame2,width=20,textvariable=self.First_Name,font=("liquid crystal", 12, "bold"))
        First_Name_box.grid(row=3,column=0,padx=10,pady =5)

        #Last_Name
        Last_Name = Label( Frame2,text= "Last Name : ",font=("liquid crystal", 12, "bold"))
        Last_Name.grid(row=4,column=0,padx=10,pady =5)

        Last_Name_box = ttk.Entry( Frame2,width=20,textvariable=self.Last_Name,font=("liquid crystal", 12, "bold"))
        Last_Name_box.grid(row=5,column=0,padx=10,pady =5)

        #Contact_NO
        Contact_NO = Label( Frame2,text= "Contact NO. : ",font=("liquid crystal", 12, "bold"))
        Contact_NO.grid(row=6,column=0,padx=10,pady =5)

        Contact_NO_box = ttk.Entry( Frame2,width=20,textvariable=self.Contact_NO,font=("liquid crystal", 12, "bold"))
        Contact_NO_box.grid(row=7,column=0,padx=10,pady =5)

        #Email
        Email = Label( Frame2,text= "Email : ",font=("liquid crystal", 12, "bold"))
        Email.grid(row=8,column=0,padx=10,pady =5)

        Email_box = ttk.Entry( Frame2,width=20,textvariable=self.Email,font=("liquid crystal", 12, "bold"))
        Email_box.grid(row=9,column=0,padx=10,pady =5)

        #Password
        Password = Label( Frame2,text= "Password : ",font=("liquid crystal", 12, "bold"))
        Password.grid(row=2,column=1,padx=10,pady =5)

        Password_box = ttk.Entry( Frame2,width=20,textvariable=self.Password,font=("liquid crystal", 12, "bold"))
        Password_box.grid(row=3,column=1,padx=10,pady =5)

        #Confirm Password
        Confirm_Password = Label( Frame2,text= "Confirm Password : ",font=("liquid crystal", 12, "bold"))
        Confirm_Password.grid(row=4,column=1,padx=10,pady =5)

        Confirm_Password_box = ttk.Entry( Frame2,width=20,textvariable=self.Confirm_Password,font=("liquid crystal", 12, "bold"))
        Confirm_Password_box.grid(row=5,column=1,padx=10,pady =5)

        #Security Question
        Security_Question = Label( Frame2,text= "Security Question : ",font=("liquid crystal", 12, "bold"))
        Security_Question.grid(row=6,column=1,padx=10,pady =5)
        Security_Question=ttk.Combobox( Frame2,textvariable=self.Security_Question,font=("liquid crystal", 12, "bold"),width=17)
        Security_Question["values"]=("SELECT","Favourite Number","Favourite Colour","Favourite Food","Other")
        Security_Question.current(0)
        Security_Question.grid(row=7,column=1,padx=10,pady =5)

        #Security_Answer
        Security_Answer = Label( Frame2,text= "Security Answer : ",font=("liquid crystal", 12, "bold"))
        Security_Answer.grid(row=8,column=1,padx=10,pady =5)

        Security_Answer_box = ttk.Entry( Frame2,width=20,textvariable=self.Security_Answer,font=("liquid crystal", 12, "bold"))
        Security_Answer_box.grid(row=9,column=1,padx=10,pady =5)

        #Register button
        Register = Button(Frame2,text="Register", command=self.register ,font=("liquid crystal", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activebackground="red",activeforeground="white")
        Register.place(x=250,y=300,width=120,height=35)
        

    def register(self):
            if self.Security_Question.get()=="SELECT" or self.Last_Name.get()=="" or self.Password.get()=="" or self.Confirm_Password.get()=="" or self.Security_Answer.get()=="":
                messagebox.showerror("Error","Not all field filled",parent=self.root)

            elif self.Confirm_Password.get() != self.Password.get():
                messagebox.showerror("Error","Password and Confirm Password must be same",parent=self.root)
                
            else:
                try:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Utk222004",database="register")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.First_Name.get(),
                    self.Last_Name.get(),
                    self.Contact_NO.get(),
                    self.Email.get(),
                    self.Password.get(),
                    self.Security_Question.get(),
                    self.Security_Answer.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Data Saved",parent=self.root)

                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)




        





if __name__ == "__main__":
    root = Tk()
    obj = register(root)
    root.mainloop()

