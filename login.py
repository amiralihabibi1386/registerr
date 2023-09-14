import os
from tkinter import *
import singup
from tkinter import ttk
from tkinter import messagebox



def login_1():

    win=Tk()
    win.title("Log in")
    win.geometry("%dx%d+%d+%d"%(400,400,500,70))
    win.configure(bg="lightgreen")
    users=[]

    def sing_up1(e):

        singup.showmsg()

    def onclicklogin(e):
        result=login()
        if result:
            os.system(f"register.py")
        else:
            messagebox.showwarning("","خطایی در یوزر یا پسوورد رخ داده است")

    def login():
        for item in singup.users:
            if item["user"]==txt_user.get() and item["password"]==txt_password.get():
                return True
        return False




    #txt
    txt_user=Entry(win,width=30)
    txt_user.place(x=110,y=100)

    txt_password=Entry(win,width=30,)
    txt_password.place(x=110,y=160)



    #lbl
    lbl_user=Label(win,text="User",bg="lightgreen",font=30)
    lbl_user.place(x=70,y=95)

    lbl_password=Label(win,text="Password",bg="lightgreen",font=30)
    lbl_password.place(x=33,y=155)



    lbl_title=Label(win,text="<به صفحه ورود خوش امدید>" ,font=50,)
    lbl_title.pack(side="top",fill=BOTH)

    #btn
    btn_login=Button(win,text="log in",width=25)
    btn_login.bind("<Button-1>",onclicklogin)
    btn_login.place(x=110,y=230)

    #lbllink
    lbl_link=ttk.Label(win,text="<برای ثیت نام کلیک کنید>",font=50)
    lbl_link.bind("<Button-1>",sing_up1)
    lbl_link.pack(side="bottom")









    win.mainloop()