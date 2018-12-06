import tkinter as tk
import tkinter.ttk as ttk
import fire_database
import tabs


class InterfaceDuty(tk.Frame):

    tree = None
    tab_list = []

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # Set title
        self.master.title("Home duty")
        # Set size of window
        self.master.geometry("700x500")
        # Don't allow resizable
        # self.master.resizable(0, 0)
        # Create the tab control
        self.tab_control = ttk.Notebook(self.master)
        self.pack()
        self.create_tabs()

    def create_tabs(self):
        for enum_tab in tabs.Tab:
            # Create frame
            tab_frame = ttk.Frame(self.tab_control)
            self.tab_list.append(tab_frame)
            # Add tab
            self.tab_control.add(tab_frame, text=enum_tab.get_val())
        self.tab_control.pack(expand=1, fill="both")

