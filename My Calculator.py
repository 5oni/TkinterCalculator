from tkinter import Tk,LEFT, Entry,BOTH,Canvas,Frame, W, Button, E, Label,RIGHT, Y, X,StringVar,IntVar
t=Tk()
t.title("Calculator")
t.configure(background="grey")
t.geometry("323x435")
t.resizable(0,0)
txt=StringVar()
txt1=StringVar()
e1=Entry(t,font=("",15),justify="right",bg="black",fg="white",textvariable=txt1,bd="0")
e1.place(x=0,y=0,width="323",height="50")
e2=Entry(t,font=("",25),justify="right",bg="black",fg="white",textvariable=txt)
e2.place(x=0,y=50,width="323",height="80")
e2.focus_set()
button=[Button()]*24
data=["%","CE","C","Del","1/x","sq","sqrt","÷","7","8","9","x","4","5","6","-","1","2","3","+","+/-","0",".","="]
k,a,b=0,0.5,130
def excpt():
    if txt.get()=="":
        txt1.set("Enter a valid number")
    ls1=[]
    ls=[]
    for t in txt.get():
        ls1.append(t)
    for i in txt.get():
        for j in data:
            if i==j:
                ls.append(i)
    if ls!=ls1:
        txt1.set("Enter a valid number")
def show(c):
    if txt.get()=="0.0":
        txt.set("")
        txt.set(txt.get()+c)
    else:
        txt.set(txt.get()+c)
def clrE():
    txt.set("")
def equa(event=None):
    try:
        z=txt.get()
        ex=eval(z)
        txt1.set(txt.get()+"=")
        txt.set(ex)
    except:
        excpt()
    
def percent():
    try:
        p=float(txt.get())
        txt1.set(txt.get()+"% =")
        txt.set(p/100)
    except:
        excpt()
def clr():
    txt.set("")
    txt1.set("")
def delete():
    global txt
    current=txt.get()
    current = current[:-1] 
    if current: 
       txt.set(current)
    else: 
       txt.set("")
def inverse():
    try:
        
        i=float(txt.get())
        txt1.set("1/"+txt.get()+" =")
        txt.set(1/i)
    except:
        excpt()
def square():
    try:
        s=float(txt.get())
        txt1.set(txt.get()+"^2 =")
        txt.set(s*s)
    except:
        excpt()
def sqrt():
    try:
        
        s=float(txt.get())
        txt1.set(txt.get()+"^(0.5) =")
        txt.set(s**0.5)
    except:
        excpt()
def sign():
    txt.set(float(txt.get())*-1)

for i in range(6):
    for j in range(4):
        button[k]=Button(t,text=data[k],font=("",15),bg="#111111",fg="white",activebackground="cyan")
        button[k].place(x=a,y=b,height="50",width="80")
        k+=1
        a+=80.5
    a=0.5
    b+=50.5
button[0].configure(bg="#070707",command=percent)
button[1].configure(bg="#070707",command=clrE)
button[2].configure(bg="#070707",command=clr)
button[3].configure(bg="#070707",command=delete)
button[4].configure(bg="#070707",command=inverse)
button[5].configure(bg="#070707",command=square)
button[6].configure(bg="#070707",command=sqrt)
button[7].configure(bg="#070707",command=lambda : show("/"))
button[8].configure(command=lambda : show(data[8]))
button[9].configure(command=lambda : show(data[9]))
button[10].configure(command=lambda : show(data[10]))
button[11].configure(bg="#070707",command=lambda : show("*"))
button[12].configure(command=lambda : show(data[12]))
button[13].configure(command=lambda : show(data[13]))
button[14].configure(command=lambda : show(data[14]))
button[15].configure(bg="#070707",command=lambda : show(data[15]))
button[16].configure(command=lambda : show(data[16]))
button[17].configure(command=lambda : show(data[17]))
button[18].configure(command=lambda : show(data[18]))
button[19].configure(bg="#070707",command=lambda : show(data[19]))
button[20].configure(command=sign)
button[21].configure(command=lambda : show(data[21]))
button[22].configure(command=lambda : show(data[22]))
button[23].configure(bg="brown",command=equa)
t.bind("<Return>",lambda event=None: button[23].invoke())

t.mainloop()
