from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x690+0+0")
        self.root.title("face recognition system")
        #=======================variables==============

        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_department=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()

        #first image
        img1=Image.open(r"C:\Users\User\Pictures\Camera Roll\images (2).jfif")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=0,y=0,width=800,height=200)

        #second image
        img2=Image.open(r"C:\Users\User\Pictures\Camera Roll\depositphotos_68789187-stock-photo-students.jpg")
        img2=img2.resize((800,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_label=Label(self.root,image=self.photoimg2)
        f_label.place(x=800,y=0,width=800,height=200) 

        #bg image
        img4=Image.open(r"C:\Users\User\Pictures\Camera Roll\download (2).jfif")
        img4=img4.resize((1500,690),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1500,height=690)

        #title
        title_lbl=Label(bg_img,text="ATTENDENCE MANEGEMENT SYSYTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        #MAIN FRAME
        MAIN_FRAME=Frame(bg_img,bd=2)
        MAIN_FRAME.place(x=20,y=55,width=1480,height=600)

        #left label frame

        left_frame=LabelFrame(MAIN_FRAME,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=710,height=580)

        img_left=Image.open(r"C:\Users\User\Pictures\Camera Roll\download (14).jfif")
        img_left=img_left.resize((700,170),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_label=Label(left_frame,image=self.photoimg_left)
        f_label.place(x=5,y=0,width=700,height=170)

        leftinside_FRAME=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        leftinside_FRAME.place(x=15,y=180,width=670,height=330)

        #label and entry
        #attendence id
        attendenceID_label=Label(leftinside_FRAME,text="ATTENDENCE ID",font=("times new roman",12,"bold"))
        attendenceID_label.grid(row=0,column=0,padx=2,pady=10)

        attendenceID_entry=ttk.Entry(leftinside_FRAME,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        attendenceID_entry.grid(row=0,column=1,padx=10,sticky=W)

         #student name
        semestername_label=Label(leftinside_FRAME,text="StudentName",font=("times new roman",12,"bold"))
        semestername_label.grid(row=0,column=2,padx=2,pady=10)

        studentname_entry=ttk.Entry(leftinside_FRAME,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,sticky=W)

        #date
        date_label=Label(leftinside_FRAME,text="Date",font=("times new roman",12,"bold"))
        date_label.grid(row=2,column=0,padx=2,pady=10)

        date_entry=ttk.Entry(leftinside_FRAME,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=1,padx=10,sticky=W)

        #time
        time_label=Label(leftinside_FRAME,text="Time",font=("times new roman",12,"bold"))
        time_label.grid(row=1,column=2,padx=2,pady=10)

        time_entry=ttk.Entry(leftinside_FRAME,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        time_entry.grid(row=1,column=3,padx=10,sticky=W)

        #department number
        department_no_label=Label(leftinside_FRAME,text="Department",font=("times new roman",12,"bold"))
        department_no_label.grid(row=1,column=0,padx=2,pady=10)
        department_no_entry=ttk.Entry(leftinside_FRAME,textvariable=self.var_atten_department,width=20,font=("times new roman",12,"bold"))
        department_no_entry.grid(row=1,column=1,padx=10,sticky=W)

        #ATTENDENCE
        ATTENDENCE_label=Label(leftinside_FRAME,text="ATTENDENCE",font=("times new roman",12,"bold"))
        ATTENDENCE_label.grid(row=3,column=0,padx=2,pady=10)
        self.atten_combo=ttk.Combobox(leftinside_FRAME,textvariable=self.var_atten_attendence,font=("times new roman",12,"bold"),width=17,state="readonly")
        self.atten_combo["values"]=("Status","Present","Absent")
        self.atten_combo.current(0)
        self.atten_combo.grid(row=3,column=1,pady=8)  


        #button frame
        btn_frame=Frame(leftinside_FRAME,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=290,width=690,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importcsv,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportcsv,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #righht frame
        rigth_frame=LabelFrame(MAIN_FRAME,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        rigth_frame.place(x=730,y=10,width=720,height=580)

        table_frame=Frame(rigth_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=525)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.studnet_table=ttk.Treeview(table_frame,column=("id","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.studnet_table.xview)
        scroll_y.config(command=self.studnet_table.yview)


        self.studnet_table.heading("id",text="ATTENDENCE ID")
        self.studnet_table.heading("name",text="StudentName")
        self.studnet_table.heading("department",text="Department")
        self.studnet_table.heading("time",text="Time")
        self.studnet_table.heading("date",text="Date")
        self.studnet_table.heading("attendence",text="ATTENDENCE")
        self.studnet_table["show"]="headings"

        self.studnet_table.column("id",width=100)
        self.studnet_table.column("name",width=100)
        self.studnet_table.column("department",width=100)
        self.studnet_table.column("time",width=100)
        self.studnet_table.column("date",width=100)
        self.studnet_table.column("attendence",width=100)

        self.studnet_table.pack(fill=BOTH,expand=1)
        self.studnet_table.bind("<ButtonRelease>",self.get_cursor)


    def fetchdata(self,rows):
        self.studnet_table.delete(*self.studnet_table.get_children())
        for i in rows:
            self.studnet_table.insert("",END,values=i)

    #importcsv
    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root) 
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    #export csv
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"sucessfully")
        except Exception as es:
                messagebox.showerror("error!",f"due to:{str(es)}",parent=self.root)

    
    def get_cursor(self,event=""):
        cursor_focus=self.studnet_table.focus()
        content=self.studnet_table.item(cursor_focus)
        data=content["values"]

        self.var_atten_id.set(data[0]),
        self.var_atten_name.set(data[1]),
        self.var_atten_department.set(data[2]),
        self.var_atten_date.set(data[3]),
        self.var_atten_time.set(data[4]),
        self.var_atten_attendence.set(data[5])

    #reset
    def reset_data(self):
        self.var_atten_id.set(""),
        self.var_atten_name.set(""),
        self.var_atten_department.set(""),
        self.var_atten_date.set(""),
        self.var_atten_time.set(""),
        self.var_atten_attendence.set("Status")

if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()