import tkinter as tk
from tabs_dir.tab_handler.reg_adapt_handler import RegAdaptHandler


class RegUi:

    def __init__(self, master=None):
        self._master = master

        self.user_name = None
        self.first_name = None
        self.last_name = None
        self.password_ins = None
        self.password_ret = None
        self.register_btn = None

        self.create_ui_register()

    def create_ui_register(self):
        self.create_user_name()
        self.create_first_name()
        self.create_last_name()
        self.create_password()
        self.create_retype_pass()
        self.create_register_btn()

    def create_user_name(self):
        tk.Label(self._master, text="User Name").grid(row=0)
        self.user_name = tk.Entry(self._master)
        self.user_name.grid(row=0, column=1)

    def create_first_name(self):
        tk.Label(self._master, text="First Name").grid(row=1)
        self.first_name = tk.Entry(self._master)
        self.first_name.grid(row=1, column=1)

    def create_last_name(self):
        tk.Label(self._master, text="Last Name").grid(row=2)
        self.last_name = tk.Entry(self._master)
        self.last_name.grid(row=2, column=1)

    def create_password(self):
        tk.Label(self._master, text="Insert password").grid(row=3)
        self.password_ins = tk.Entry(self._master)
        self.password_ins.grid(row=3, column=1)

    def create_retype_pass(self):
        tk.Label(self._master, text="Retype password").grid(row=4)
        self.password_ret = tk.Entry(self._master)
        self.password_ret.grid(row=4, column=1)

    def create_register_btn(self):
        self.register_btn = tk.Button(self._master, text="Registration", command=self.command_reg_btn)
        self.register_btn.grid(row=5, column=5)

    def command_reg_btn(self):
        # TODO PROGRESS TOOLBAR IMPLEMENTATION
        reg_adapt_handler = RegAdaptHandler(self)
        if reg_adapt_handler.execute():
            tk.messagebox.showinfo("Registration", "Registration Successful")
        else:
            tk.messagebox.showinfo("Registration", "Registration Failed")

    # Getters
    @property
    def user_name(self):
        return self._user_name

    @property
    def password_ins(self):
        return self._password_ins

    @property
    def password_ret(self):
        return self._password_ret

    @property
    def register_btn(self):
        return self._register_btn

    # Setters
    @user_name.setter
    def user_name(self, val):
        self._user_name = val

    @password_ins.setter
    def password_ins(self, val):
        self._password_ins = val

    @password_ret.setter
    def password_ret(self, val):
        self._password_ret = val

    @register_btn.setter
    def register_btn(self, val):
        self._register_btn = val


