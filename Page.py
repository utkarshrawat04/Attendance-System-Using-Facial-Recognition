from tkinter import *
from PIL import Image,ImageTk
from Student import student
from tkinter import messagebox
import mysql.connector
import numpy as np
from time import strftime
from tkinter import filedialog
from datetime import datetime
import cv2
import os
from Attendance import Attenance



class Face_Recognization_system:
    def __init__(self,root):
        self.root=root
        #self.root.geometry("1530x790+0+0")
        self.root.attributes('-fullscreen', True)
        self.root.title("SYSTEM")

    
        Frame0 = Frame(self.root, bg="white")
        Frame0.place(x=0, y=0, width=1540, height=870)

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\img1.jpg")
        label_bg=Label(Frame0,image=self.bg)
        label_bg.place(x=0,y=0,relwidth=1,relheight=1)

        def time():
            time_string = strftime("%H:%M:%S %p")
            tim.config(text=time_string)

            tim.after(1000, time)
          

        title = Label(Frame0, text="Face Recognization System", font=("liquid crystal", 38), bg="Darkred", fg="white")
        title.place(x=0, y=0, relwidth=1)

        tim = Label(Frame0,font=("liquid crystal", 20), bg="darkred", fg="white")
        tim.place(x=10,y=0,width=160,height=60)
        time()

        #Button
        img_1 = Image.open(r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\b1.jpg")
        img_1 = img_1.resize((220,220), Image.LANCZOS)
        self.img_1 = ImageTk.PhotoImage(img_1)

        b1 = Button(Frame0,text="Student Detail",image=self.img_1, font=("liquid crystal", 19), command=self.student_buttons, bg="black", fg="white")
        b1.place(x=200, y=150, width=220, height=220)

        b1_1 = Button(Frame0,text="1", font=("liquid crystal", 15), command=self.student_buttons, bg="black", fg="white")
        b1_1.place(x=200, y=350, width=220, height=40)


        img_2 = Image.open(r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\b2.jpg")
        img_2 = img_2.resize((220,220), Image.LANCZOS)
        self.img_2 = ImageTk.PhotoImage(img_2)

        b2 = Button(Frame0,text ="Face Detection",image=self.img_2,command=self.face_recognize,font=("liquid crystal", 19), bg="black", fg="white")
        b2.place(x = 650,y = 150,width = 220, height = 220)

        b2_1 = Button(Frame0,text ="2",command=self.face_recognize,font=("liquid crystal", 15), bg="black", fg="white")
        b2_1.place(x = 650,y = 350,width = 220, height = 40)

        img_3 = Image.open(r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\b3.jpg")
        img_3 = img_3.resize((220,220), Image.LANCZOS)
        self.img_3 = ImageTk.PhotoImage(img_3)

        b3 = Button(Frame0,text ="Attendance",image=self.img_3,command= self.Attendance_buttons,font=("liquid crystal", 19), bg="black", fg="white")
        b3.place(x = 1100,y = 150,width = 220, height = 220)

        b3_1 = Button(Frame0,text ="3",command= self.Attendance_buttons, font=("liquid crystal", 15), bg="black", fg="white")
        b3_1.place(x = 1100,y = 350,width = 220, height = 40)


        img_4 = Image.open(r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\b4.jpg")
        img_4 = img_4.resize((220,210), Image.LANCZOS)
        self.img_4 = ImageTk.PhotoImage(img_4)

        b4 = Button(Frame0,text ="Exit",image=self.img_4,command=self.exit,font=("liquid crystal", 19), bg="black", fg="white")
        b4.place(x = 200,y = 450,width = 220, height = 220)

        b4_1 = Button(Frame0,text ="4",command=self.exit,font=("liquid crystal", 15), bg="black", fg="white")
        b4_1.place(x = 200,y = 650,width = 220, height = 40)


        img_5 = Image.open(r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\b5.jpg")
        img_5 = img_5.resize((220,220), Image.LANCZOS)
        self.img_5 = ImageTk.PhotoImage(img_5)

        b5 = Button(Frame0,text ="Photos",image=self.img_5,font=("liquid crystal", 19),command=self.open_img, bg="black", fg="white")
        b5.place(x = 650,y = 450,width = 220, height = 220)

        b5_1 = Button(Frame0,text ="5",font=("liquid crystal", 15),command=self.open_img, bg="black", fg="white")
        b5_1.place(x = 650,y = 650,width = 220, height = 40)

        img_6 = Image.open(r"C:\Users\Utkarsh\Desktop\SIP\SIP_Attendance\Images\b6.jpg")
        img_6 = img_6.resize((220,220), Image.LANCZOS)
        self.img_6 = ImageTk.PhotoImage(img_6)

        b6 = Button(Frame0,text ="Train Data",image= self.img_6,command=self.train_classification,font=("liquid crystal", 19), bg="black", fg="white")
        b6.place(x = 1100,y = 450,width = 220, height = 220)

        b6_1 = Button(Frame0,text ="6",command=self.train_classification,font=("liquid crystal", 15), bg="black", fg="white")
        b6_1.place(x = 1100,y = 650,width = 220, height = 40)

        
    def student_buttons(self):
        self.new_window = Toplevel(self.root)  
        self.app = student(self.new_window)

    def Attendance_buttons(self):
        self.new_window = Toplevel(self.root)  
        self.app = Attenance(self.new_window)
    
    def open_img(self):
        os.startfile("Data")

    #Function to train the model on image datasets taken
    def train_classification(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')  # GRAY SCALE IMAGES
            image_np = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(image_np)
            ids.append(id)

            cv2.imshow("Training", image_np)
            cv2.waitKey(1) 
        ids=np.array(ids)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Resilt","Training Done")
    
    # Detects the person and adds detail to mark attendence
    def mark_attedance(self,i,r,n,d,fln):
        with open(fln,"r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    #To Exit the code 
    def exit(self):
            self.root.destroy()

    #Function for the facedetection
    def face_recognize(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        def draw_boundary(img,classifier,scaleFactore,minNeighbours,color,text,clf):
            grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(grey_image,scaleFactore,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(grey_image[y:y+h,x:x+w])
                confidence=int(100*(1-(predict/300)))

                conn = mysql.connector.connect(host="localhost",username="root",password="Utk222004",database="btech")
                my_cursor=conn.cursor()

                my_cursor.execute("Select Name from student where Id="+str(id))
                n = my_cursor.fetchone()

                my_cursor.execute("Select Roll_No from student where Id="+str(id))
                r = my_cursor.fetchone()

                my_cursor.execute("Select Department from student where Id="+str(id))
                d = my_cursor.fetchone()

                my_cursor.execute("Select Id from student where Id="+str(id))
                i = my_cursor.fetchone()

                if confidence > 78:
                    cv2.putText(img, f"Id:{i[0]}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r[0]}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d[0]}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n[0]}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attedance(i[0],r[0],n[0],d[0],fln)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    
                coord=[x,y,w,y]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord= draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("C:\\Users\\Utkarsh\\Desktop\\SIP\\SIP_Attendance\\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Regonization",img)

            k = cv2.waitKey(1)
            if k == ord('q'):
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognization_system(root)
    root.mainloop()








'''
import cv2
import threading
from deepface import DeepFace 

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)   # to access and capture video from devices  backend and continuously captures frames from the camera

video.set(cv2.CAP_PROP_FRAME_WIDTH,640)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
#constants used to set or get the width and height of frames in OpenCV
#allowing configuration or retrieval of video frame dimensions

counter = 0
face_match = False

ref_image = cv2.imread("C:\\Users\\Utkarsh\\Desktop\\SIP\\SIP_Attendance\\img\\img1.jpg")


def check(frame):
    global face_match
    try:
        if DeepFace.verify(frame, ref_image.copy())['verified']:
            face_match = True
        else:
            face_match = False
    
    except ValueError:
        face_match = False


while True:
    ret, frame = video.read()  # Gives bool (if the webcam is working or not) and frame

    if ret:
        if counter % 30 ==0:
            try:
                threading.Thread(target=check(frame),args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText(frame, "Match",(20, 450), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0), 3)
        else:
            cv2.putText(frame, "NO Match",(20, 450), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255), 3)
            
        cv2.imshow("frame", frame)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()

'''

'''
video = cv2.VideoCapture(0)   # To capture webcam
while True:
    ret, frame = video.read()  # Gives bool (if the webcam is working or not) and frame
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
'''