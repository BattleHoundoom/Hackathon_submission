# Requirements

## Specs
Windows 10,
 python 3,
 Google Chrome,
 Notifications enabled,
 python IDE (not compulsory as executable file is available!)

## Installation Process
1) Download the repository as a zip file.
2) Unzip the file an 2 folders should be present (application and website)
3) the website folder contains the source code for our website.
4) Open the application folder, in it you will see 3 things - an image folder, and 2 files.
5) the first file, main.py, contains the source code, it can be opened and the program can be run from there.
6) alternatively, for convenience, you can run the main.pyw file and the code automatically runs as it is an executable. (for multiple use of program)

## Libraries

psutil - (pip install psutil)

tkinter - (import tkinter as tk,
           from tkinter import ttk,
           from tkinter import * ) 
           
plyer - (pip install plyer)

mysql - (pip install mysql-connector-python)

smtplib - (pip install smtplib)

ssl - (pip install ssl)

win32gui - (pip install win32gui)

win32con - (pip install win32con)

webbrowser - (pip install webbrowser)

## Operation (How to use)

1) After the code is run, the Fitness Check UI window will appear.
2) Here a check box, a progress bar and an email box are present.
3) To start of, enter a valid email in and click the submit button.
4) If the email isnt registered or is a fake email, it will bounce back.
5) To register your email, click on the respective button at the bottom left of the UI window.
6) This will take you to the website which is still in development. here you can go to the register page and register your email, make sure to remember your password.
7) Once registered it is saved to a database, you can then login whenever on the login page, in order to check your profile. Here your strikes will be counted. These are the warnings you receive when you dont obey the screen time.
8) After the email is registered, you must rerun the program in order to submit the email you just registered into the UI window.
9) After which you can click on the enable check box button to start running the fitness check code.
10) The code will wait until you active use Google Chrome next, when this happens it will start its fitness counter. 
11) Every 5 seconds it will send you a notification, and after every 5 notifications it will send you an email to your registered account.
12) these timings are just temporary ofcourse and only for the demo of this product, the actual times will be as follows: first notification - after 20 mins of google chrome use. rest of the notifications: after 5 mins of eachother until user quits or minimizes chrome.
