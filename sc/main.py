# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 23:34:41 2023

@author: Arribaat
"""

import sign_up as su
import app as ap
import data as dt
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

custom_font = ("Courier New", 15, "bold")
default_pack = {"side": tk.TOP, "fill": tk.BOTH, "expand": True, "padx": 10, "pady": 2}
usr_data = [{}]
username = str()

class WALLABI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wallabi")
        self.initialize_ui()

    def initialize_ui(self):
        self.geometry("500x300")
        self.label = tk.Label(self, text="WALLABI\nKonsultan Keuangan Digital", font=custom_font)
        self.label.place(anchor=tk.N,x=250,y=80)

        self.button = tk.Button(self, text="START", command=self.main_m, font=custom_font,width=10)
        self.button.place(anchor=tk.S,x=250,y=250)
        return

    def main_m(self):
        self.withdraw()

        self.menu = tk.Toplevel()
        self.menu.geometry("500x300")
        self.menu.title("User Menu")

        self.greeting = tk.Label(self.menu, text="Selamat Datang", font=custom_font,width=80)
        self.greeting.place(anchor=tk.N,x=250,y=80)

        self.login_button = tk.Button(self.menu, text="Log In", command=lambda: self.login(), font=custom_font,width=10)
        self.login_button.place(anchor=tk.S,x=250,y=220)

        self.reg = tk.Button(self.menu, text="Register", command=lambda: self.regist(), font=custom_font,width=10)
        self.reg.place(anchor=tk.S,x=250,y=280)
        return

    def login(self):
        self.menu.withdraw()

        self.login_window = tk.Toplevel()
        self.login_window.geometry("500x300")
        self.login_window.title("Log In")

        self.login_usrtext = tk.Label(self.login_window, text="Username", font=custom_font)
        self.login_usrtext.pack(default_pack)

        self.login_usrinput = tk.Entry(self.login_window, bd=5, font=custom_font,width=150)
        self.login_usrinput.pack(side=tk.TOP,fill=tk.BOTH,pady=5,padx=10)

        self.login_passtext = tk.Label(self.login_window, text="Password", font=custom_font)
        self.login_passtext.pack(default_pack)

        self.login_passinput = tk.Entry(self.login_window, bd=5, show="*", font=custom_font,width=150)
        self.login_passinput.pack(side=tk.TOP,fill=tk.BOTH,pady=5,padx=10)

        self.login_backtomain = tk.Button(self.login_window, text="Back", command=lambda:self.withdraw_login(), font=custom_font)
        self.login_backtomain.pack(side=tk.LEFT, anchor=tk.SW, padx=10, pady=10)

        self.login_confirm = tk.Button(self.login_window, text="Log In", command=lambda:self.ver_login(), font=custom_font)
        self.login_confirm.pack(side=tk.RIGHT,pady=10,padx=10,anchor=tk.SE)

    def withdraw_login(self):
        self.login_window.withdraw()
        self.deiconify()
        return

    def getusr_login(self):
        return self.login_usrinput.get()
        
    def usrdenied_login(self):
        messagebox.showerror("Denied","Username Tidak Ditemukan")

    def getpass_login(self):
        return self.login_passinput.get()
        
    def passdenied_login(self):
        messagebox.showerror("Denied","Password Salah")
        return

    def passacc_login(self):
        loginpass = messagebox.askyesno("Accepted","Masuk Aplikasi?")
        if loginpass:
            print("Masuk aplikasi")
            self.login_window.withdraw()
            self.initialize_app()
        return

    def ver_login(self):
        username = self.getusr_login()
        password = self.getpass_login()

        try:
            usr_data = dt.read_data(username)
            username_exist = True
        except FileNotFoundError:
            username_exist = False

        if username_exist:
            if password != usr_data[0]["password"]:
                dt.usr_path_data_create(username)
                self.passdenied_login()
            else:
                dt.usr_path_data_create(username)
                self.passacc_login()
        else:
            self.usrdenied_login()
        return

    def regist(self):
        self.menu.withdraw()

        self.regist_window = tk.Toplevel()
        self.regist_window.geometry("500x300")
        self.regist_window.title("Register")

        self.regist_usrtext = tk.Label(self.regist_window, text="Username", font=custom_font)
        self.regist_usrtext.pack(default_pack)
        self.regist_usrinput = tk.Entry(self.regist_window, bd=5,font=custom_font,width=150)
        self.regist_usrinput.pack(side=tk.TOP,fill=tk.BOTH,pady=5,padx=10)
            
        self.regist_passtext = tk.Label(self.regist_window, text="Password", font=custom_font)
        self.regist_passtext.pack(default_pack)
        self.regist_passinput = tk.Entry(self.regist_window, bd=5, show="*",font=custom_font,width=150)
        self.regist_passinput.pack(side=tk.TOP,fill=tk.BOTH,pady=5,padx=10)

        self.regist_passconf = tk.Label(self.regist_window, text="Confirm Password", font=custom_font)
        self.regist_passconf.pack(default_pack)
        self.regist_passconfinput = tk.Entry(self.regist_window, bd=5, show="*",font=custom_font,width=150)
        self.regist_passconfinput.pack(side=tk.TOP,fill=tk.BOTH,pady=5,padx=10)

        self.regist_backtomainreg = tk.Button(self.regist_window, text="Back", command=lambda:self.withdraw_regist(), font=custom_font)
        self.regist_backtomainreg.pack(side=tk.LEFT, anchor=tk.SW, padx=10, pady=10)

        self.regist_confirm = tk.Button(self.regist_window, text="Confirm",command=lambda:self.ver_regist(), font=custom_font)
        self.regist_confirm.pack(side=tk.RIGHT,pady=10,padx=10,anchor=tk.SE)
        return

    def withdraw_regist(self):
        self.regist_window.withdraw()
        self.deiconify()
        return

    def getusr_regist(self):
        return self.regist_usrinput.get()

    def usrdenied_regist(self):
        usrdenied = messagebox.askretrycancel("Denied","Username Sudah Digunakan\nMasukkan Username Unik")
        if usrdenied:
            self.withdraw_regist()
        else:
            self.exitapp()
        return

    def getpass_regist(self):
        return self.regist_passinput.get()
            
    def getpassconf_regist(self):
        return self.regist_passconfinput.get()

    def passacc_regist(self):
        registpass = messagebox.askyesno("Accepted","Lanjutkan Proses?")
        if registpass:
            print("go to user data")
            self.regist_window.withdraw()
            dt.add_data(username,usr_data)
            self.initiate_sign_up()
        return

    def passdenied_regist(self):
        messagebox.showerror("Denied","Password Tidak Cocok")
        return

    def ver_regist(self):
        global username
        username = self.getusr_regist()
        password = self.getpass_regist()
        passwordconf = self.getpassconf_regist()

        try:
            dt.read_data(username)
            file_exist = True
        except FileNotFoundError:
            file_exist = False 

        if password == passwordconf:
            pass_state = True
            usr_data[0]["password"] = password
        else:
            self.passdenied_regist()
            pass_state = False

        if file_exist:
            self.usrdenied_regist()
            username_state = False
        else:
            username_state = True

        if username_state and pass_state:
            dt.usr_path_data_create(username)
            self.passacc_regist()
        else:
            pass
        return

    def initiate_sign_up(self):
        su.main()
        self.deinitailize_sign_up()
        return

    def deinitailize_sign_up(self):
        dt.del_data()
        self.deiconify()
        su.quits()
        return
    
    def initialize_app(self):
        ap.start()
        self.deinitailize_app()
        return

    def deinitailize_app(self):
        ap.exitapp()
        self.quit()
        return

apps = WALLABI()
v = apps.mainloop()

if not v:
    try : 
        dt.del_data()
    except:
        pass
    exit()
