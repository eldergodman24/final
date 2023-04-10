import random
import sqlite3
import time

import tkinter
import tkinter as tk
from tkinter import *
from tkinter import Tk,ttk
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.geometry("1080x1200")
root.title('Dyslexia Detection')



def loginpage(logdata):
    frame2.destroy()
    time.sleep(0.5)
    global frame

    frame=customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both",expand=True)

    label=customtkinter.CTkLabel(master=frame, text="Login System")
    label.pack(pady=12,padx=10)

    user_name=StringVar()
    passW = StringVar()

    ulabel = customtkinter.CTkLabel(frame, text="Username",text_color="white", fg_color='transparent')
    ulabel.pack(pady=50,padx=50)
    ulabel.place(relx=0.35,rely=0.08)
    entry1 = customtkinter.CTkEntry(master=frame,textvariable=user_name, placeholder_text="Username")
    entry1.pack(pady=12,padx=10)

    plabel = customtkinter.CTkLabel(frame, text="Password",text_color="white", fg_color='transparent')
    plabel.pack(pady=50,padx=50)
    plabel.place(relx=0.35,rely=0.14)
    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password",textvariable=passW,show="*")
    entry2.pack(pady=12,padx=10)

    # button=customtkinter.CTkButton(master=frame, text="Login",command=check)
    # button.pack(pady=12,padx=10)
    #
    button2=customtkinter.CTkButton(master=frame,
                                   text="Login",
                                   text_color="white",
                                   fg_color="transparent",
                                   hover_color= "red",
                                   command=lambda :check())
    button2.pack(pady=10,padx=10)

    def check():
        for a, b, c, d in logdata:
            if b == user_name.get() and c == passW.get():
                print(logdata)

                menu(a)
                break
        else:
            error = Label(frame, text="Wrong Username or Password!", fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)
    #
    # # LOGIN BUTTON
    # log = Button(login_frame, text='Login', padx=5, pady=5, width=5, command=check, fg="white", bg="black")
    # log.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    # log.place(relx=0.4, rely=0.6)

    frame.mainloop()


def signUpPage():
    frame0.destroy()
    time.sleep(0.5)
    global frame2
    fname = StringVar()
    user_name = StringVar()
    passW = StringVar()
    c = StringVar()
    frame2=customtkinter.CTkFrame(master=root)
    frame2.pack(pady=20, padx=60, fill="both", expand=True)
    label=customtkinter.CTkLabel(master=frame2, text="Sign Up")
    label.pack(pady=12,padx=10)

    # full name
    flabel = customtkinter.CTkLabel(frame2, text="YourName",text_color="white", fg_color='transparent')
    flabel.pack(pady=50,padx=50)
    flabel.place(relx=0.35,rely=0.08)
    entry0 = customtkinter.CTkEntry(master=frame2,textvariable=fname, placeholder_text="Name")
    entry0.pack(pady=12,padx=10)

    # username
    ulabel = customtkinter.CTkLabel(frame2, text="Username",text_color="white", fg_color='transparent')
    ulabel.pack(pady=50,padx=50)
    ulabel.place(relx=0.35,rely=0.15)
    entry1 = customtkinter.CTkEntry(master=frame2,textvariable=user_name, placeholder_text="Username")
    entry1.pack(pady=12,padx=10)

    # password
    plabel = customtkinter.CTkLabel(frame2, text=" Password",text_color="white", fg_color='transparent')
    plabel.pack(pady=50,padx=50)
    plabel.place(relx=0.35,rely=0.22)
    entry2 = customtkinter.CTkEntry(master=frame2, placeholder_text="Password",textvariable=passW,show="*")
    entry2.pack(pady=12,padx=102)

    # country
    clabel = customtkinter.CTkLabel(frame2, text=" Country",text_color="white", fg_color='transparent',)
    clabel.pack(pady=50,padx=10)
    clabel.place(relx=0.35,rely=0.29)
    # option = customtkinter.CTkOptionMenu(frame2, values=["India", "USA", "Japan", "Pakistan", "SriLanka", "India", "USA",
    #                                                     "Japan", "Pakistan", "SriLanka", "India", "USA", "Japan",
    #                                                     "Pakistan", "SriLanka", "India", "USA", "Japan", "Pakistan",
    #                                                     "SriLanka", "India", "USA", "Japan", "Pakistan", "SriLanka"],
    #                                      dropdown_text_color="black", fg_color="black",dropdown_fg_color="white")
    #
    # option.pack(pady=12, padx=10)
    # option.set("Choose any one")

    def addUserToDataBase():

        fullname = fname.get()
        username = user_name.get()
        password = passW.get()
        country = c.get()

        if len(fname.get()) == 0 and len(user_name.get()) == 0 and len(passW.get()) == 0  :
            error = Label(text="You haven't enter any field...Please Enter all the fields", fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(fname.get()) == 0 or len(user_name.get()) == 0 or len(passW.get()) == 0 :
            error = Label(text="Please Enter all the fields", fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(user_name.get()) == 0 and len(passW.get()) == 0:
            error = Label(text="Username and password can't be empty", fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(user_name.get()) == 0 and len(passW.get()) != 0:
            error = Label(text="Username can't be empty", fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(user_name.get()) != 0 and len(passW.get()) == 0:
            error = Label(text="Password can't be empty", fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        else:

            conn = sqlite3.connect('quiz.db')
            create = conn.cursor()
            create.execute(
                'CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
            create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)", (fullname, username, password, country))
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z = create.fetchall()
            print(z)
            # L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            conn.close()
            loginpage(z)

    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z = create.fetchall()
        loginpage(z)

    # signup BUTTON
    button3=customtkinter.CTkButton(master=frame2,
                                   text="Signup",
                                   text_color="white",
                                   fg_color="transparent",
                                   hover_color= "red",
                                   command=lambda :addUserToDataBase())
    button3.pack(pady=10,padx=10)
    # sp = Button(sup_frame, text='SignUp', padx=5, pady=5, width=5, command=addUserToDataBase, bg="black", fg="white")
    # sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    # sp.place(relx=0.4, rely=0.8)

    log = Button(frame2, text='Already have a Account?', padx=5, pady=5, width=5, command=gotoLogin, bg="#BADA55",
                 fg="black")
    log.configure(width=16, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.393, rely=0.9)

    frame2.mainloop()


def menu(abcdefgh):
    frame.destroy()
    global menu
    menu = Tk()
    menu.title('Quiz App Menu')

    menu_canvas = Canvas(menu, width=720, height=440, bg="orange")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas, bg="#7FFFD4")
    menu_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    wel = Label(menu_canvas, text=' W E L C O M E  T O  Q U I Z  S T A T I O N ', fg="white", bg="orange")
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1, rely=0.02)

    abcdefgh = 'Welcome ' + abcdefgh
    level34 = Label(menu_frame, text=abcdefgh, bg="black", font="calibri 18", fg="white")
    level34.place(relx=0.17, rely=0.15)

    level = Label(menu_frame, text='Select your Difficulty Level !!', bg="orange", font="calibri 18")
    level.place(relx=0.25, rely=0.3)

    var = IntVar()
    easyr = Radiobutton(menu_frame, text='CHILD', bg="#7FFFD4", font="calibri 16", value=1, variable=var)
    easyr.place(relx=0.25, rely=0.4)

    mediumr = Radiobutton(menu_frame, text='Medium', bg="#7FFFD4", font="calibri 16", value=2, variable=var)
    mediumr.place(relx=0.25, rely=0.5)

    hardr = Radiobutton(menu_frame, text='Hard', bg="#7FFFD4", font="calibri 16", value=3, variable=var)
    hardr.place(relx=0.25, rely=0.6)

    def navigate():

        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            medium()

        elif x == 3:
            menu.destroy()
            difficult()
        else:
            pass

    letsgo = Button(menu_frame, text="Let's Go", bg="black", fg="white", font="calibri 12", command=navigate)
    letsgo.place(relx=0.25, rely=0.8)
    menu.mainloop()


def easy():
    global e
    e = Tk()
    e.title('Quiz App - Easy Level')

    easy_canvas = Canvas(e, width=720, height=440, bg="orange")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas, bg="#BADA55")
    easy_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    def countDown():
        check = 0
        for k in range(10, 0, -1):

            if k == 1:
                check = -1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)

        timer.configure(text="Times up!")
        if check == -1:
            return (-1)
        else:
            return 0

    global score
    score = 0

    easyQ = [
        [
            "What will be the output of the following Python code? \nl=[1, 0, 2, 0, 'hello', '', []] \nlist(filter("
            "bool, nl))",
            "[1, 0, 2, ‘hello’, '', []]",
            "Error",
            "[1, 2, ‘hello’]",
            "[1, 0, 2, 0, ‘hello’, '', []]"
        ],
        [
            "What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)",
            "34.00",
            "34.000000",
            "34.0000",
            "34.00000000"

        ],
        [
            "What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10",
            "30.8",
            "27.2",
            "28.4",
            "30.0"
        ],
        [
            "Which of these in not a core data type?",
            "Tuples",
            "Dictionary",
            "Lists",
            "Class"
        ],
        [
            "Which of the following represents the bitwise XOR operator?",
            "&",
            "!",
            "^",
            "|"
        ]
    ]
    answer = [
        "[1, 2, ‘hello’]",
        "34.000000",
        "27.2",
        "Class",
        "^"
    ]
    li = ['', 0, 1, 2, 3, 4]
    x = random.choice(li[1:])

    ques = Label(easy_frame, text=easyQ[x][0], font="calibri 12", bg="orange")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    a = Radiobutton(easy_frame, text=easyQ[x][1], font="calibri 10", value=easyQ[x][1], variable=var, bg="#BADA55")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(easy_frame, text=easyQ[x][2], font="calibri 10", value=easyQ[x][2], variable=var, bg="#BADA55")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(easy_frame, text=easyQ[x][3], font="calibri 10", value=easyQ[x][3], variable=var, bg="#BADA55")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(easy_frame, text=easyQ[x][4], font="calibri 10", value=easyQ[x][4], variable=var, bg="#BADA55")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)

    li.remove(x)

    timer = Label(e)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    def display():

        if len(li) == 1:
            e.destroy()
            showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End', command=calc)

        if li:
            x = random.choice(li[1:])
            ques.configure(text=easyQ[x][0])

            a.configure(text=easyQ[x][1], value=easyQ[x][1])

            b.configure(text=easyQ[x][2], value=easyQ[x][2])

            c.configure(text=easyQ[x][3], value=easyQ[x][3])

            d.configure(text=easyQ[x][4], value=easyQ[x][4])

            li.remove(x)
            y = countDown()
            if y == -1:
                display()

    def calc():
        global score
        if (var.get() in answer):
            score += 1
        display()

    submit = Button(easy_frame, command=calc, text="Submit", fg="white", bg="black")
    submit.place(relx=0.5, rely=0.82, anchor=CENTER)

    nextQuestion = Button(easy_frame, command=display, text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87, rely=0.82, anchor=CENTER)

    # pre=Button(easy_frame,command=display, text="Previous", fg="white", bg="black")
    # pre.place(relx=0.75, rely=0.82, anchor=CENTER)

    y = countDown()
    if y == -1:
        display()
    e.mainloop()


def medium():
    global m
    m = Tk()
    m.title('Quiz App - Medium Level')

    med_canvas = Canvas(m, width=720, height=440, bg="#101357")
    med_canvas.pack()

    med_frame = Frame(med_canvas, bg="#A1A100")
    med_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    def countDown():
        check = 0
        for k in range(10, 0, -1):

            if k == 1:
                check = -1
            timer.configure(text=k)
            med_frame.update()
            time.sleep(1)

        timer.configure(text="Times up!")
        if check == -1:
            return (-1)
        else:
            return 0

    global score
    score = 0

    mediumQ = [
        [
            "Which of the following is not an exception handling keyword in Python?",
            "accept",
            "finally",
            "except",
            "try"
        ],
        [
            "Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?",
            "3",
            "5",
            "25",
            "1"
        ],
        [
            "Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?",
            "Error",
            "None",
            "25",
            "2"
        ],
        [
            "print(0xA + 0xB + 0xC):",
            "0xA0xB0xC",
            "Error",
            "0x22",
            "33"
        ],
        [
            "Which of the following is invalid?",
            "_a = 1",
            "__a = 1",
            "__str__ = 1",
            "none of the mentioned"
        ],
    ]
    answer = [
        "accept",
        "1",
        "25",
        "33",
        "none of the mentioned"
    ]

    li = ['', 0, 1, 2, 3, 4]
    x = random.choice(li[1:])

    ques = Label(med_frame, text=mediumQ[x][0], font="calibri 12", bg="#B26500")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    a = Radiobutton(med_frame, text=mediumQ[x][1], font="calibri 10", value=mediumQ[x][1], variable=var, bg="#A1A100")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(med_frame, text=mediumQ[x][2], font="calibri 10", value=mediumQ[x][2], variable=var, bg="#A1A100")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(med_frame, text=mediumQ[x][3], font="calibri 10", value=mediumQ[x][3], variable=var, bg="#A1A100")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(med_frame, text=mediumQ[x][4], font="calibri 10", value=mediumQ[x][4], variable=var, bg="#A1A100")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)

    li.remove(x)

    timer = Label(m)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    def display():

        if len(li) == 1:
            m.destroy()
            showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End', command=calc)

        if li:
            x = random.choice(li[1:])
            ques.configure(text=mediumQ[x][0])

            a.configure(text=mediumQ[x][1], value=mediumQ[x][1])

            b.configure(text=mediumQ[x][2], value=mediumQ[x][2])

            c.configure(text=mediumQ[x][3], value=mediumQ[x][3])

            d.configure(text=mediumQ[x][4], value=mediumQ[x][4])

            li.remove(x)
            y = countDown()
            if y == -1:
                display()

    def calc():
        global score
        if (var.get() in answer):
            score += 1
        display()

    submit = Button(med_frame, command=calc, text="Submit", fg="white", bg="black")
    submit.place(relx=0.5, rely=0.82, anchor=CENTER)

    nextQuestion = Button(med_frame, command=display, text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87, rely=0.82, anchor=CENTER)

    # pre=Button(med_frame,command=display, text="Previous", fg="white", bg="black")
    # pre.place(relx=0.75, rely=0.82, anchor=CENTER)

    y = countDown()
    if y == -1:
        display()
    m.mainloop()


def difficult():
    global h
    # count=0
    h = Tk()
    h.title('Quiz App - Hard Level')

    hard_canvas = Canvas(h, width=720, height=440, bg="#101357")
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas, bg="#008080")
    hard_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    def countDown():
        check = 0
        for k in range(10, 0, -1):

            if k == 1:
                check = -1
            timer.configure(text=k)
            hard_frame.update()
            time.sleep(1)

        timer.configure(text="Times up!")
        if check == -1:
            return (-1)
        else:
            return 0

    global score
    score = 0

    hardQ = [
        [
            "All keywords in Python are in _________",
            "lower case",
            "UPPER CASE",
            "Capitalized",
            "None of the mentioned"
        ],
        [
            "Which of the following cannot be a variable?",
            "__init__",
            "in",
            "it",
            "on"
        ],
        [
            "Which of the following is a Python tuple?",
            "[1, 2, 3]",
            "(1, 2, 3)",
            "{1, 2, 3}",
            "{}"
        ],
        [
            "What is returned by math.ceil(3.4)?",
            "3",
            "4",
            "4.0",
            "3.0"
        ],
        [
            "What will be the output of print(math.factorial(4.5))?",
            "24",
            "120",
            "error",
            "24.0"
        ]

    ]
    answer = [
        "None of the mentioned",
        "in",
        "(1,2,3)",
        "4",
        "error"
    ]

    li = ['', 0, 1, 2, 3, 4]
    x = random.choice(li[1:])

    ques = Label(hard_frame, text=hardQ[x][0], font="calibri 12", bg="#A0DB8E")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    a = Radiobutton(hard_frame, text=hardQ[x][1], font="calibri 10", value=hardQ[x][1], variable=var, bg="#008080",
                    fg="white")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(hard_frame, text=hardQ[x][2], font="calibri 10", value=hardQ[x][2], variable=var, bg="#008080",
                    fg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(hard_frame, text=hardQ[x][3], font="calibri 10", value=hardQ[x][3], variable=var, bg="#008080",
                    fg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(hard_frame, text=hardQ[x][4], font="calibri 10", value=hardQ[x][4], variable=var, bg="#008080",
                    fg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)

    li.remove(x)

    timer = Label(h)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    def display():

        if len(li) == 1:
            h.destroy()
            showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End', command=calc)

        if li:
            x = random.choice(li[1:])
            ques.configure(text=hardQ[x][0])

            a.configure(text=hardQ[x][1], value=hardQ[x][1])

            b.configure(text=hardQ[x][2], value=hardQ[x][2])

            c.configure(text=hardQ[x][3], value=hardQ[x][3])

            d.configure(text=hardQ[x][4], value=hardQ[x][4])

            li.remove(x)
            y = countDown()
            if y == -1:
                display()

    def calc():
        global score
        # count=count+1
        if (var.get() in answer):
            score += 1
        display()

    # def lastPage():
    #    h.destroy()
    #   showMark()

    submit = Button(hard_frame, command=calc, text="Submit", fg="white", bg="black")
    submit.place(relx=0.5, rely=0.82, anchor=CENTER)

    nextQuestion = Button(hard_frame, command=display, text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87, rely=0.82, anchor=CENTER)

    # pre=Button(hard_frame,command=display, text="Previous", fg="white", bg="black")
    # pre.place(relx=0.75, rely=0.82, anchor=CENTER)

    # end=Button(hard_frame,command=showMark(m), text="End", fg="white", bg="black")
    # end.place(relx=0.8, rely=0.82, anchor=CENTER)

    y = countDown()
    if y == -1:
        display()
    h.mainloop()


def showMark(mark):
    sh = Tk()
    sh.title('Your Marks')

    st = "Your score is " + str(mark) + "/5"
    mlabel = Label(sh, text=st, fg="black", bg="white")
    mlabel.pack()

    def callsignUpPage():
        sh.destroy()
        start()

    def myeasy():
        sh.destroy()
        easy()

    b24 = Button(text="Re-attempt", command=myeasy, bg="black", fg="white")
    b24.pack()

    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
    from matplotlib.figure import Figure

    fig = Figure(figsize=(5, 4), dpi=100)
    labels = 'Marks Obtained', 'Total Marks'
    sizes = [int(mark), 5 - int(mark)]
    explode = (0.1, 0)
    fig.add_subplot(111).pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=0)

    canvas = FigureCanvasTkAgg(fig, master=sh)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    b23 = Button(text="Sign Out", command=callsignUpPage, fg="white", bg="black")
    b23.pack()

    sh.mainloop()


def start():
    global frame0
    # root = Tk()
    # root.title('Welcome To Quiz App')
    # canvas = Canvas(root, width=720, height=440, bg='pink')
    # canvas.grid(column=0, row=1)
    frame0 = customtkinter.CTkFrame(master=root)
    frame0.pack(pady=20, padx=60, fill="both", expand=True)
    label = customtkinter.CTkLabel(master=frame0, text="Home")
    label.pack(pady=12, padx=10)

    button5 = customtkinter.CTkButton(master=frame0,
                                      text="You Must create an account",
                                      text_color="white",
                                      fg_color="transparent",
                                      hover_color="red",
                                      command=lambda: signUpPage())
    button5.pack(pady=10, padx=10)

    frame0.mainloop()


if __name__ == '__main__':
    start()
