from tkinter import Label,Spinbox,Button,DISABLED,NORMAL,Tk
window=Tk()
window.title("CALENDER")
window.iconbitmap('download.ico')
#day
Label(window,text=" DAY",font=10).grid(row=0)
d=Spinbox(window,from_=1,to=31,width=3,bd=5,wrap=True)
d.grid(row=0,column=1)
#month
Label(window,text="MONTH",font=10).grid(row=0,column=4)
m=Spinbox(window,from_=1,to=12,width=3,bd=5,wrap=True)
m.grid(row=0,column=5)
#year
Label(window,text="YEAR",font=10).grid(row=0,column=7)
y=Spinbox(window,from_=0,to=2020,width=10,bd=5,wrap=True)
y.grid(row=0,column=8)
#center window
def center_window(width=300, height=200):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
center_window(323, 150)
window.resizable(0,0)

def  calender():
    global k
    year=int(y.get())
    month=int(m.get())
    day=int(d.get())
    a,b=0,0
    for i in range(1,month):
        if i<8 and i!=2:
            if i%2==0:
                a+=2
            else:
                a+=3
        elif i==2:
            if year%4==0:
                a+=1
            else:
                a+=0
        elif i>=8:
            if i%2==0:
                a+=3
            else:
                a+=2
    b=(year-1)%100
    c=b//4
    s=a+b+c+day
    w=s%7
    if w==0:
        k=Label(window,text="sunday",font=("arial bold",20))
        k.place(x=115,y=110)
    elif w==1:
        k=Label(window,text="monday",font=("arial bold",20))
        k.place(x=115,y=110)
    elif w==2:
        k=Label(window,text="tuesday",font=("arial bold",20))
        k.place(x=115,y=110)
    elif w==3:
        k=Label(window,text="wednesday",font=("arial bold",20))
        k.place(x=115,y=110)
    elif w==4:
        k=Label(window,text="thursday",font=("arial bold",20))
        k.place(x=115,y=110)
    elif w==5:
        k=Label(window,text="friday",font=("arial bold",20))
        k.place(x=115,y=110) 
    elif w==6:
        k=Label(window,text="saturday",font=("arial bold",20))
        k.place(x=115,y=110)
    mybutton['state']=DISABLED
mybutton=Button(window,text="CHECK",command=calender)
mybutton.place(x=130,y=50)
def clear():
    k.destroy()
    mybutton['state']=NORMAL
Button(window,text="Clear",command=clear).place(x=135.4,y=80)
window.mainloop()
