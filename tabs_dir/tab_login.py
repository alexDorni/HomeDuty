import tkinter as tk
import os


class LoginUi:
    image_label  = None
    email_ins    = None
    password_ins = None
    login_btn    = None

    def __init__(self, master=None):
        self._master = master
        self.create_ui_login()

    def create_ui_login(self):
        self.create_image()
        self.create_email()
        self.create_pass()
        self.create_login_btn()

    def create_image(self):
        image_path = os.getcwd() + "\images" + "\image_user.gif"
        photo = tk.PhotoImage(file=image_path)
        self.image_label = tk.Label(self._master, image=photo)
        self.image_label.image = photo
        self.image_label.grid(row=0, column=10)

    def create_email(self):
        tk.Label(self._master, text="Email").grid(row=4)
        self.email_ins = tk.Entry(self._master)
        self.email_ins.grid(row=4, column=1)

    def create_pass(self):
        tk.Label(self._master, text="Password").grid(row=5)
        self.password_ins = tk.Entry(self._master)
        self.password_ins.grid(row=5, column=1)

    def create_login_btn(self):
        self.login_btn = tk.Button(self._master, text="Login")
        self.login_btn.grid(row=8, column=10)
