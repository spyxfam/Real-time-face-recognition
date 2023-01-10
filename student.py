from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x690+0+0")
        self.root.title("face recognition system")

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()

        #first image
        img1=Image.open(r"C:\Users\User\Pictures\Camera Roll\images (2).jfif")
        img1=img1.resize((550,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=0,y=0,width=500,height=130)
 
        #second image
        img2=Image.open(r"C:\Users\User\Pictures\Camera Roll\images (3).jfif")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_label=Label(self.root,image=self.photoimg2)
        f_label.place(x=500,y=0,width=500,height=130)

        #3rd image
        img3=Image.open(r"C:\Users\User\Pictures\Camera Roll\images (4).jfif")
        img3=img3.resize((550,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_label=Label(self.root,image=self.photoimg3)
        f_label.place(x=1000,y=0,width=500,height=130)

        #background image
        img4=Image.open(r"C:\Users\User\Pictures\Camera Roll\download (2).jfif")
        img4=img4.resize((1500,690),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1500,height=690)

        title_lbl=Label(bg_img,text="STUDENT MANEGEMENT SYSYTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        MAIN_FRAME=Frame(bg_img,bd=2)
        MAIN_FRAME.place(x=10,y=55,width=1470,height=560)

        #left label frame

        left_frame=LabelFrame(MAIN_FRAME,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=690,height=680)

        #left image
        img_left=Image.open(r"C:\Users\User\Pictures\Camera Roll\images (4).jfif")
        img_left=img_left.resize((680,140),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_label=Label(left_frame,image=self.photoimg_left)
        f_label.place(x=15,y=0,width=680,height=140)

        #current course
        left_frame1=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",12,"bold"))
        left_frame1.place(x=5,y=145,width=690,height=200)

        #deptartment
        dep_label=Label(left_frame1,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=2,pady=10)

        dep_combo=ttk.Combobox(left_frame1,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Your Dept","Computer Science","Mechanical","Civil","Electronics and Communication")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10)

        #courses
        corse_label=Label(left_frame1,text="course",font=("times new roman",12,"bold"))
        corse_label.grid(row=0,column=2,padx=2,pady=10)

        corse_combo=ttk.Combobox(left_frame1,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        corse_combo["values"]=("Select Your Course","FE","SE","BE","ME")
        corse_combo.current(0)
        corse_combo.grid(row=0,column=3,padx=10)

        #YEAR
        YEAR_label=Label(left_frame1,text="Year",font=("times new roman",12,"bold"))
        YEAR_label.grid(row=1,column=0,padx=2,pady=10)

        YEAR_combo=ttk.Combobox(left_frame1,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        YEAR_combo["values"]=("Select Year","2020-21","2021-22","2022-23")
        YEAR_combo.current(0)
        YEAR_combo.grid(row=1,column=1,padx=10)

        #semister
        semester_label=Label(left_frame1,text="Semester",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=2,pady=10)

        semester_combo=ttk.Combobox(left_frame1,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-4","sem-5")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=10)

        #CLASS STUDENT INFORMATION
        left_frame2=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        left_frame2.place(x=5,y=250,width=690,height=300)

        #student id
        semesterID_label=Label(left_frame2,text="StudentID",font=("times new roman",12,"bold"))
        semesterID_label.grid(row=0,column=0,padx=2,pady=10)

        studentID_entry=ttk.Entry(left_frame2,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student name
        semestername_label=Label(left_frame2,text="StudentName",font=("times new roman",12,"bold"))
        semestername_label.grid(row=0,column=2,padx=2,pady=10)

        studentname_entry=ttk.Entry(left_frame2,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,sticky=W)

        #roll number
        semesterroll_no_label=Label(left_frame2,text="Roll No.",font=("times new roman",12,"bold"))
        semesterroll_no_label.grid(row=1,column=0,padx=2,pady=10)

        studentroll_no_entry=ttk.Entry(left_frame2,width=20,font=("times new roman",12,"bold"))
        studentroll_no_entry.grid(row=1,column=1,padx=10,sticky=W)

        #email
        semesteremail_label=Label(left_frame2,text="Email",font=("times new roman",12,"bold"))
        semesteremail_label.grid(row=1,column=2,padx=2,pady=10)

        studentemail_entry=ttk.Entry(left_frame2,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        studentemail_entry.grid(row=1,column=3,padx=10,sticky=W)

        #gender
        semestergender_label=Label(left_frame2,text="Gender",font=("times new roman",12,"bold"))
        semestergender_label.grid(row=2,column=0,padx=2,pady=10)

        gender_combo=ttk.Combobox(left_frame2,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="readonly")
        gender_combo["values"]=("select gender","Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10)

        #phone number
        semesterphno_label=Label(left_frame2,text="Phone no.",font=("times new roman",12,"bold"))
        semesterphno_label.grid(row=2,column=2,padx=2,pady=10)

        studentphno_entry=ttk.Entry(left_frame2,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        studentphno_entry.grid(row=2,column=3,padx=10,sticky=W)

    

        #RADIO BUTTONS
        self.var_radio1=StringVar()
        radonbtn=ttk.Radiobutton(left_frame2,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radonbtn.grid(row=4,column=0)
        radonbtn2=ttk.Radiobutton(left_frame2,variable=self.var_radio1,text="No Photo Sample",value="no")
        radonbtn2.grid(row=4,column=1)

        #button frame
        btn_frame=Frame(left_frame2,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=170,width=715,height=40)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="update",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="delete",command=self.delete_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(left_frame2,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=210,width=715,height=35)

        take_btn=Button(btn_frame1,text="Take photo",command=self.generate_dataset,width=38,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_btn.grid(row=0,column=0)

        update1_btn=Button(btn_frame1,text="Update photo",width=38,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update1_btn.grid(row=0,column=1)



        #righht frame
        rigth_frame=LabelFrame(MAIN_FRAME,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        rigth_frame.place(x=710,y=10,width=720,height=580)

        img_right=Image.open(r"C:\Users\User\Pictures\Camera Roll\images (4).jfif")
        img_right=img_right.resize((680,140),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_label=Label(rigth_frame,image=self.photoimg_right)
        f_label.place(x=5,y=0,width=680,height=140)

        #search sytem
        search_frame2=LabelFrame(rigth_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame2.place(x=5,y=145,width=690,height=70)

        search_label=Label(search_frame2,text="Search by:",font=("times new roman",12,"bold"))
        search_label.grid(row=0,column=0,padx=2,pady=10)

        search_combo=ttk.Combobox(search_frame2,font=("times new roman",12,"bold"),width=17,state="readonly")
        search_combo["values"]=("Select","Roll.NO","Phone.No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10)

        search_entry=ttk.Entry(search_frame2,width=16,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)

        search_btn=Button(search_frame2,text="search",cursor="hand2",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame2,text="Show All",cursor="hand2",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)
        
        #table frame
        table_frame2=LabelFrame(rigth_frame,bd=2,bg="white",relief=RIDGE)
        table_frame2.place(x=5,y=250,width=690,height=250)

        scroll_x=ttk.Scrollbar(table_frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame2,orient=VERTICAL)

        self.studnet_table=ttk.Treeview(table_frame2,column=("dep","course","year","sem","id","name","gender","email","phone.no","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.studnet_table.xview)
        scroll_y.config(command=self.studnet_table.yview)


        self.studnet_table.heading("dep",text="Department")
        self.studnet_table.heading("course",text="course")
        self.studnet_table.heading("year",text="Year")
        self.studnet_table.heading("sem",text="Semester")
        self.studnet_table.heading("id",text="StudentID")
        self.studnet_table.heading("name",text="StudentName")
        self.studnet_table.heading("gender",text="Gender")
        self.studnet_table.heading("email",text="Email")
        self.studnet_table.heading("phone.no",text="Phone no.")
        self.studnet_table.heading("photo",text="photosample")
        self.studnet_table["show"]="headings"

        self.studnet_table.column("dep",width=100)
        self.studnet_table.column("course",width=100)
        self.studnet_table.column("year",width=100)
        self.studnet_table.column("sem",width=100)
        self.studnet_table.column("id",width=100)
        self.studnet_table.column("name",width=100)
        self.studnet_table.column("gender",width=100)
        self.studnet_table.column("email",width=100)
        self.studnet_table.column("phone.no",width=100)
        self.studnet_table.column("photo",width=150)

        self.studnet_table.pack(fill=BOTH,expand=1)
        self.studnet_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #function
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("error!","do fill everydetails",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Akshatha17*",database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_id.get(),self.var_name.get(),self.var_gender.get(),self.var_email.get(),self.var_phone.get(),self.var_radio1.get()))                                                        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("error!",f"due to:{str(es)}",parent=self.root) 
            

    #fetch data
    def fetch_data(self):
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Akshatha17*",database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.studnet_table.delete(*self.studnet_table.get_children())
                    for i in data:
                        self.studnet_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
    #get cursor
    def get_cursor(self,event=" "):
        cursor_focus=self.studnet_table.focus()
        content=self.studnet_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4])
        self.var_name.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_email.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_radio1.set(data[9])

    #update
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("error!","do fill everydetails",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("update","Do you want to update",parent=self.root)
                if Update:
                    conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Akshatha17*",database="facerecognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,gender=%s,email=%s,phone=%s,photosample=%s where id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_name.get(),self.var_gender.get(),self.var_email.get(),self.var_phone.get(),self.var_radio1.get(),self.var_id.get()))
                else:
                    if not Update:
                        return
                messagebox.showinfo("success","student detail successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                    
            except Exception as es:
                messagebox.showerror("error!",f"due to:{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("error","id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student Delete page","do ypu want to delete",parent=self.root) 
                if delete:
                    conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Akshatha17*",database="facerecognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","Are you sure to delete",parent=self.root)
            except Exception as es:
                messagebox.showerror("error!",f"due to:{str(es)}",parent=self.root)
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Sem")
        self.var_id.set("")
        self.var_name.set("Select Department")
        self.var_gender.set("select gender")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")
    #generte
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("error!","do fill everydetails",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Akshatha17*",database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,gender=%s,email=%s,phone=%s,photosample=%s where id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_name.get(),self.var_gender.get(),self.var_email.get(),self.var_phone.get(),self.var_radio1.get(),self.var_id.get()))
                self.fetch_data()
                self.reset_data()
                conn.close()
                #load predefined data 
                face_classifier=cv2.CascadeClassifier('algorithm.xml')
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray, 1.3, 5)
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                        
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                messagebox.showinfo("result","genedrating dataset successfull")
            except Exception as es:
                messagebox.showerror("error!",f"due to:{str(es)}",parent=self.root)


                
                



                



                        

                        


                        






    

                    
        
    
                



            



        



  


            











        













 


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()



