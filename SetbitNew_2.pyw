from tkinter import *
from tkinter import messagebox
from turtle import left

window = Tk()
window.title('置位器')       # 设置窗口的标题
window.geometry('750x300')     # 设置窗口的大小

global number
number=0

bitmap = list(range(32))

st16 = StringVar()
st10 = StringVar()
st8 = StringVar()
st2 = StringVar()

# 放置各种进制数组
frame1 = Frame(window, relief=RAISED, borderwidth=1)
frame1.pack(side=TOP, fill=X, ipadx=0, ipady=0, expand=0)

# 放置 label
frame2 = Frame(window, relief=RAISED, borderwidth=3)
frame2.pack(side=TOP, fill=X, ipadx=0, ipady=0, expand=0)

hex_label = Label(frame1, text="HEX:")
dec_label = Label(frame1, text="DEC:")
oct_label = Label(frame1, text="OCT:")
bin_label = Label(frame1, text="BIN:")

hex_entry = Entry(frame1, width=50, textvariable=st16)           # 十六进制窗体
dec_entry = Entry(frame1, width=50, textvariable=st10)           # 十进制窗体
oct_entry = Entry(frame1, width=50, textvariable=st8)           # 八进制窗体
bin_entry = Entry(frame1, width=50, textvariable=st2)           # 二进制窗体


hex_label.grid(row=0, column=0)
hex_entry.grid(row=0,column=1, columnspan=3)

dec_label.grid(row=1, column=0)
dec_entry.grid(row=1, column=1, columnspan=3)

oct_label.grid(row=2, column=0)
oct_entry.grid(row=2,column=1, columnspan=3)

bin_label.grid(row=3,column=0)
bin_entry.grid(row=3,column=1, columnspan=3)


def click(event):
    global number
    number = 0
    if event.widget['background'] == 'green':
        event.widget['background'] = 'white'
        #number = number & ~(1 << event.widget['text'])
    else:
        event.widget['background'] = 'green'
        #number = number | (1 << event.widget['text'])

    for i in range(32):
        if bitmap[i]['background'] == 'green' :
            number = number + (1 << i)
            
    st16.set("%x" % number)
    st10.set("%d" % number)
    st8.set("%o" % number)
    st2.set("%s" % bin(number)[2:])


for i in range(32):
    # 创建Lable组件
    bitmap[i] = Label(frame2, text=i, relief=SUNKEN, font=('Verdana', 10), width=5, background='white')
    # 为label绑定单击事件
    bitmap[i].bind('<Button-1>', click)
    bitmap[i].grid(row=i // 16, column=i % 16)
    bitmap[i].grid(row=i // 16, column=i % 16)


def drowLabel(num):
    i = 0
    while (num > 0):
        if (num & 1):
            bitmap[i]['background'] = 'green'
        else:
            bitmap[i]['background'] = 'white'

        i += 1
        num = num >> 1
    if (num < 31):
        while (i < len(bitmap)):
            bitmap[i]['background'] = 'white'
            i += 1


# 直接输入十六进制可直接转换
def checkAndUpdate_16(event):
    global number
    content = st16.get()
    drowLabel(int(content, 16))
    if(content == ''):
        st16.set('')
        st10.set('')
        st8.set('')
        st2.set('')
        number = 0
    else:
        st10.set("%d" % int(content, 16))
        st8.set("%o" % int(content, 16))
        st2.set("%s" % bin(int(content, 16))[2:])

hex_entry.bind('<KeyRelease>', checkAndUpdate_16)


# 直接输入十进制可直接转换
def checkAndUpdate_10(event):
    global number
    content = st10.get()
    drowLabel(int(content, 10))
    if(content == ''):
        st16.set('')
        st10.set('')
        st8.set('')
        st2.set('')
        number = 0
    else:
        st16.set("%x" % int(content, 10))
        st8.set("%o" % int(content, 10))
        st2.set("%s" % bin(int(content, 10))[2:])

dec_entry.bind('<KeyRelease>', checkAndUpdate_10)

# 直接输入八进制可直接转换
def checkAndUpdate_8(event):
    global number
    content = st8.get()
    drowLabel(int(content, 8))
    if(content == ''):
        st16.set('')
        st10.set('')
        st8.set('')
        st2.set('')
        number = 0
    else:
        st16.set("%x" % int(content, 8))
        st10.set("%d" % int(content, 8))
        st2.set("%s" % bin(int(content, 8))[2:])

oct_entry.bind('<KeyRelease>', checkAndUpdate_8)

# 不支持直接输入二进制可直接转换
def checkAndUpdate_2(event):
    global number
    content = st2.get()
    if(content != ''):
        st16.set('')
        st10.set('')
        st8.set('')
        st2.set('不支持直接输入')

bin_entry.bind('<Return>', checkAndUpdate_2)


# 放置 botton

def overset():
    global number
    for i in range(32):
        bitmap[i].configure(background = 'white')
    
    st16.set('')
    st10.set('')
    st8.set('')
    st2.set('')

    number = 0


frame2 = Frame(window, relief=RAISED, borderwidth=1)
frame2.pack(side=TOP, fill=X, ipadx=0, ipady=0, expand=0)

resetButton = Button(frame2, text="重置", command=overset)
changeButton = Button(frame2, text="计算")

resetButton.pack(side=LEFT, fill=Y, ipadx=30, ipady=15)
changeButton.pack(side=LEFT, fill=Y, ipadx=30, ipady=15)



window.mainloop()             # 启动窗口