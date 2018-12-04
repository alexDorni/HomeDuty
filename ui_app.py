import tkinter as tk
import tkinter.ttk as ttk


class InterfaceDuty(tk.Frame):

    tree = None

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # Set title
        self.master.title("Home duty")
        # Set size of window
        self.master.geometry("700x500")
        # Don't allow resizable
        self.master.resizable(0, 0)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self)
        self.tree.pack()
        self.tree['columns'] = ('subject', 'tests', 'status', 'bug')

def say_hi(self):
        print("hi there, everyone!")

