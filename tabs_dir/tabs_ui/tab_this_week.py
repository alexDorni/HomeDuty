import tkinter as tk


class ThisWeek:
    def __init__(self, master=None):
        self.__master = master
        self.refresh_btn = None
        self.top_listbox = None
        self.image_label = None
        self.username_label = None
        self.type_label = None
        self.status_label = None