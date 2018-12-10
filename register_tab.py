import tkinter as tk


class RegUi:
    email_ins    = None
    password_ins = None
    password_ret = None
    register_btn = None

    def __init__(self, master=None):
        self._master = master
        self.create_ui_register()

    def create_ui_register(self):
        self.create_register_btn()
        self.create_email()
        self.create_password()
        self.create_retype_pass()

    def create_email(self):
        tk.Label(self._master, text="Email").grid(row=0)
        self.email_ins = tk.Entry(self._master)
        self.email_ins.grid(row=0, column=1)

    def create_password(self):
        tk.Label(self._master, text="Insert password").grid(row=1)
        self.password_ins = tk.Entry(self._master)
        self.password_ins.grid(row=1, column=1)

    def create_retype_pass(self):
        tk.Label(self._master, text="Retype password").grid(row=2)
        self.password_ret = tk.Entry(self._master)
        self.password_ret.grid(row=2, column=1)

    def create_register_btn(self):
        self.register_btn = tk.Button(self._master, text="Registration")
        self.register_btn.grid(row=3, column=5)
