from tkinter import *


win=Tk()

win.title("MSG")
win.geometry("%dx%d+%d+%d"%(400,200,450,200))
win.configure(bg="lightgreen")

def cheack(e):
    if txt_msg.get()=="yes":
        win.withdraw()
    else:
        lbl3.configure(text="مقدار درونی درست وارد نشد")



#txt
txt_msg=Entry(win,width=30)
txt_msg.place(x=110,y=100)

#lbl
lbl_title=Label(win,text="حذف اطلاعات نزدیک شماست",fg="red",font=50)

lbl_title.pack(side="top",fill=BOTH)

lbl_msg=Label(win,text="Yes or No",font=50,fg="red",bg="lightgreen")
lbl_msg.place(x=165,y=70)

lbl3=Label(win,text="",bg="lightgreen",fg="red")
lbl3.pack(side="bottom",fill=BOTH)

#btn
btn_smg=Button(win,text="تایید",width=15)
btn_smg.bind("<Button-1>",cheack)
btn_smg.place(x=146,y=145)



















win.mainloop()