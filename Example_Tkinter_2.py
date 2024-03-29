#Python GUI-Tkinter
#Example_Entry
from tkinter import *

root = Tk()
#Tkinter提供了grid()方法允许使用表格的形式来管理组件的位置
Label(root, text = "账号：").grid(row = 0)
Label(root, text = "密码：").grid(row = 1)
v1 = StringVar()
v2 = StringVar()
e1 = Entry(root, textvariable = v1)
e2 = Entry(root, textvariable = v2, show = "*")
e1.grid(row = 0, column = 1, padx = 10, pady = 5)
e2.grid(row = 1, column = 1, padx = 10, pady = 5)

def show():
    print("账号： %s" % v1.get())
    print("密码： %s" % v2.get())
    e1.delete(0, END)
    e2.delete(0, END)

Button(root, text = "芝麻开门", width = 10, command = show).grid(row = 3, column = 0, sticky = W, padx = 10, pady = 5)
Button(root, text = "退出", width = 10, command = root.quit).grid(row = 3, column = 1, sticky = E, padx = 10, pady = 5)

mainloop()