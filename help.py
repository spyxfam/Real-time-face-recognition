from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x690+0+0")
        self.root.title("face recognition system")


        title_lbl=Label(self.root,text="HELP DISK",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1500,height=45)


        #first image
        img1=Image.open(r"C:\Users\User\Pictures\Camera Roll\facial-recognition.jpg")
        img1=img1.resize((1530,750),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=0,y=55,width=1530,height=750)

        dep_label=Label(f_label,text="Email:tn.keshav02@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dep_label.place(x=550,y=260)

        dep_label=Label(f_label,text="Email:suhaasgjaradya@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dep_label.place(x=550,y=310)

        dep_label=Label(f_label,text="Email:radhika401@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dep_label.place(x=550,y=360)

        dep_label=Label(f_label,text="Do contact any one of the email id's if any problem",font=("times new roman",20,"bold"),fg="white",bg="red")
        dep_label.place(x=470,y=210)


if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()