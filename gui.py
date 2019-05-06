from tkinter import *
from tkinter import messagebox
from test import result
def getInfo():
    FFMC = (E1.get())
    DMC = (E2.get())
    DC = (E3.get())
    ISI = (E4.get())
    temp = (E5.get())
    RH = (E6.get())
    wind = (E7.get())
    test = []
    test.append(float(FFMC))
    test.append(float(DMC))
    test.append(float(DC))
    test.append(float(ISI))
    test.append(float(temp))
    test.append(float(RH))
    test.append(float(wind))
    ketqua =  result(test)
    if ketqua == 0:
        message = 'Rừng không có nguy cơ bị cháy'
    else:
        message = 'Rừng có nguy cơ bị cháy'
    messagebox.showinfo("Kết quả", message)
top = Tk(className='Cảnh báo cháy rừng')
top.minsize(width=300, height=500)
top.maxsize(width=300, height=500)
L1 = Label(top, text="FFMC")
L1.pack()
E1 =Entry(top, bd=5)
E1.pack()
L2 = Label(top, text="DMC")
L2.pack()
E2 =Entry(top, bd=5)
E2.pack()
L3 = Label(top, text="DC")
L3.pack()
E3 =Entry(top, bd=5)
E3.pack()
L4 = Label(top, text="ISI")
L4.pack()
E4 =Entry(top, bd=5)
E4.pack()
L5 = Label(top, text="temp")
L5.pack()
E5 =Entry(top, bd=5)
E5.pack()
L6 = Label(top, text="RH")
L6.pack()
E6 =Entry(top, bd=5)
E6.pack()
L7 = Label(top, text="wind")
L7.pack()
E7 =Entry(top, bd=5)
E7.pack()
B = Button(top, text="submit",command=getInfo)
B.pack()
close = Button(top, text='Close', command=top.destroy)
close.pack()
top.mainloop()



