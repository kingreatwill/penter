"""
Tcl 是“工具控制语言（Tool Control Language）”的缩写。
Tk 是 Tcl“图形工具箱”的扩展，它提供各种标准的 GUI 接口项，以利于迅速进行高级应用程序开发。
Tcl/Tk（读作“tickle tee-kay”）
# http://www.tkdocs.com/
# https://www.tcl.tk/doc/
tkinter 包使用面向对象的方式对Tcl/Tk进行了一层薄包装

othergui:https://docs.python.org/zh-cn/3/library/othergui.html
"""
# python -m tkinter
# idle    当你安装python的时候,同时也安装了IDLE  开始”菜单→“所有程序”→“Python 3.5”→“IDLE（Python GUI）”


# https://docs.python.org/zh-cn/3/library/tk.html
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

# from tkinter import ttk
# import tkinter
#
# root = tkinter.Tk()
#
# style = ttk.Style()
# style.theme_settings("default", {
#    "TCombobox": {
#        "configure": {"padding": 5},
#        "map": {
#            "background": [("active", "green2"),
#                           ("!disabled", "green4")],
#            "fieldbackground": [("!disabled", "green3")],
#            "foreground": [("focus", "OliveDrab1"),
#                           ("!disabled", "OliveDrab2")]
#        }
#    }
# })
#
# combo = ttk.Combobox().pack()
#
# root.mainloop()