from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def list():


    win=Tk()

    win.title("list")
    win.geometry("%dx%d+%d+%d"%(400,400,400,70))
    win.configure(bg="lightgreen")


    #txt
    txt_search=Entry(win,width=30)
    txt_search.place(x=120,y=12)

    #lbl
    lbl_search=Label(win,text="Search",bg="lightgreen")
    lbl_search.place(x=70,y=12)

    #btn
    btn_search=Button(win,text="Search",width=5)
    btn_search.bind("<Button-1>",)
    btn_search.place(x=310,y=10)



    #tbl
    column=("c1","c2","c3")
    tbl_search=ttk.Treeview(win,columns=column,show="headings",height=15)

    tbl_search.heading(column[0], text="name")
    tbl_search.column(column[0],width=110)
    tbl_search.heading(column[1], text="lastname")
    tbl_search.column(column[1],width=110)
    tbl_search.heading(column[2], text="age")
    tbl_search.column(column[2],width=110)

    tbl_search.place(x=30,y=50)


















    win.mainloop()