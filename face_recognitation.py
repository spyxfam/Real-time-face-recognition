from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2 
import os
import numpy as np


class Face_Recognisation:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x690+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="FACE DETECTOR",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        img_top=Image.open(r"C:\Users\User\Pictures\Camera Roll\images (9).jfif")
        img_top=img_top.resize((680,750),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root,image=self.photoimg_top)
        f_label.place(x=0,y=55,width=680,height=750)

        img_bottom=Image.open(r"C:\Users\User\Pictures\Camera Roll\download (10).jfif")
        img_bottom=img_bottom.resize((950,750),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_label=Label(self.root,image=self.photoimg_bottom)
        f_label.place(x=680,y=55,width=950,height=750)

        b1_1=Button(f_label,text="Face recognition",command=self.face_recog,cursor="hand2",font=("times new roman",16,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=375,y=660,width=200,height=40) 
        #_____________________attendence-------------

    def mark_attendance(self,i,n,S,d):
        with open("ATTENDENCE.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (S not in name_list) and  (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{S},{d},{dtString},{d1},Present")





        #__________________________--detction--____________________#
    
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Akshatha17*",database="facerecognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from Student where id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select sem from Student where id="+str(id))
                S=my_cursor.fetchone()
                S="+".join(S)

                my_cursor.execute("select dep from Student where id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select id from Student where id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Sem:{S}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,n,S,d)
                
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,facecascade):
            coord=draw_boundary(img,facecascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        facecascade=cv2.CascadeClassifier("algorithm.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifiers.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,facecascade)
            cv2.imshow("Welcome To Face Fecognisation",img)

            if cv2.waitKey(1)==13:
                break
        
        video_cap.release()
        cv2.destroyAllWindows()

                    






if __name__=="__main__":
    root=Tk()
    obj=Face_Recognisation(root)
    root.mainloop()