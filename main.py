import random
import sqlite3
import time

from tkinter import *

import pyttsx3


import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.geometry("1080x980")
root.title('Dyslexia Detection')
radio_var1=IntVar()
radio_var2=IntVar()
radio_var3=IntVar()
radio_var4=IntVar()
radio_var5=IntVar()
radio_var6=IntVar()
radio_var7=IntVar()
def start():
    global frame0

    frame0 = customtkinter.CTkFrame(master=root)
    frame0.pack(pady=20, padx=60, fill="both", expand=True)
    label = customtkinter.CTkLabel(master=frame0, text="Home")
    label.pack(pady=12, padx=10)

    button5 = customtkinter.CTkButton(master=frame0,
                                      text="You Must create an account",
                                      text_color="white",
                                      fg_color="transparent",
                                      hover_color="red",
                                      command=lambda :signUpPage())
    button5.pack(pady=10, padx=10)

    frame0.mainloop()
def signUpPage():
    frame0.destroy()
    time.sleep(0.5)

    fname = StringVar()
    user_name = StringVar()
    passW = StringVar()
    c = StringVar()

    global frame1
    frame1=customtkinter.CTkFrame(master=root)
    frame1.pack(pady=20, padx=60, fill="both", expand=True)
    label=customtkinter.CTkLabel(master=frame1, text="Sign Up")
    label.pack(pady=12,padx=10)

    # full name
    flabel = customtkinter.CTkLabel(frame1, text="YourName",text_color="white", fg_color='transparent')
    flabel.pack(pady=50,padx=50)
    flabel.place(relx=0.35,rely=0.08)
    entry0 = customtkinter.CTkEntry(master=frame1,textvariable=fname, placeholder_text="Name")
    entry0.pack(pady=12,padx=10)

    # username
    ulabel = customtkinter.CTkLabel(frame1, text="Username",text_color="white", fg_color='transparent')
    ulabel.pack(pady=50,padx=50)
    ulabel.place(relx=0.35,rely=0.15)
    entry1 = customtkinter.CTkEntry(master=frame1,textvariable=user_name, placeholder_text="Username")
    entry1.pack(pady=12,padx=10)

    # password
    plabel = customtkinter.CTkLabel(frame1, text=" Password",text_color="white", fg_color='transparent')
    plabel.pack(pady=50,padx=50)
    plabel.place(relx=0.35,rely=0.22)
    entry2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Password",textvariable=passW,show="*")
    entry2.pack(pady=12,padx=102)

    # country
    clabel = customtkinter.CTkLabel(frame1, text=" Country",text_color="white", fg_color='transparent',)
    clabel.pack(pady=50,padx=50)
    clabel.place(relx=0.35,rely=0.29)
    option = customtkinter.CTkOptionMenu(frame1, values=["India", "USA", "Japan", "Pakistan", "SriLanka"],
                                      dropdown_text_color="black", variable=c, fg_color="black",
                                      dropdown_fg_color="white")
    option.pack(pady=12,padx=10)
    option.set("Choose the country")

    def addUserToDataBase():

        fullname = fname.get()
        username = user_name.get()
        password = passW.get()
        country = c.get()

        if len(fname.get())==0 and len(user_name.get())==0 and len(passW.get())==0 and len(c.get()) == 0  :
            error = Label(text="You haven't enter any field...Please Enter all the fields", fg='black', bg='white')
            error.place(relx=0.41, rely=0.36)

        elif len(fname.get())==0 or len(user_name.get())==0 or len(passW.get())==0 or len(c.get()) == 0 :
            error = Label(text="Please Enter all the fields", fg='red')
            error.place(relx=0.41, rely=0.36)

        elif len(user_name.get()) == 0 and len(passW.get()) == 0:
            error = Label(text="Username and password can't be empty", fg='red')
            error.place(relx=0.41, rely=0.36)

        elif len(user_name.get()) == 0 and len(passW.get()) != 0:
            error = Label(text="Username can't be empty", fg='red')
            error.place(relx=0.41, rely=0.36)

        elif len(user_name.get()) != 0 and len(passW.get()) == 0:
            error = Label(text="Password can't be empty", fg='red')
            error.place(relx=0.41, rely=0.36)

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
    button3=customtkinter.CTkButton(master=frame1,
                                   text="Signup",
                                   text_color="white",
                                   fg_color="transparent",
                                   hover_color= "red",
                                   command=lambda :addUserToDataBase())
    button3.pack(pady=10,padx=10)
    button3.place(relx=0.408,rely=0.40)

    button3=customtkinter.CTkButton(master=frame1,
                                   text="Already have a Account?",
                                   text_color="white",
                                   fg_color="transparent",
                                   hover_color= "green",
                                   command=lambda :gotoLogin(),
                                    width=16,
                                    height=1)
    button3.pack(pady=10,padx=10)
    button3.place(relx=0.402,rely=0.45)

    frame1.mainloop()


def loginpage(logdata):
    frame1.destroy()
    time.sleep(0.5)
    global frame2

    frame2=customtkinter.CTkFrame(master=root)
    frame2.pack(pady=20, padx=60, fill="both",expand=True)

    label=customtkinter.CTkLabel(master=frame2, text="Login System")
    label.pack(pady=12,padx=10)

    user_name=StringVar()
    passW = StringVar()

    ulabel = customtkinter.CTkLabel(frame2, text="Username",text_color="white", fg_color='transparent')
    ulabel.pack(pady=50,padx=50)
    ulabel.place(relx=0.35,rely=0.08)
    entry1 = customtkinter.CTkEntry(master=frame2,textvariable=user_name, placeholder_text="Username")
    entry1.pack(pady=12,padx=10)

    plabel = customtkinter.CTkLabel(frame2, text="Password",text_color="white", fg_color='transparent')
    plabel.pack(pady=50,padx=50)
    plabel.place(relx=0.35,rely=0.14)
    entry2 = customtkinter.CTkEntry(master=frame2, placeholder_text="Password",textvariable=passW,show="*")
    entry2.pack(pady=12,padx=10)

    button2=customtkinter.CTkButton(master=frame2,
                                   text="Login",
                                   text_color="white",
                                   fg_color="transparent",
                                   hover_color= "red",
                                   command=lambda :check())
    button2.pack(pady=10,padx=10)
    button2.place(relx=0.40,rely=0.25)

    def check():
        for a, b, c, d in logdata:
            if b == user_name.get() and c == passW.get():
                print(logdata)

                tab_view()
                break
        else:
            error = Label(frame2, text="Wrong Username or Password!", fg='red')
            error.place(relx=0.37, rely=0.20)


    frame2.mainloop()



def tab_view():
    frame2.destroy()
    global frame3
    time.sleep(0.5)
    tabview = customtkinter.CTkTabview(root,height=500,width=500)
    frame3 = customtkinter.CTkFrame(master=root)
    tabview = customtkinter.CTkTabview(frame3,height=500,width=500)
    frame3.pack(pady=20, padx=60, fill="both", expand=True)
    t1=tabview.add("tab 1")  # add tab at the end
    t2=tabview.add("tab 2")
    t3=tabview.add("tab 3")  # add tab at the end
    t4=tabview.add("tab 4")
    t5=tabview.add("tab 5")  # add tab at the end
    t6=tabview.add("tab 6")
    t7=tabview.add("tab 7")

    tabview.pack(padx=20, pady=20)
    label=customtkinter.CTkLabel(t1,text="Question1")
    label.grid(row=0,column=0,padx=20,pady=20)
    label2=customtkinter.CTkLabel(t2,text="Question2")
    label2.grid(row=0,column=0,padx=20,pady=20)
    label3=customtkinter.CTkLabel(t3,text="Question3")
    label3.grid(row=0,column=0,padx=20,pady=20)
    label4=customtkinter.CTkLabel(t4,text="Question4")
    label4.grid(row=0,column=0,padx=20,pady=20)
    label5=customtkinter.CTkLabel(t5,text="Question5")
    label5.grid(row=0,column=0,padx=20,pady=20)
    label6=customtkinter.CTkLabel(t6,text="Question6")
    label6.grid(row=0,column=0,padx=20,pady=20)
    label7=customtkinter.CTkLabel(t7,text="Question7")
    label7.grid(row=0,column=0,padx=20,pady=20)
    frame1 = customtkinter.CTkFrame(master=t1, width=400, height=100)
    frame1.grid(row=1, column=0, padx=20, pady=20)
    frame32 = customtkinter.CTkFrame(master=t2, width=400, height=100)
    frame32.grid(row=1, column=0, padx=20, pady=20)
    frame33 = customtkinter.CTkFrame(master=t3, width=400, height=100)
    frame33.grid(row=1, column=0, padx=20, pady=20)
    frame4 = customtkinter.CTkFrame(master=t4, width=400, height=100)
    frame4.grid(row=1, column=0, padx=20, pady=20)
    frame5 = customtkinter.CTkFrame(master=t5, width=400, height=100)
    frame5.grid(row=1, column=0, padx=20, pady=20)
    frame6 = customtkinter.CTkFrame(master=t6, width=400, height=100)
    frame6.grid(row=1, column=0, padx=20, pady=20)
    frame7 = customtkinter.CTkFrame(master=t7, width=400, height=100)
    frame7.grid(row=1, column=0, padx=20, pady=20)
    qlabel1 = customtkinter.CTkLabel(master=frame1, text="Which of the following is not an exception handling keyword in Python?")
    qlabel1.pack(pady=12, padx=10)
    radiobutton_1 = customtkinter.CTkRadioButton(master=frame1, text="Option 1",
                                                      variable=radio_var1, value=1)
    radiobutton_2 = customtkinter.CTkRadioButton(master=frame1, text="Option 2",
                                                      variable=radio_var1, value=2)
    radiobutton_3 = customtkinter.CTkRadioButton(master=frame1, text="Option 3",
                                                      variable=radio_var1, value=3)
    radiobutton_4 = customtkinter.CTkRadioButton(master=frame1, text="Option 4",
                                                      variable=radio_var1, value=4)
    radiobutton_1.pack(padx=20, pady=10)
    radiobutton_2.pack(padx=20, pady=10)
    radiobutton_3.pack(padx=20, pady=10)
    radiobutton_4.pack(padx=20, pady=10)
    button = customtkinter.CTkButton(master=frame1, text="Submit", command=lambda: print("Option", radio_var1.get()))
    button.pack(pady=12, padx=10)
    qlabel2 = customtkinter.CTkLabel(master=frame32, text="Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?")
    qlabel2.pack(pady=12, padx=10)
    radiobutton_1 = customtkinter.CTkRadioButton(master=frame32, text="Option 1",
                                                      variable=radio_var2, value=1)
    radiobutton_2 = customtkinter.CTkRadioButton(master=frame32, text="Option 2",
                                                      variable=radio_var2, value=2)
    radiobutton_3 = customtkinter.CTkRadioButton(master=frame32, text="Option 3",
                                                      variable=radio_var2, value=3)
    radiobutton_4 = customtkinter.CTkRadioButton(master=frame32, text="Option 4",
                                                      variable=radio_var2, value=4)
    radiobutton_1.pack(padx=20, pady=10)
    radiobutton_2.pack(padx=20, pady=10)
    radiobutton_3.pack(padx=20, pady=10)
    radiobutton_4.pack(padx=20, pady=10)
    button = customtkinter.CTkButton(master=frame32, text="Submit", command=lambda: print("Option", radio_var2.get()))
    button.pack(pady=12, padx=10)
    qlabel3 = customtkinter.CTkLabel(master=frame33, text="Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?")
    qlabel3.pack(pady=12, padx=10)
    radiobutton_1 = customtkinter.CTkRadioButton(master=frame33, text="Option 1",
                                                      variable=radio_var3, value=1)
    radiobutton_2 = customtkinter.CTkRadioButton(master=frame33, text="Option 2",
                                                      variable=radio_var3, value=2)
    radiobutton_3 = customtkinter.CTkRadioButton(master=frame33, text="Option 3",
                                                      variable=radio_var3, value=3)
    radiobutton_4 = customtkinter.CTkRadioButton(master=frame33, text="Option 4",
                                                      variable=radio_var3, value=4)
    radiobutton_1.pack(padx=20, pady=10)
    radiobutton_2.pack(padx=20, pady=10)
    radiobutton_3.pack(padx=20, pady=10)
    radiobutton_4.pack(padx=20, pady=10)
    button = customtkinter.CTkButton(master=frame33, text="Submit", command=lambda: print("Option", radio_var3.get()))
    button.pack(pady=12, padx=10)
    qlabel4 = customtkinter.CTkLabel(master=frame4, text="print(0xA + 0xB + 0xC):?")
    qlabel4.pack(pady=12, padx=10)
    radiobutton_1 = customtkinter.CTkRadioButton(master=frame4, text="Option 1",
                                                      variable=radio_var4, value=1)
    radiobutton_2 = customtkinter.CTkRadioButton(master=frame4, text="Option 2",
                                                      variable=radio_var4, value=2)
    radiobutton_3 = customtkinter.CTkRadioButton(master=frame4, text="Option 3",
                                                      variable=radio_var4, value=3)
    radiobutton_4 = customtkinter.CTkRadioButton(master=frame4, text="Option 4",
                                                      variable=radio_var4, value=4)
    radiobutton_1.pack(padx=20, pady=10)
    radiobutton_2.pack(padx=20, pady=10)
    radiobutton_3.pack(padx=20, pady=10)
    radiobutton_4.pack(padx=20, pady=10)
    button = customtkinter.CTkButton(master=frame4, text="Submit", command=lambda: print("Option", radio_var4.get()))
    button.pack(pady=12, padx=10)
    qlabel5 = customtkinter.CTkLabel(master=frame5, text="Which of the following is invalid?")
    qlabel5.pack(pady=12, padx=10)
    radiobutton_1 = customtkinter.CTkRadioButton(master=frame5, text="Option 1",
                                                      variable=radio_var5, value=1)
    radiobutton_2 = customtkinter.CTkRadioButton(master=frame5, text="Option 2",
                                                      variable=radio_var5, value=2)
    radiobutton_3 = customtkinter.CTkRadioButton(master=frame5, text="Option 3",
                                                      variable=radio_var5, value=3)
    radiobutton_4 = customtkinter.CTkRadioButton(master=frame5, text="Option 4",
                                                      variable=radio_var5, value=4)
    radiobutton_1.pack(padx=20, pady=10)
    radiobutton_2.pack(padx=20, pady=10)
    radiobutton_3.pack(padx=20, pady=10)
    radiobutton_4.pack(padx=20, pady=10)
    button = customtkinter.CTkButton(master=frame5, text="Submit", command=lambda: print("Option", radio_var5.get()))
    button.pack(pady=12, padx=10)
    qlabel6 = customtkinter.CTkLabel(master=frame6, text="What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10")
    qlabel6.pack(pady=12, padx=10)
    radiobutton_1 = customtkinter.CTkRadioButton(master=frame6, text="Option 1",
                                                      variable=radio_var6, value=1)
    radiobutton_2 = customtkinter.CTkRadioButton(master=frame6, text="Option 2",
                                                      variable=radio_var6, value=2)
    radiobutton_3 = customtkinter.CTkRadioButton(master=frame6, text="Option 3",
                                                      variable=radio_var6, value=3)
    radiobutton_4 = customtkinter.CTkRadioButton(master=frame6, text="Option 4",
                                                      variable=radio_var6, value=4)
    radiobutton_1.pack(padx=20, pady=10)
    radiobutton_2.pack(padx=20, pady=10)
    radiobutton_3.pack(padx=20, pady=10)
    radiobutton_4.pack(padx=20, pady=10)
    button = customtkinter.CTkButton(master=frame6, text="Submit", command=print("Option", radio_var6.get))
    button.pack(pady=12, padx=10)
    qlabel7 = customtkinter.CTkLabel(master=frame7, text="What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)")
    qlabel7.pack(pady=12, padx=10)
    radiobutton_1 = customtkinter.CTkRadioButton(master=frame7, text="Option 1",
                                                      variable=radio_var7, value=1)
    radiobutton_2 = customtkinter.CTkRadioButton(master=frame7, text="Option 2",
                                                      variable=radio_var7, value=2)
    radiobutton_3 = customtkinter.CTkRadioButton(master=frame7, text="Option 3",
                                                      variable=radio_var7, value=3)
    radiobutton_4 = customtkinter.CTkRadioButton(master=frame7, text="Option 4",
                                                      variable=radio_var7, value=4)
    radiobutton_1.pack(padx=20, pady=10)
    radiobutton_2.pack(padx=20, pady=10)
    radiobutton_3.pack(padx=20, pady=10)
    radiobutton_4.pack(padx=20, pady=10)
    button = customtkinter.CTkButton(master=frame7, text="Submit", command=lambda:print("Option", radio_var7.get()),)
    button.pack(pady=12, padx=10)
    b=customtkinter.CTkButton(frame3,text="End",fg_color="red",command=lambda :Speech())
    b.pack()

def Speech():
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    print(rate)
    rate = engine.setProperty('rate', 150)
    volume = engine.getProperty('volume')
    print(volume)
    volume = engine.setProperty('volume', 5.0)

    engine.say('hey sathya')
    engine.say("poda punda mavana")
    engine.runAndWait()
    engine.stop()

    engine.runAndWait()


if __name__ == '__main__':
    start()
