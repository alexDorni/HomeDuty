import tkinter as tk


class RegUi:
    email_entry  = None
    ins_password = None
    ret_password = None
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
        self.email_entry = tk.Entry(self._master)
        self.email_entry.grid(row=0, column=1)

    def create_password(self):
        tk.Label(self._master, text="Insert password").grid(row=1)
        self.ins_password = tk.Entry(self._master)
        self.ins_password.grid(row=1, column=1)

    def create_retype_pass(self):
        tk.Label(self._master, text="Retype password").grid(row=2)
        self.ret_password = tk.Entry(self._master)
        self.ret_password.grid(row=2, column=1)

    def create_register_btn(self):
        self.register_btn = tk.Button(self._master, text="Registration")
        self.register_btn.grid(row=3, column=5)
