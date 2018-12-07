import tkinter as tk
import tkinter.ttk as ttk
import tab_controller


class InterfaceDuty(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Home duty")
        self.master.geometry("700x500")
        self.pack()
        tab_controller.TabController(master)
