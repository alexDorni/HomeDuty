import tkinter as tk

from tabs_dir.tab_controller_logic.tab_controller_logic import ControllerUiLogic
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

        self.__create_ui_register()

    def __create_ui_register(self):
        self.__create_user_name()
        self.__create_first_name()
        self.__create_last_name()
        self.__create_password()
        self.__create_retype_pass()
        self.__create_register_btn()

    def __create_user_name(self):
        tk.Label(self._master, text="User Name").grid(row=0)
        self.user_name = tk.Entry(self._master)
        self.user_name.grid(row=0, column=1)

    def __create_first_name(self):
        tk.Label(self._master, text="First Name").grid(row=1)
        self.first_name = tk.Entry(self._master)
        self.first_name.grid(row=1, column=1)

    def __create_last_name(self):
        tk.Label(self._master, text="Last Name").grid(row=2)
        self.last_name = tk.Entry(self._master)
        self.last_name.grid(row=2, column=1)

    def __create_password(self):
        tk.Label(self._master, text="Insert password").grid(row=3)
        self.password_ins = tk.Entry(self._master)
        self.password_ins.grid(row=3, column=1)

    def __create_retype_pass(self):
        tk.Label(self._master, text="Retype password").grid(row=4)
        self.password_ret = tk.Entry(self._master)
        self.password_ret.grid(row=4, column=1)

    def __create_register_btn(self):
        self.register_btn = tk.Button(self._master, text="Registration", command=self.__command_reg_btn)
        self.register_btn.grid(row=5, column=5)

    def __command_reg_btn(self):
        reg_adapt_handler = RegAdaptHandler(self)
        if reg_adapt_handler.execute():
            tk.messagebox.showinfo("Registration", "Registration Successful")
            ControllerUiLogic.select_login_tab()
        else:
            tk.messagebox.showinfo("Registration", "Registration Failed! \nSome problems could be:\n"
                                                   "Blank fields \nWrong password \nUser already exists")
        self.__reset_entrys()

    def __reset_entrys(self):
        self.user_name.delete(0, "end")
        self.first_name.delete(0, "end")
        self.last_name.delete(0, "end")
        self.password_ins.delete(0, "end")
        self.password_ret.delete(0, "end")


