# Imports
import psutil as psutil
import time
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from plyer import notification
import smtplib, ssl
import win32gui
import win32con

from dotenv import dotenv_values

config = dotenv_values(".env")

print(config.get('PASSWORD'))