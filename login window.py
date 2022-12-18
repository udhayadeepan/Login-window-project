import mysql.connector
from tkinter import *
from tkinter import messagebox
import os
win=Tk()
win.title("LOGIN PAGE PROJECT")
win.resizable(0,0)
win.geometry("300x340")
win.configure()
Label(win,text=" LOGIN WINDOW ",bg="light blue").pack(pady=15,fill='both')
f1=Frame(win)
f2=Frame(win)
f3=Frame(win)
log=Frame(win)
image_path=str(os.getcwd())+"\image\open.png"
bg=PhotoImage(file=image_path)
image_path2=str(os.getcwd())+"\image\close.png"
bg2=PhotoImage(file=image_path2)
image_path3=str(os.getcwd())+"\image\one.png"
bg3=PhotoImage(file=image_path3)
image_path4=str(os.getcwd())+"\image\suc.png"
success=PhotoImage(file=image_path4)
image_path5=str(os.getcwd())+"\image\wrong.png"
fail=PhotoImage(file=image_path5)

label1=Label(f1,image=bg)
label1.grid(column=1)

mydb=mysql.connector.connect(host="127.0.0.1",user="root",password="udhaya.p23")

sql=mydb.cursor()
try:
      sql.execute("create database login_page")
      sql.execute("use login_page")
      sql.execute("create table user_data(username varchar(50) primary key,password varchar(50) ,security_qn varchar(50),security_ans varchar(50))")
      
except:
      sql.execute("use login_page")
            
def Login():
      f3.pack_forget()
      f2.pack_forget()
      f1.pack(fill=X)
      log.forget()
      Signup.configure(comman=new_user,text="New User?Signup")
      reset.configure(text="Forget Password?",command=forget)
      reset.place(x=200,y=280)
      Label(f1,text="Username").grid(row=1,column=0,padx=10,pady=5)
      ID=Entry(f1)
      ID.grid(row=1,column=1)
      Label(f1,text="Password").grid(row=2,column=0,padx=10,pady=5)
      Pass=Entry(f1,show='*')
      Pass.grid(row=2,column=1)
      
      def verify():
            userID=ID.get()
            Password=Pass.get()
            syn="select * from user_data where username=%s"
            val=[userID]
            sql.execute(syn,val)
            for i in sql:
                  if Password==i[1]:
                        f1.forget()
                        log.pack(fill="both")
                        Label(log,image=success).grid(row=0,column=0,sticky="nsew",padx=70)
                        Label(log,text="Login Succefully!").grid(row=1,column=0,sticky="nsew")
                        #Button(log,text="Back to login",command=Login).grid(row=2,column=0,padx=40)
                  else:
                        f1.forget()
                        log.pack(fill="both")
                        Label(log,image=fail).grid(row=0,column=0,sticky="nsew",padx=70)
                        Label(log,text="I think You forget your username or password!").grid(row=1,column=0,sticky="nsew")
            Button(log,text="Back to login",command=Login).grid(row=2,column=0,padx=30)                        
            ID.delete(0,END)
            Pass.delete(0,END)
      
      def focusin(event):
            label1.configure(image=bg2)
            def show():
                  Pass.configure(show='')
                  label1.configure(image=bg3)
                  def hide():
                        Pass.configure(show='*')
                        label1.configure(image=bg2)
                        show_but.configure(text="show",command=show)
                  show_but.configure(text="hide",command=hide)
            global show_but
            show_but=Button(f1,text="show",command =show)
            show_but.grid(row=2,column=2,padx=5)
      
      def focusout(event):
            show_but.grid_forget()
            label1.configure(image=bg)
            Pass.configure(show='*')
      Pass.bind('<FocusIn>',focusin)
      Pass.bind('<FocusOut>',focusout)
      Button(f1,text="Login",command=verify).grid(row=3,column=1,pady=2)
      
def new_user():      
      f1.pack_forget()
      f2.pack_forget()
      f3.pack_forget()
      log.pack_forget()
      f2.pack(fill=X)
      Signup.configure(comman=Login,text="Login")
      reset.configure(text="Forget Password",command=forget)
      Label (f2,text="New User SignUp").grid(row=0,column=1)
      Label(f2,text="Username").grid(row=1,column=0,padx=10,pady=5)
      ID=Entry(f2)
      ID.grid(row=1,column=1)

      def Is_available():
            userID=ID.get()
            syn="select * from user_data where username=%s"
            val=[userID]
            sql.execute(syn,val)
            is_name_available=True
            for i in sql:
                  is_name_available=False
            if  is_name_available:
                  ID.configure(state=DISABLED)
                  avail.grid_forget()
                  Label(f2,text="Password").grid(row=2,column=0,padx=10,pady=5)
                  Pass=Entry(f2)
                  Pass.grid(row=2,column=1)
                  security_qns=["Favourite Place?","Favourite person?","First Love?","Favourite Food?"]
                  options=StringVar(f2)
                  options.set(security_qns[0])
                  Label(f2,text="Security Qn").grid(row=3,column=0,pady=5)
                  qn=OptionMenu(f2,options,*security_qns)
                  qn.grid(row=3,column=1,pady=5)
                  Label(f2,text="Security Ans").grid(row=4,column=0,pady=5)
                  ans=Entry(f2)
                  ans.grid(row=4,column=1,pady=5)
                  def create():
                        PassW=Pass.get()
                        #Qn=qn.get()
                        Ans=ans.get()
                        syn="insert into user_data(username,password,security_qn,security_ans) values(%s,%s,%s,%s)"
                        val=[userID,PassW,options.get(),Ans]
                        sql.execute(syn,val)
                        mydb.commit()
                        messagebox.showinfo("success","Account created Succesfully")
                        Login()
                  Button(f2,text="Create Account",command=create).grid(row=5,column=1,pady=5)
            else:
                  ID.delete(0,END)
                  messagebox.askretrycancel("Name already taken","Try any other names!")
      avail=Button(f2,text="Next",command=Is_available)
      avail.grid(row=2,column=1,pady=5)
      
def forget():
      f1.forget()
      f2.forget()
      log.forget()
      f3.pack(fill="both")
      Label(f3,text="Username").grid(row=0,column=0)
      user=Entry(f3)
      user.grid(row=0,column=1,padx=20)
      Signup.configure(command=Login,text="Login")
      reset.configure(text="New User?Signup",command=new_user)     
      def check():
            userID=user.get()
            syn="select * from user_data where username=%s"
            val=[userID]
            sql.execute(syn,val)
            user_present=False
            security_qn=""
            Password=''
            security_ans=""
            for i in sql:
                  user_present=True
                  Password=i[1]
                  security_qn=i[2]
                  security_ans=i[3]
            if user_present:
                  check.grid_forget()
                  user.configure(state=DISABLED)
                  qn_lab=Label(f3,text=security_qn)
                  qn_lab.grid(row=1,column=1,sticky="nsew",pady=2)
                  lab=Label(f3,text="enter your answer below")
                  lab.grid(row=2,column=1)
                  ans=Entry(f3)
                  ans.grid(row=3,column=1)
                  def verify_security():
                        temp=ans.get()
                        if ans.get()==security_ans:
                              ans.delete(0,END)
                              qn_lab.grid_forget()
                              lab.configure(text="Enter new Password")
                              def change():
                                    check.grid_forget()
                                    if Password==ans.get():
                                          messagebox.showwarning("warning","New password must not be same as old")
                                          ans.delete(0,END)      
                                    else:
                                          new_password=ans.get()
                                          syn="update user_data set password=%s where username=%s"
                                          val=[new_password,userID]
                                          sql.execute(syn,val)
                                          mydb.commit()
                                          messagebox.showinfo("INFO","password changed succefully")
                                          ans.delete(0,END)
                                          ans.grid_forget()
                                          lab.grid_forget()
                                          user.grid_forget()
                                          nex.grid_forget()
                                          Login()
                                          
                              nex.configure(text="Change Password",command=change)
                        else:
                              messagebox.showwarning("Worng Answer","Who the hell are you?")
                           
                  nex=Button(f3,text="Next",command=verify_security)
                  nex.grid(row=4,column=1)
            else :
                  messagebox.showwarning("warning","Wrong Username! Recheck Username")
                  
      check=Button(f3,text="Next",command=check)
      check.grid(row=1,column=1,pady=5)
   


Signup=Button(win,text="New User?signup",command=new_user)
Signup.place(x=1,y=280)
reset=Button(win,text="Forget Password!",command=forget)
reset.place(x=200,y=280)
Label(win,text="Code by : u_d_h_a_y_23").place(x=80,y=310)
Login()
win.mainloop()



