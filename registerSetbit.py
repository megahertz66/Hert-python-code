from tkinter import *
# 导入ttk
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
        self.number = 0

    def initWidgets(self):
        self.st16 = StringVar()  # ShringVar()：用于包装str 值的变量
        self.st10 = StringVar()
        self.st8  = StringVar()
        #创建ttk容器
        f1 = ttk.Frame(self.master)
        f1.pack(side=TOP)
        f2 = ttk.Frame(self.master)
        f2.pack(side=TOP, ipady=20) #ipad参数设置距离其他组件y方向高度距离
        #用于放置复位按钮部件
        f3 = ttk.Frame(self.master)
        f3.pack(side=TOP, ipady=20)
        self.l = list(range(32))

        #创建32个标签，模拟不弹起按钮
        for i in range(32):
            #创建Lable组件
            self.l[i] = Label(f1, text=i, relief=SUNKEN, font=('Verdana', 10), width=5, background='white')
            #为label绑定单击事件
            self.l[i].bind('<Button-1>', self.click)
            self.l[i].grid(row=i // 16, column=i % 16)
        print(self.l)

        ttk.Entry(f2, textvariable=self.st16, font=('StSong', 15, 'bold'), width=50).pack(side=TOP, expand=YES)
        ttk.Entry(f2, textvariable=self.st10, font=('StSong', 15, 'bold'), width=50).pack(side=TOP, expand=YES)
        ttk.Entry(f2, textvariable=self.st8 , font=('StSong', 15, 'bold'), width=50).pack(side=TOP, expand=YES)
        ttk.Button(f3, text='重新开始', command=self.overset).pack(side=TOP)
    def click(self, event):
        #使用这种方式将label变成不弹起按钮更加合理
        if event.widget['background'] == 'green':
            event.widget['background'] = 'white'
            self.number = self.number & ~(1 << event.widget['text'])
        else:
            event.widget['background'] = 'green'
            self.number = self.number | (1 << event.widget['text'])

        self.st16.set("HEX:   %x" % self.number)
        self.st10.set("DEC:   %d" % self.number)
        self.st8.set ("OCT:   %o" % self.number)

    def overset(self):
        self.st16.set("HEX:   ")
        self.st10.set("DEC:   ")
        self.st8.set ("OCT:   ")
        self.number = 0
        for i in range(32):
            (self.l[i]).configure(background = 'white')



root = Tk()
root.title('置位器(可复制版本)')
root.geometry("800x250+30+30")
App(root)
root.mainloop()
