from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x690+0+0")
        self.root.title("face recognition system")


        title_lbl=Label(self.root,text="DEVELOPERS",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1500,height=45)


        #first image
        img1=Image.open(r"C:\Users\User\Pictures\Camera Roll\facial-recognition.jpg")
        img1=img1.resize((1530,750),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=0,y=55,width=1530,height=750) 

        MAIN_FRAME=Frame(f_label,bd=2)
        MAIN_FRAME.place(x=1020,y=0,width=500,height=560)

        img12=Image.open(r"C:\Users\User\Pictures\Camera Roll\face-recognition\IMG-20220912-WA0017-01.jpeg")
        img12=img12.resize((200,250),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        f_label2=Label(MAIN_FRAME,image=self.photoimg12)
        f_label2.place(x=300,y=0,width=200,height=250)

        dep_label=Label(MAIN_FRAME,text="This is Suhaas ,",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dep_label.place(x=0,y=5)


        dep_label=Label(MAIN_FRAME,text="One of the developer for this project",font=("times new roman",14,"bold"),fg="blue",bg="white")
        dep_label.place(x=0,y=50)

        img13=Image.open(r"C:\Users\User\Pictures\Camera Roll\software-developer-copy.jpg")
        img13=img13.resize((500,350),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(img13)

        f_label1=Label(MAIN_FRAME,image=self.photoimg13)
        f_label1.place(x=-2,y=220,width=500,height=350)


        MAIN_FRAME1=Frame(f_label,bd=2)
        MAIN_FRAME1.place(x=515,y=0,width=500,height=560)

        img14=Image.open(r"C:\Users\User\Pictures\Camera Roll\IMG_20221203_141024.jpg")
        img14=img14.resize((200,250),Image.ANTIALIAS)
        self.photoimg14=ImageTk.PhotoImage(img14)

        f_label3=Label(MAIN_FRAME1,image=self.photoimg14)
        f_label3.place(x=300,y=0,width=200,height=250)

        dep_label=Label(MAIN_FRAME1,text="This is Radhika, ",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dep_label.place(x=0,y=5)


        dep_label=Label(MAIN_FRAME1,text="One of the developer for this project",font=("times new roman",14,"bold"),fg="blue",bg="white")
        dep_label.place(x=0,y=50)

        img15=Image.open(r"C:\Users\User\Pictures\Camera Roll\shape10.png")
        img15=img15.resize((500,350),Image.ANTIALIAS)
        self.photoimg15=ImageTk.PhotoImage(img15)

        f_label4=Label(MAIN_FRAME1,image=self.photoimg15)
        f_label4.place(x=-2,y=220,width=500,height=350)


        MAIN_FRAME2=Frame(f_label,bd=2)
        MAIN_FRAME2.place(x=8,y=0,width=500,height=560)

        img16=Image.open(r"C:\Users\User\Pictures\Camera Roll\WhatsApp Image 2022-12-03 at 4.03.13 PM.jpeg")
        img16=img16.resize((200,250),Image.ANTIALIAS)
        self.photoimg16=ImageTk.PhotoImage(img16)

        f_label5=Label(MAIN_FRAME2,image=self.photoimg16)
        f_label5.place(x=300,y=0,width=200,height=250)

        dep_label=Label(MAIN_FRAME2,text="This is Keshav ,",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dep_label.place(x=0,y=5)


        dep_label=Label(MAIN_FRAME2,text="One of the developer for this project",font=("times new roman",14,"bold"),fg="blue",bg="white")
        dep_label.place(x=0,y=50)

        img17=Image.open(r"C:\Users\User\Pictures\Camera Roll\software-developer-copy.jpg")
        img17=img17.resize((500,350),Image.ANTIALIAS)
        self.photoimg17=ImageTk.PhotoImage(img17)

        f_label6=Label(MAIN_FRAME2,image=self.photoimg13)
        f_label6.place(x=-2,y=220,width=500,height=350)

if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()

