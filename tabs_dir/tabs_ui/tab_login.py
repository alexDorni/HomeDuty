from tabs_dir.tab_handler.login_adapt_handler import LoginAdaptHandler
import tkinter as tk
from tkinter import messagebox
import os


class LoginUi:
    def __init__(self, master=None):
        self._master = master

        self.image_label = None
        self.user_name = None
        self.password_ins = None
        self.login_btn = None

        self.create_ui_login()

    def create_ui_login(self):
        self.create_image()
        self.create_email()
        self.create_password()
        self.create_login_btn()

    def create_image(self):
        image_path = os.getcwd() + "\images" + "\image_user.gif"
        photo = tk.PhotoImage(file=image_path)
        self.image_label = tk.Label(self._master, image=photo)
        self.image_label.image = photo
        self.image_label.grid(row=0, column=10)

    def create_email(self):
        tk.Label(self._master, text="User Name").grid(row=4)
        self.user_name = tk.Entry(self._master)
        self.user_name.grid(row=4, column=1)

    def create_password(self):
        tk.Label(self._master, text="Password").grid(row=5)
        self.password_ins = tk.Entry(self._master)
        self.password_ins.grid(row=5, column=1)

    def create_login_btn(self):
        self.login_btn = tk.Button(self._master, text="Login", command=self.command_login_btn)
        self.login_btn.grid(row=8, column=10)

    def command_login_btn(self):
        login_handler = LoginAdaptHandler(self)
        if login_handler.execute():
            messagebox.showinfo("Login", "Successful Login")
        else:
            messagebox.showinfo("Login", "Incorrect username or password")

    # Getters
    @property
    def user_name(self):
        return self._user_name

    @property
    def password_ins(self):
        return self._password_ins

    @property
    def login_btn(self):
        return self._login_btn

    # Setters
    @user_name.setter
    def user_name(self, val):
        self._user_name = val

    @password_ins.setter
    def password_ins(self, val):
        self._password_ins = val

    @login_btn.setter
    def login_btn(self, val):
        self._login_btn = val
