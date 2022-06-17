#!/usr/bin/python
from tkinter import *
from tkinter.messagebox import *


class Calculator:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("计算圆的周长和面积")
        self.frame.geometry("400x250")
        self.frame.resizable(FALSE, FALSE)
        self.frame["bg"] = "lightblue"

        self.var_radius = StringVar()

        self.Label_input = Label(self.frame, text="请输入圆的半径：", bg="lightgray", fg="black",
                                 font=("微软雅黑", 12, "bold"))
        self.Label_input.place(x=65, y=18)

        self.Entry_input = Entry(self.frame, font=("宋体", 14, "bold"), width=18,
                                 textvariable=self.var_radius, show="fault", state="normal", name="forth",
                                 justify="center",)
        self.Entry_input.place(x=90, y=60)

        # Button
        self.Button_cal = Button(self.frame, text="计算", bg="lightgray", fg="black",
                                 command=self.get_result, state="active", takefocus=1)
        self.Button_cal.place(x=320, y=60)

        # 蓝色
        self.Label2_input = Label(self.frame, text="圆的面积", bg="lightgray", fg="blue",
                                  font=("宋体", 12, "bold"), width=25)
        self.Label2_input.place(x=20, y=120)
        self.Label4_input = Label(self.frame, text="面积cal", bg="lightgray", fg="red",
                                  font=("宋体", 12, "bold"), width=25)
        self.Label4_input.place(x=20, y=180)

        # 红色
        self.Label3_input = Label(self.frame, text="圆的周长", bg="lightgray", fg="red",
                                  font=("宋体", 12, "bold"), width=25)
        self.Label3_input.place(x=180, y=120)
        self.Label5_input = Label(self.frame, text="周长cal", bg="lightgray", fg="red",
                                  font=("宋体", 12, "bold"), width=25)
        self.Label5_input.place(x=180, y=180)

    def show(self):
        self.frame.mainloop()

    def get_result(self):
        pi = 3.1415926
        radius = float(self.var_radius.get())
        c = self.Label4_input["text"] = pi * 2 * radius
        s = self.Label5_input["text"] = pi * radius ** 2
        showinfo(message="{0}{1}".format(str(c), str(s)), title="world")


if __name__ == '__main__':
    this_gui = Calculator()
    if True:
        pass
    try:
        this_gui.show()
    except errorfo:
        showinfo(message="请输入数字!")
