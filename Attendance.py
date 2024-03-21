from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog
from time import strftime
from datetime import datetime
from PIL import Image,ImageTk

mydata=[]
class Attenance:
    def __init__(self, root):
        self.root = root
        #self.root.geometry("1530x790+0+0")
        self.root.attributes('-fullscreen', True)
        self.root.title("Attendance")
    

        self.var_dep=StringVar()
        self.var_Id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_atten=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\img2.jpg")
        label_bg=Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        title = Label(self.root, text="Attendance", font=("liquid crystal", 30), bg="darkgreen", fg="white")
        title.place(x=0, y=0, relwidth=1)

        Frame1 = Frame(self.root, bd=2, relief=RIDGE)
        Frame1.place(x=20, y=60, width=1480, height=750)


        Left_frame = LabelFrame(Frame1, bd=2, bg="white", relief=RIDGE, text="Student Attendance", font=("liquid crystal", 15, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=690)

        student_frame = LabelFrame(Frame1, bd=2, bg="white", relief=RIDGE, text="Current course", font=("liquid crystal", 15, "bold"))
        student_frame.place(x=12, y=135, width=715, height=550)


        def time():
            time_string = strftime("%H:%M:%S %p")
            tim.config(text=time_string)

            tim.after(1000, time)
          
        
        tim = Label(self.root,font=("liquid crystal", 20), bg="darkgreen", fg="white")
        tim.place(x=10,y=0,width=160,height=50)
        time()
        
        #Student ID
        Id = Label(student_frame,text= "Attendance ID : ",font=("liquid crystal", 15, "bold"))
        Id.grid(row=0,column=0,padx=10,pady =5)

        Id_box = ttk.Entry(student_frame,textvariable=self.var_Id,width=20,font=("liquid crystal", 15, "bold"))
        Id_box.grid(row=0,column=1,padx=10,pady =5)

        #name
        name = Label(student_frame,text= "Student Name : ",font=("liquid crystal", 15, "bold"))
        name.grid(row=1,column=0,padx=10,pady =5)

        name_box = ttk.Entry(student_frame,textvariable=self.var_name,width=20,font=("liquid crystal", 15, "bold"))
        name_box.grid(row=1,column=1,padx=10,pady =5)

        #Roll
        Roll = Label(student_frame,text= "Roll No. : ",font=("liquid crystal", 15, "bold"))
        Roll.grid(row=2,column=0,padx=10,pady =5)

        Roll_box = ttk.Entry(student_frame,textvariable=self.var_roll,width=20,font=("liquid crystal", 15, "bold"))
        Roll_box.grid(row=2,column=1,padx=10,pady =5)

        #Department
        Department = Label(student_frame,text= "Department Name : ",font=("liquid crystal", 15, "bold"))
        Department.grid(row=3,column=0,padx=10,pady =5)

        Department_box = ttk.Entry(student_frame,textvariable=self.var_dep,width=20,font=("liquid crystal", 15, "bold"))
        Department_box.grid(row=3,column=1,padx=10,pady =5)

        #Time
        Time = Label(student_frame,text= "Time : ",font=("liquid crystal", 15, "bold"))
        Time.grid(row=4,column=0,padx=10,pady =5)

        Time_box = ttk.Entry(student_frame,textvariable=self.var_time,width=20,font=("liquid crystal", 15, "bold"))
        Time_box.grid(row=4,column=1,padx=10,pady =5)

        #Date
        Date = Label(student_frame,text= "Date : ",font=("liquid crystal", 15, "bold"))
        Date.grid(row=5,column=0,padx=10,pady =5)

        Date_box = ttk.Entry(student_frame,textvariable=self.var_date,width=20,font=("liquid crystal", 15, "bold"))
        Date_box.grid(row=5,column=1,padx=10,pady =5)


        #Attendance
        attendance = Label(student_frame,text= "Attendance Status : ",font=("liquid crystal", 15, "bold"))
        attendance.grid(row=6,column=0,padx=10,pady =5)

        self.attendance_combo=ttk.Combobox(student_frame,textvariable=self.var_atten,font=("liquid crystal", 15, "bold"),width=17)
        self.attendance_combo["values"]=("Status","Present","Absent")
        self.attendance_combo.current(0)
        self.attendance_combo.grid(row=6,column=1,padx=10,pady =5)

        #button frame
        bbt_frame = LabelFrame(student_frame, bd=2, bg="white", relief=RIDGE)
        bbt_frame.place(x=0, y=300, width=715, height=935)

        Import = Button(bbt_frame,text="Import",command=self.importcsv,height=2,width =20,font=("liquid crystal", 22, "bold"),bg="green",fg="white")
        Import.grid(row=0,column=0)

        Export = Button(bbt_frame,text="Export",command=self.export ,height=2,width =20,font=("liquid crystal", 22, "bold"),bg="green",fg="white")
        Export.grid(row=1,column=0)

        Add = Button(bbt_frame,text="Add" ,command=self.Add,height=2,width =20,font=("liquid crystal", 22, "bold"),bg="green",fg="white")
        Add.grid(row=1,column=1)

        reset = Button(bbt_frame,text="Reset",command=self.reset,height=2,width =20,font=("liquid crystal",22, "bold"),bg="green",fg="white")
        reset.grid(row=0,column=1)

        Exit = Button(Left_frame,text="Exit",command=self.exit,height=3,width = 12,font=("liquid crystal", 13, "bold"),bg="green",fg="white")
        Exit.place(x=10,y=10)
        

        #Right Frame of the GUI
        Right_frame = LabelFrame(Frame1, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("liquid crystal", 12, "bold"))
        Right_frame.place(x=780, y=10, width=670, height=690)

        Tabel_Frame= LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, font=("liquid crystal", 12, "bold"))
        Tabel_Frame.place(x=1,y=1,width=663,height=665)

        scroll_x = ttk.Scrollbar(Tabel_Frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Tabel_Frame,orient=VERTICAL)
        self.student_tabel= ttk.Treeview(Tabel_Frame,columns=("Id","Roll_No","name","dep","Time","Date","attendance"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_tabel.xview)
        scroll_y.config(command=self.student_tabel.yview)

        self.student_tabel.heading("Id",text="Id")
        self.student_tabel.heading("dep",text="Department")
        self.student_tabel.heading("Roll_No",text="Roll_No")
        self.student_tabel.heading("name",text="Name")
        self.student_tabel.heading("Time",text="Time")
        self.student_tabel.heading("Date",text="Date")
        self.student_tabel.heading("attendance",text="Attenance")
    
        self.student_tabel["show"]="headings"

        self.student_tabel.column("Id",width=100)
        self.student_tabel.column("dep",width=100)
        self.student_tabel.column("Roll_No",width=100)
        self.student_tabel.column("name",width=100)
        self.student_tabel.column("Time",width=100)
        self.student_tabel.column("Date",width=100)
        self.student_tabel.column("attendance",width=100)
     

        self.student_tabel.pack(fill=BOTH,expand=1)
        self.student_tabel.bind("<ButtonRelease>",self.get_cursor)
    

    def fetechData(self,rows):
        self.student_tabel.delete(*self.student_tabel.get_children())
        for i in rows:
            self.student_tabel.insert("",END,values=i)
    
    #To import the CSV file
    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread= csv.reader(myfile,delimiter=",") 
            for i in csvread:
                mydata.append(i)
            self.fetechData(mydata)

    def exit(self):
            self.root.destroy()

    #To export the CSVfile
    def export(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found", parent=self.root)
                return False
            fln = filedialog.asksaveasfile(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=(("CSV files", "*.csv"), ("All files", "*.*")),
                defaultextension=".csv",
                parent=self.root
                                )
            
            with open(fln.name, mode="w", newline="", encoding='utf-8') as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                        exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Data Exported" + " successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
    
    def get_cursor(self,event=""):
        cursor_row=self.student_tabel.focus()
        content=self.student_tabel.item(cursor_row)
        data=content['values']

        self.var_Id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_dep.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_atten.set(data[6])
        
    def reset(self):
        self.var_Id.set(""),
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_dep.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        self.var_atten.set("")

    #To Add to the excl file
    def Add(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found", parent=self.root)
                return False
            else:
                data = [
                    self.var_Id.get(),
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_dep.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_atten.get()
                ]
                mydata.append(data)
                self.fetechData(mydata)
                #messagebox.showinfo("Data Copied", "Data has been Copied successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
    
    



if __name__ == "__main__":
    root = Tk()
    obj = Attenance(root)
    root.mainloop()