import random
from tkinter import Tk, Label, Entry, Button, Text, Label, END
from PIL import ImageTk, Image

total = 10
correct = 0
nums = range(1, 11)


def calc(a, ops, b):
    if ops == "+":
        return a+b
    elif ops == "-":
        return a-b
    elif ops == "*":
        return a*b
    elif ops == "/":
        return a//b   # integer division
    else:
        raise ValueError("Unsupported math operation")


def createImage(flag=0):
    global math_random
    global image_label
    global image_display
    global entry
    global verify_label
    global answer
    ops = random.choice("+-*/")
    a, b = random.choices(nums, k=2)
    answer = calc(a, ops, b)
    math_random = str(a)+str(ops)+str(b)
    if flag == 1:
        verify_label.grid_forget()
    entry.delete(0, END)

    l = Label(root, text=math_random)
    l.config(font=("Courier", 14))
    l.grid(row=1, column=0, columnspan=2, pady=0)


def check(x, y):
    global verify_label
    verify_label.grid_forget()
    if x == y:
        verify_label = Label(master=root,
                             text="Verified",
                             font="Arial 15",
                             bg='#ffe75c',
                             fg="#00a806"
                             )
        verify_label.grid(row=0, column=0, columnspan=2, pady=10)
    else:
        verify_label = Label(master=root,
                             text="Incorrect!",
                             font="Arial 15",
                             bg='#ffe75c',
                             fg="#fa0800"
                             )
        verify_label.grid(row=0, column=0, columnspan=2, pady=10)
        createImage()


if __name__ == "__main__":
    root = Tk()
    root.title('Image Captcha')
    root.configure(background='#fff')
    verify_label = Label(root)
    image_label = Label(root)
    entry = Entry(root, width=10, borderwidth=5,
                  font="Arial 15", justify="center")
    entry.grid(row=2, column=0)
    createImage()
    path = './refresh.png'
    reload_img = ImageTk.PhotoImage(Image.open(
        path).resize((32, 32), Image.ANTIALIAS))
    reload_button = Button(image=reload_img, command=lambda: createImage(1))
    reload_button.grid(row=2, column=1, pady=10)
    submit_button = Button(root, text="Submit", font="Arial 10",
                           command=lambda: check(int(entry.get()), answer))
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)
    root.bind('<Return>', func=lambda Event: check(int(entry.get()), answer))
    root.mainloop()
