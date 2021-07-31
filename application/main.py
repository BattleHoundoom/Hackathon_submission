# Imports
import psutil as psutil
import time
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter import font
from plyer import notification
from email.message import EmailMessage
import mysql.connector as ms
import smtplib, ssl
import win32gui
import win32con

# Variables and Configuration
port = 465
smtp_server = "smtp.gmail.com"
sender_email = "syntaxerrorfound404@gmail.com"
password = "Syntax@404"
on = False
times = 0
notif_counter = 0
second = 0
email_user = ""

# Database Connection
db = ms.connect(
    host = "sql6.freemysqlhosting.net",
    user = "sql6428478",
    passwd = "Tk3jBdaXtt",
    database = "sql6428478"
)

# Functions
def notifymee(vtitle, vmessage):
    notification.notify(
        title = vtitle,
        message = vmessage,
        app_icon = r"img/donsit.ico",
        timeout = 1
    )
    
def getCheckboxValue():
    checkedOrNot = on.get()
    return checkedOrNot

def submit_email():
    global email_user
    email_user = getInputBoxValue()
    if "@" in email_user:
        if "." in email_user:
            cursor = db.cursor()
            query = f"SELECT * FROM users WHERE email = '{email_user}'"
            cursor.execute(query)
            data = cursor.fetchone()
            if data:
                show_widget(label_good)
                hide_widget(label_bad)
                hide_widget(label_not_registered)
            else:
                show_widget(label_not_registered)
                hide_widget(label_good)
                hide_widget(label_bad)
                    
        else:
            show_widget(label_bad)
            hide_widget(label_good)  
            hide_widget(label_not_registered)
    else:
        show_widget(label_bad)
        hide_widget(label_good)
        hide_widget(label_not_registered)

def hide_widget(widget):
    widget.place_forget()

def callback():
    webbrowser.open_new("https://succulent-fourth-atrociraptor.glitch.me/")    

def show_widget(widget):
    widget.place(x=300, y=380)

def makeProgress():
    progessBarOne['value']=progessBarOne['value'] + 1
    root.update_idletasks()
    
def resetProgress():
    progessBarOne['value']=0
    root.update_idletasks()

def getInputBoxValue():
    userInput = email_input.get()
    return userInput

def hello():
    global on
    if on == True:
        on = False

    else:
        on = True
        global second
        if on == True:
            root.after(100, when_loop)

def when_loop():
    global second, times
    if on == True:
        if "chrome.exe" in (p.name() for p in psutil.process_iter()):
            tempWindowName=win32gui.GetWindowText (win32gui.GetForegroundWindow())
            window = win32gui.FindWindow(None, tempWindowName) 
            full_text = ""
            substring = "Google Chrome"
            if substring in tempWindowName:
                if window:
                    tup = win32gui.GetWindowPlacement(window)
                    if tup[1] == win32con.SW_SHOWMAXIMIZED:
                        minimized = False
                        second+=1
                        makeProgress()
                    elif tup[1] == win32con.SW_SHOWMINIMIZED:
                        minimized = True
                        
                    elif tup[1] == win32con.SW_SHOWNORMAL:
                        normal = True     
            else:
                print("window is not chrome")
                pass
            time.sleep(1)
            if (second % 5 == 0):
                if second != 0:
                    cursor = db.cursor()
                    times += 1
                    resetProgress()
                    query =f"UPDATE sql6428478.users set strikes = strikes + 1 where email='{email_user}'"
                    cursor.execute(query)
                    db.commit()
                    if ((times % 5) == 0):
                        print("sending email")
                        receiver_email = email_user
                        message = """\
Subject: Warning - Excessive Usage

Dear user,

We noticed that you have been excessively utilising your device. We believe that excessively using devices have many defects. Hence, do not use it!

Thanks & Regards,
The Syntax Error Found 404 Team"""
                        
                        context = ssl.create_default_context()
                        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                            server.login(sender_email, password)
                            server.sendmail(sender_email, receiver_email, message)
                

                        times += 1
                    notifymee("Get up!!!", "Its time to stretch and do some Exercise!!!")
                    print("Notification sent!")

            root.after(100, when_loop)

# Layout - Tkinter
root = Tk()
on = tk.IntVar()

root.geometry('573x457')
root.configure(background='#CFCFCF')
root.title('Fitness Check')

CheckBoxOne=Checkbutton(root, text='Enable', bg='#CFCFCF', font=('courier', 18, 'normal'), command=hello)
CheckBoxOne.place(x=215, y=41)

Label(root, text='Progress Bar:', bg='#CFCFCF', font=('courier', 18, 'normal')).place(x=191, y=115)

progessBarOne_style = ttk.Style()
progessBarOne_style.theme_use('clam')
progessBarOne_style.configure('progessBarOne.Horizontal.TProgressbar', foreground='#EE0000', background='#EE0000')

progessBarOne=ttk.Progressbar(root, style='progessBarOne.Horizontal.TProgressbar', orient='horizontal', length=409, mode='determinate', maximum=5, value=0)
progessBarOne.place(x=86, y=177)

email_input=Entry(root, textvariable=email_user, font=('courier', 13, 'normal'))
email_input.place(x=190, y=322, height=25, width=300)

Label(root, text='Add Email: ', bg='#CFCFCF', font=('courier', 15, 'normal')).place(x=60, y=321)

Button(root, text='Submit', bg='#FFFFFF', font=('courier', 15, 'normal'), command=submit_email).place(x=200, y=375)

label_good = Label(root, text="Successfully Saved Email!", bg="#CFCFCF", fg="#025B00", font=('courier', 10, 'normal'))
label_good.place(x=300, y=380)

hide_widget(label_good)

label_bad = Label(root, text="Invalid Email Address!", bg="#CFCFCF", fg="#FF0000", font=('courier', 10, 'normal'))
label_bad.place(x=300, y=380)

hide_widget(label_bad)

label_not_registered = Label(root, text="Please Register your email on our website!", bg="#CFCFCF", fg="#FF0000", font=('courier', 10, 'normal'))
label_not_registered.place(x=300, y=380)

hide_widget(label_not_registered)

label_register_texts = Label(root, text='To register your email click', bg='#CFCFCF', font=('courier', 10, 'normal')).place(x=281, y=430)


link_button = Button(text="here", command=callback, fg="blue", width=5).place(x=515, y=428)

root.mainloop()