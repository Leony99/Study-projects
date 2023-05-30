import re
from tkinter import END
from win32api import GetMonitorInfo, MonitorFromPoint

def window_size_center(window, width, height):
    monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
    work_area = monitor_info.get("Work")

    x = (work_area[2]/2) - (width/2)
    y = (work_area[3]/2) - (height/2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

def clearEmailEntry(emailEntry):
    def email_enter(event):
        if emailEntry.get()=='Email':
            emailEntry.delete(0, END)

    emailEntry.bind('<FocusIn>', email_enter)

def clearPasswordEntry(passwordEntry):
    def password_enter(event):
        if passwordEntry.get()=='Password':
            passwordEntry.delete(0, END)
        if passwordEntry.get()=='Confirm password':
            passwordEntry.delete(0, END)
        passwordEntry.config(show='*')

    passwordEntry.bind('<FocusIn>', password_enter)

def clearNameEntry(orNameEntry):
    def name_enter(event):
        if orNameEntry.get()=='Name':
            orNameEntry.delete(0, END)

    orNameEntry.bind('<FocusIn>', name_enter)

def clearCountryEntry(orCountryEntry):
    def country_enter(event):
        if orCountryEntry.get()=='Country':
            orCountryEntry.delete(0, END)

    orCountryEntry.bind('<FocusIn>', country_enter)

def checkEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if(re.fullmatch(regex, email)):
        return "valid"
    else:
        return "invalid"