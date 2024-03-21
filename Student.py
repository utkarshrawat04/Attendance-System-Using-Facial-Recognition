from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import *

import cv2



class student:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        #self.root.geometry("1530x790+0+0")
        self.root.title("Student Detail")


        self.var_dep=StringVar()
        self.var_Id=StringVar()
        self.var_Year=StringVar()
        self.var_semester=StringVar()
        self.var_name=StringVar()
        self.var_division=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_DOB=StringVar()
        self.var_Email=StringVar()
        self.var_Phone=StringVar()
        self.var_Address=StringVar()

        self.var_SearchBY=StringVar()
        self.var_find=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\img1.jpg")
        label_bg=Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relwidth=1,relheight=1)



        title = Label(self.root, text="Student Detail", font=("liquid crystal", 30), bg="darkred", fg="white")
        title.place(x=0, y=0, relwidth=1)

        Frame1 = Frame(self.root, bd=2, relief=RIDGE)
        Frame1.place(x=20, y=60, width=1480, height=750)

        Left_frame = LabelFrame(Frame1, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("liquid crystal", 12, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=690)
        

        Course_frame = LabelFrame(Frame1, bd=2, bg="white", relief=RIDGE, text="Current course", font=("liquid crystal", 12, "bold"))
        Course_frame.place(x=12, y=135, width=715, height=125)

        def time():
            time_string = strftime("%H:%M:%S %p")
            tim.config(text=time_string)

            tim.after(1000, time)
          
        
        tim = Label(self.root,font=("liquid crystal", 20), bg="darkred", fg="white")
        tim.place(x=10,y=0,width=160,height=50)
        time()
        

        
        #Department
        dep = Label(Course_frame,text= "Department",font=("liquid crystal", 12, "bold"))
        dep.grid(row=0,column=0,padx=2,pady=10)
        dep_combo=ttk.Combobox(Course_frame,textvariable=self.var_dep ,font=("liquid crystal", 12, "bold"),width=17)
        dep_combo["values"]=("SELECT","AI","COMPUTER","IT","CIVIL","MECHANICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #Year
        Year = Label(Course_frame,text= "Year",font=("liquid crystal", 12, "bold"))
        Year.grid(row=1,column=0,padx=2,pady=10)
        Year_combo=ttk.Combobox(Course_frame,textvariable=self.var_Year,font=("liquid crystal", 12, "bold"),width=17)
        Year_combo["values"]=("SELECT","1","2","3","4","5","6")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10)

        #semester
        semester = Label(Course_frame,text= "Semester",font=("liquid crystal", 12, "bold"))
        semester.grid(row=1,column=2,padx=10)
        semester_combo=ttk.Combobox(Course_frame,textvariable=self.var_semester,font=("liquid crystal", 12, "bold"),width=17)
        semester_combo["values"]=("SELECT","I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10)


        #Student info
        student_frame = LabelFrame(Frame1, bd=2, bg="white", relief=RIDGE, text="Student Info", font=("liquid crystal", 12, "bold"))
        student_frame.place(x=12, y=260, width=715, height=410)

        #Student ID
        Id = Label(student_frame,text= "Student ID : ",font=("liquid crystal", 12, "bold"))
        Id.grid(row=0,column=0,padx=10,pady =5)

        Id_box = ttk.Entry(student_frame,textvariable=self.var_Id,width=25,font=("liquid crystal", 12, "bold"))
        Id_box.grid(row=0,column=1,padx=10,pady =5)

        #name
        name = Label(student_frame,text= "Student Name : ",font=("liquid crystal", 12, "bold"))
        name.grid(row=1,column=0,padx=10,pady =5)

        name_box = ttk.Entry(student_frame,textvariable=self.var_name,width=25,font=("liquid crystal", 12, "bold"))
        name_box.grid(row=1,column=1,padx=10,pady =5)

        #division
        division = Label(student_frame,text= "Student Division : ",font=("liquid crystal", 12, "bold"))
        division.grid(row=3,column=0,padx=10,pady =5)

        division_box = ttk.Entry(student_frame,textvariable=self.var_division,width=25,font=("liquid crystal", 12, "bold"))
        division_box.grid(row=3,column=1,padx=10,pady =5)

        #roll no.
        roll = Label(student_frame,text= "Student Roll No. : ",font=("liquid crystal", 12, "bold"))
        roll.grid(row=4,column=0,padx=10,pady =5)

        roll_box = ttk.Entry(student_frame,textvariable=self.var_roll,width=25,font=("liquid crystal", 12, "bold"))
        roll_box.grid(row=4,column=1,padx=10,pady =5)

        #Gender
        gender = Label(student_frame,text= "Student Gender : ",font=("liquid crystal", 12, "bold"))
        gender.grid(row=5,column=0,padx=10,pady =5)

        gender_box = ttk.Entry(student_frame,textvariable=self.var_gender,width=25,font=("liquid crystal", 12, "bold"))
        gender_box.grid(row=5,column=1,padx=10,pady =5)

        #DOB
        DOB = Label(student_frame,text= "Student DOB : ",font=("liquid crystal", 12, "bold"))
        DOB.grid(row=6,column=0,padx=10,pady =5)

        DOB_box = ttk.Entry(student_frame,textvariable=self.var_DOB,width=25,font=("liquid crystal", 12, "bold"))
        DOB_box.grid(row=6,column=1,padx=10,pady =5)

        #Email
        Email = Label(student_frame,text= "Student Email : ",font=("liquid crystal", 12, "bold"))
        Email.grid(row=7,column=0,padx=10,pady =5)

        Email_box = ttk.Entry(student_frame,textvariable=self.var_Email,width=25,font=("liquid crystal", 12, "bold"))
        Email_box.grid(row=7,column=1,padx=10,pady =5)

        #Phoneno.
        Phone = Label(student_frame,text= "Student Phone No. : ",font=("liquid crystal", 12, "bold"))
        Phone.grid(row=8,column=0,padx=10,pady =5)

        Phone_box = ttk.Entry(student_frame,textvariable=self.var_Phone,width=25,font=("liquid crystal", 12, "bold"))
        Phone_box.grid(row=8,column=1,padx=10,pady =5)

        #Address
        Address = Label(student_frame,text= "Student Address : ",font=("liquid crystal", 12, "bold"))
        Address.grid(row=7,column=0,padx=10,pady =5)

        Address_box = ttk.Entry(student_frame,textvariable=self.var_Address,width=25,font=("liquid crystal", 12, "bold"))
        Address_box.grid(row=7,column=1,padx=10,pady =5)

        #radio butthon
        self.var_radio = StringVar()
        Radio_button = ttk.Radiobutton(student_frame,variable=self.var_radio,text= "Take Photo Sample : ",value="Yes")
        Radio_button.place(x=25,y=290)

        Radio_button2 = ttk.Radiobutton(student_frame,variable=self.var_radio,text= "No Photo Sample : ",value="No")
        Radio_button2.place(x=25,y=320)

        #button frame
        bbt_frame = LabelFrame(student_frame, bd=2, bg="white", relief=RIDGE)
        bbt_frame.place(x=530, y=0, width=158, height=363)

        save = Button(bbt_frame,text="Save",command=self.add_data ,height=3,width = 12,font=("liquid crystal", 15, "bold"),bg="red",fg="white")
        save.grid(row=0,column=0)

        update = Button(bbt_frame,text="Update",command=self.update,height=3,width = 12,font=("liquid crystal", 15, "bold"),bg="red",fg="white")
        update.grid(row=1,column=0)

        delete = Button(bbt_frame,text="Delete",command=self.delete ,height=3,width = 12,font=("liquid crystal", 15, "bold"),bg="red",fg="white")
        delete.grid(row=2,column=0)

        reset = Button(bbt_frame,text="Reset",command=self.reset,height=3,width = 12,font=("liquid crystal",15, "bold"),bg="red",fg="white")
        reset.grid(row=3,column=0)

        take_photo = Button(student_frame,text="Take Photo",command=self.generate_dataset,height=3,width = 12,font=("liquid crystal", 13, "bold"),bg="red",fg="white")
        take_photo.place(x=195,y=290)

        Exit = Button(Left_frame,text="Exit",command=self.exit,height=3,width = 12,font=("liquid crystal", 13, "bold"),bg="red",fg="white")
        Exit.place(x=10,y=10)
        
        Right_frame = LabelFrame(Frame1, bd=2, bg="white", relief=RIDGE, text="Tabel", font=("liquid crystal", 12, "bold"))
        Right_frame.place(x=780, y=10, width=670, height=690)

        Tabel_Frame= LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, font=("liquid crystal", 12, "bold"))
        Tabel_Frame.place(x=1,y=0,width=661,height=665)


        scroll_x = ttk.Scrollbar(Tabel_Frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Tabel_Frame,orient=VERTICAL)
        self.student_tabel= ttk.Treeview(Tabel_Frame,columns=("dep","Id","Year","semester","name","division","roll","gender","DOB","Email","Phone","Address","Photo"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_tabel.xview)
        scroll_y.config(command=self.student_tabel.yview)

        self.student_tabel.heading("Id",text="Id")
        self.student_tabel.heading("dep",text="Department")
        self.student_tabel.heading("Year",text="Year")
        self.student_tabel.heading("semester",text="Semester")
        self.student_tabel.heading("name",text="Name")
        self.student_tabel.heading("division",text="Division")
        self.student_tabel.heading("roll",text="Roll_No")
        self.student_tabel.heading("gender",text="Gender")
        self.student_tabel.heading("DOB",text="DOB")
        self.student_tabel.heading("Email",text="Email")
        self.student_tabel.heading("Phone",text="Phone")
        self.student_tabel.heading("Address",text="Address")
        self.student_tabel.heading("Photo",text="Photo")
        self.student_tabel["show"]="headings"

        self.student_tabel.column("Id",width=100)
        self.student_tabel.column("dep",width=100)
        self.student_tabel.column("Year",width=100)
        self.student_tabel.column("semester",width=100)
        self.student_tabel.column("name",width=100)
        self.student_tabel.column("division",width=100)
        self.student_tabel.column("roll",width=100)
        self.student_tabel.column("gender",width=100)
        self.student_tabel.column("DOB",width=100)
        self.student_tabel.column("Email",width=100)
        self.student_tabel.column("Phone",width=100)
        self.student_tabel.column("Address",width=100)
        self.student_tabel.column("Photo",width=100)

        self.student_tabel.pack(fill=BOTH,expand=1)
        self.student_tabel.bind("<ButtonRelease>",self.click)
        self.data_shw()

    

    def exit(self):
            self.root.destroy()




    def add_data(self):
        if self.var_dep.get()=="Select" or self.var_name.get()=="" or self.var_Id.get()=="":
            messagebox.showerror("Error","Not all field filled",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Utk222004",database="btech")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_dep.get(),
                self.var_Id.get(),
                self.var_Year.get(),
                self.var_semester.get(),
                self.var_name.get(),
                self.var_division.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_DOB.get(),
                self.var_Email.get(),
                self.var_Phone.get(),
                self.var_Address.get(),
                self.var_radio.get()
                ))
                conn.commit()
                self.data_shw()
                conn.close()
                messagebox.showinfo("Success","Data Saved",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def data_shw(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Utk222004",database="btech")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from Student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in data:
                self.student_tabel.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def click(self,event=""):
        cursor_focus= self.student_tabel.focus()
        content= self.student_tabel.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_Id.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_name.set(data[4]),
        self.var_division.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_DOB.set(data[8]),
        self.var_Email.set(data[9]),
        self.var_Address.set(data[11]),
        self.var_Phone.set(data[10]),
        self.var_radio.set(data[11])
    
    def update(self):
        if self.var_dep.get()=="Select" or self.var_name.get()=="" or self.var_Id.get()=="":
            messagebox.showerror("Error","Not all field filled",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do You want to update?",parent=self.root) 
                if Update==1:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Utk222004",database="btech")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update Student set Department=%s,Year=%s,semester=%s,name=%s,division=%s,Roll_No=%s,gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Photo=%s where Id=%s",(
                        self.var_dep.get(),
                        self.var_Year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_division.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_DOB.get(),
                        self.var_Email.get(),
                        self.var_Phone.get(),
                        self.var_Address.get(),
                        self.var_radio.get(),
                        self.var_Id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Update Complete",parent=self.root)
                conn.commit()
                self.data_shw()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    

    def delete(self):
        if self.var_Id.get()=="":
            messagebox.showerror("Error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do You want delete this record",parent=self.root)
                if delete==1:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Utk222004",database="btech")
                    my_cursor=conn.cursor()
                    my_cursor.execute("delete from Student where Id=%s",(self.var_Id.get(),))
                
                else:
                    if not delete:
                        return
                conn.commit()
                self.data_shw()
                conn.close()
                messagebox.showinfo("Success","Deletion Complete",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    def reset(self):
        self.var_dep.set("SELECT")
        self.var_Year.set("SELECT")
        self.var_semester.set("SELECT")
        self.var_Id.set("")
        self.var_name.set("")
        self.var_division.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_DOB.set("")
        self.var_Email.set("")
        self.var_Phone.set("")
        self.var_Address.set("")
        self.var_radio.set("")
    

                


    def generate_dataset(self):
        if self.var_dep.get()=="Select" or self.var_name.get()=="" or self.var_Id.get()=="":
            messagebox.showerror("Error","Not all field filled",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Utk222004",database="btech")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT * from Student")
                myresult=my_cursor.fetchall()
                id= 0
                for x in myresult:
                    id = id+1
                my_cursor.execute("Update Student set Department=%s,Year=%s,semester=%s,name=%s,division=%s,Roll_No=%s,gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Photo=%s where Id=%s",(
                        self.var_dep.get(),
                        self.var_Year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_division.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_DOB.get(),
                        self.var_Email.get(),
                        self.var_Phone.get(),
                        self.var_Address.get(),
                        self.var_radio.get(),
                        self.var_Id.get()==id+1
                    ))
                conn.commit()
                self.data_shw()
                self.reset()
                conn.close()
    
                face_classifier = cv2.CascadeClassifier("C:\\Users\\Utkarsh\\Desktop\\SIP\\SIP_Attendance\\haarcascade_frontalface_default.xml")
                def face_crop(img):
                    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(grey,1.3,5)
                    #scaling factor = 1.3
                    #minimum nebiour = 5

                    for(x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop
                    
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, frame= cap.read()
                    if face_crop(frame) is not None:
                        img_id = img_id + 1
                        face=cv2.resize(face_crop(frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



    
if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
