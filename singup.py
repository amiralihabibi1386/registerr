from tkinter import *
from tkinter import messagebox

users=[]

def showmsg():

        win=Tk()
        win.title("Sing up")
        win.geometry("%dx%d+%d+%d"%(600,600,400,70))
        win.configure(bg="lightgreen")


        def singup(e):
            b=False
            for item in users:
                if item["user"]==txt_user.get():
                    messagebox.showinfo("","تکراری")
                    b=True
                    break
            if b==False:
                if txt_password.get()==txt_repassword.get():
                    dic={"user":txt_user.get(),"password":txt_password.get()}
                    users.append(dic)
                else:
                    messagebox.showwarning("Error","Please check the password")


        #txt
        txt_user=Entry(win,width=30)
        txt_user.place(x=210,y=100)

        txt_password=Entry(win,width=30,)
        txt_password.place(x=210,y=160)

        txt_repassword=Entry(win,width=30,)
        txt_repassword.place(x=210,y=220)

        #lbl
        lbl_user=Label(win,text="User",bg="lightgreen",font=30)
        lbl_user.place(x=160,y=95)

        lbl_password=Label(win,text="Password",bg="lightgreen",font=30)
        lbl_password.place(x=130,y=155)

        lbl_title=Label(win,text="<به صفحه ورود خوش امدید>" ,font=50,)
        lbl_title.pack(side="top",fill=BOTH)

        lbl_repassword=Label(win,text="Repassword",bg="lightgreen",font=30)
        lbl_repassword.place(x=115,y=215)

        #btn
        btn_singup=Button(win,text="sing up",width=25)
        btn_singup.bind("<Button-1>",singup)
        btn_singup.place(x=210,y=280)











        win.mainloop()