from tabs_dir import tab_enum, tab_factory
import tkinter.ttk as ttk


class TabController:

    def __init__(self, master=None):
        self.tab_frame_dic = {}
        self._master = master
        self.tab_control = ttk.Notebook(self._master)

    def create_tabs(self):
        for enum_tab in tab_enum.Tab:
            # Create frame
            tab_frame = ttk.Frame(self.tab_control)
            # {Enum : new tab Frame}
            self.tab_frame_dic.update({enum_tab.name: tab_frame})
            self.tab_control.add(tab_frame, text=enum_tab.value)
        self.tab_control.pack(expand=1, fill="both")
        self.create_ui_tabs()

    def create_ui_tabs(self):
        for item_factory in self.tab_frame_dic:
            tab_obj = tab_factory.TabFactory()
            tab_obj.create_tab(item_factory, master=self.tab_frame_dic.get(item_factory))
