import os
import tkinter as tk
import threading


class Spinner(threading.Thread):
    def __init__(self, master_frame=None):
        threading.Thread.__init__(self)
        self.__master = master_frame

        self.__spinner_path_gif = os.getcwd() + "/images" + "/spinner" + "/spinner.gif"
        self.__label_spinner = None

    def create_label_spinner(self):
        self.__label_spinner = tk.Label(self.__master, image=self.__spinner_path_gif)

    def update_frame(self):
        pass
