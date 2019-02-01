import tkinter as tk
from tabs_dir.tab_controller_logic import tab_controller
import global_instances


class InterfaceDuty(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Home duty")
        self.master.geometry("700x500")
        self.pack()
        tab = tab_controller.TabController(master)

        # Global instance for tabs ui
        global_instances.TABS = tab

        tab.create_tabs()
