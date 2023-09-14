import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


win=Tk()

win.title("REGISTER")
win.geometry("%dx%d+%d+%d"%(600,310,400,70))
win.configure(bg="lightgreen")
users=[]
#def
def onclickregister(e):
    if  btn_rgister.cget("state")==NORMAL:
        try:
            dic={"name":txt_name.get(),"lastname":txt_lastname.get(),"age":int(txt_age.get())}
            if exist(dic)==False:
                load()
                register(dic)
                insert(dic)
                txt_name.focus_set()
                txtnamevar.set("")
                txtlastnamevar.set("")
                txtagevar.set("")
            else:
                messagebox.showwarning("Rep","فرد تکراری میاشد")
        except:
            messagebox.showwarning("Error","خطایی رخ داده است")


def register(vlue):
    users.append(vlue)


def insert(value):
    tbl_search.insert('',"end",values=[value["name"],value["lastname"],str(value["age"])])

def activebtn(e):
    if txt_name.get()=="":
        btn_rgister.configure(state=DISABLED)
    else:
       btn_rgister.configure(state=NORMAL)



def getselection(e):
    selection=tbl_search.selection()
    if selection!=():
        s=tbl_search.item(selection)["values"]
        txtnamevar.set(s[0])
        txtlastnamevar.set(s[1])
        txtagevar.set(s[2])

def onclicksearch(e):
    search1=txt_search.get()
    result=search(search1)
    clear()
    for item in result:
        insert(item)

def search(value):
    resultlist = []
    for item in users:
        if item["name"] == txt_search.get() or item["lastname"] == txt_search.get() or str(item["age"]) == txt_search.get():
            resultlist.append(item)
    return resultlist

def clear():
    for item in tbl_search.get_children():
        sel=str(item,)
        tbl_search.delete(sel)

def load_and_clear(value):
    for item in tbl_search.get_children():
        sel=str(item,)
        tbl_search.delete(sel)
    for item in  value:
        tbl_search.insert('', "end", values=[value["name"], value["lastname"], str(value["age"])])

def exist(value):
    for item in users:
       if item["name"]==value["name"] and item["lastname"]==value["lastname"] and item["age"]==value["age"]:
            return True
    return False

def onclickdelet(e):
    dialog=shoemsg()

    if dialog==True:
        dic={"name":txt_name.get(),"lastname":txt_lastname.get(),"age":txt_age.get()}
        delet(dic)
        remove_tbl()
def delet(value):
    for item in users:
        if item["name"] == value["name"]  and item["lastname"] == value["lastname"]  and item["age"] == value["age"]:
            users.remove(value)

def remove_tbl():
    selection = tbl_search.selection()
    if selection != ():
         tbl_search.delete(selection)


def shoemsg():
    os.system(f"msg.py")

def onclickupdate(e):
    select=tbl_search.selection()
    if select!=():
        select_item=tbl_search.item(select)["values"]
        dic={"name":select_item[0],"lastname":select_item[1],"age":int(select_item[2])}
        index1=update(dic)
        p=users[index1]
        tbl_search.item(select,values=[p["name"],p["lastname"],p["age"]])


def update(value):
    index=users.index(value)
    users[index]={"name":txt_name.get(),"lastname":txt_lastname.get(),"age":int(txt_age.get())}
    return index

def load():
    clear()
    for item in users:
        insert(item)


txtnamevar=StringVar()
txtlastnamevar=StringVar()
txtagevar=StringVar()
txtsearchvar=StringVar()

#txt
txt_name=Entry(win,width=30,textvariable=txtnamevar)
txt_name.bind("<KeyRelease>",activebtn)
txt_name.place(x=100,y=60)

txt_lastname=Entry(win,width=30,textvariable=txtlastnamevar)
txt_lastname.place(x=100,y=120)

txt_age=Entry(win,width=30,textvariable=txtagevar)

txt_age.place(x=100,y=180)

txt_search=Entry(win,width=20)
txt_search.place(x=380,y=30)

#lbl
lbl_name=Label(win,text="Name :",bg="lightgreen",font=30)
lbl_name.place(x=1,y=60)

lbl_lastname=Label(win,text="Last name :",bg="lightgreen",font=30)
lbl_lastname.place(x=1,y=120)

lbl_age=Label(win,text="Age :",bg="lightgreen",font=30)
lbl_age.place(x=1,y=180)

lbl_search=Label(win,text="Search",bg="lightgreen",)
lbl_search.place(x=340,y=30)

#BTN
btn_rgister=Button(win,text="Rgister",width=25)
btn_rgister.configure(state=DISABLED)
btn_rgister.bind("<Button-1>",onclickregister)
btn_rgister.place(x=100,y=220)

btn_search=Button(win,text="Search",width=5)
btn_search.bind("<Button-1>",onclicksearch)
btn_search.place(x=517,y=30)

btn_delet=Button(win,text="delet",width=25)
btn_delet.bind("<Button-1>",onclickdelet)
btn_delet.place(x=100,y=250)

btn_update=Button(win,text="Update",width=25)
btn_update.bind("<Button-1>",onclickupdate)
btn_update.place(x=100,y=280)

#tbl
column=("c1","c2","c3")
tbl_search=ttk.Treeview(win,columns=("c1","c2","c3"),show="headings",height=10)

tbl_search.heading("c1", text="name")
tbl_search.column("c1",width=80)
tbl_search.heading("c2", text="lastname")
tbl_search.column("c2",width=80)
tbl_search.heading("c3", text="age")
tbl_search.column("c3",width=80)

tbl_search.bind("<Button-1>",getselection)

tbl_search.place(x=320,y=60)




























win.mainloop()