import tkinter as tk
from tabs_dir.tab_controller_logic import tab_controller
import global_instances


class InterfaceDuty(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Home duty")
        self.master.geometry("800x600")
        self.pack()
        tab = tab_controller.TabController(master)

        # Global instance for tabs ui
        global_instances.TABS = tab

        global_instances.TABS_MAP_FRAMES = tab.tab_frame_dict

        tab.create_tabs()
