import global_instances
from images.spinner.spinner import Spinner
from tabs_dir.tab_controller_logic.tab_controller import TabController


class FrameSwitch:
    def __init__(self, master=None):
        self.__master = master

        self.__master.pack(side="top", fill="both", expand=True)
        self.__master.grid_rowconfigure(0, weight=1)
        self.__master.grid_columnconfigure(0, weight=1)

        self.frames_switch_dict = {}

        for F in (TabController, Spinner):
            page_name = F.__name__
            print(page_name)
            frame = F(self.__master)
            self.frames_switch_dict[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
