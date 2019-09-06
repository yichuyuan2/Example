#Python GUI
import tkinter as tk

def callback():
    var.set("吹吧你，我才不信呢~")

#创建一个toplevel的根窗口并将它作为参数实例化app对象
root = tk.Tk()

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

#创建一个文本label对象
var = tk.StringVar()
var.set("您所观看的影片含有未成年人限制内容,\n 请满18岁后再点击观看")
textLabel = tk.Label(frame1, textvariable = var, justify = tk.LEFT)
textLabel.pack(side = tk.LEFT)
#创建一个按钮
theButton = tk.Button(frame2, text = "已满18周岁", command = callback)
theButton.pack()

frame1.pack(padx = 10, pady = 10)
frame2.pack(padx = 10, pady = 10)

#开始主事件循环
root.mainloop()