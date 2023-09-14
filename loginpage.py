from tkinter import *
import login
import listrgister

win=Tk()

win.title("Login Page")
win.geometry("%dx%d+%d+%d"%(700,400,400,70))
win.configure(bg="lightgreen")

#def
def btnlogin(e):

    login.login_1()

def list1(e):

    listrgister.list()

def forget(e):
    win.destroy()


#lbl
lbl_name=Label(win,text="<Welcome to the login page>",bg="#E6B325",font=50)
lbl_name.pack(side="top",fill=BOTH)






#btn
btn_login=Button(win,text="Login",width=25,height=2)
btn_login.bind("<Button-1>",btnlogin)
btn_login.place(x=480,y=80)

btn_list=Button(win,text="List",width=25,height=2)
btn_list.bind("<Button-1>",list1)
btn_list.place(x=480,y=160)

btn_exit=Button(win,text="Exit",width=25,height=2,fg="red")
btn_exit.bind("<Button-1>",forget)
btn_exit.place(x=480,y=240)
























win.mainloop()