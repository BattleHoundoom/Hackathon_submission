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
