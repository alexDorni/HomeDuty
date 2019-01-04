import tkinter as tk


class RecoverUiPass:
    email_ins  = None
    finish_btn = None

    def __init__(self, master=None):
        self._master = master
        self.create_ui_reconver_pass()

    def create_ui_reconver_pass(self):
        self.create_email()
        self.create_finish_btn()

    def create_email(self):
        tk.Label(self._master, text="Email").grid(row=0)
        self.email_ins = tk.Entry(self._master)
        self.email_ins.grid(row=0, column=1)

    def create_finish_btn(self):
        self.finish_btn = tk.Button(self._master, text="Finish")
        self.finish_btn.grid(row=1, column=2)

