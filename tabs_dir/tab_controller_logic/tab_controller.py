from tabs_dir.tab_controller_logic.tab_controller_logic import ControllerUiLogic
from tabs_dir.tab_controller_logic import tab_enum, tab_factory
import tkinter.ttk as ttk


class TabController:
    def __init__(self, master=None):
        self.tab_frame_dict = {}
        self._master = master
        self.tab_control = ttk.Notebook(self._master)

    def create_tabs(self):
        for enum_tab in tab_enum.Tab:
            # Create frame
            tab_frame = ttk.Frame(self.tab_control)
            # {Enum : new tab Frame}
            self.tab_control.add(tab_frame, text=enum_tab.name)
            # TODO BIND EVENTS TO TABS SELECTED

            ui_obj_tab = tab_factory.TabFactory.create(enum_tab.name, tab_frame)
            self.tab_frame_dict.update({enum_tab.name: ui_obj_tab})

        self.tab_control.pack(expand=1, fill="both")
        ControllerUiLogic.disable_tabs_before_login()

