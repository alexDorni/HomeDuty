import tkinter as tk
from tkinter import ttk
import os

from PIL import Image, ImageTk

from images.spinner.spinner_path import GIF_FRAMES_COUNT, spinner_path
from images.image_convert import image_path
from tkinter import ttk


class ThisWeek:
    def __init__(self, master=None):
        self.__master = master
        self.refresh_btn = None
        self.image_spinner_label = None
        self.top_users_label = None
        self.status_combobox = None
        self.update_btn = None

        self.top_place_1 = None
        self.top_place_2 = None
        self.top_place_3 = None

        self.top_tree_view = None
        self.tasks_tree_view = None

        self.image_label = None

        self.__create_this_week_ui()

    def insert_data_tree_view(self, name='', points=0):
        # TODO color them
        points = tk.Checkbutton(self, text=name)
        self.top_tree_view.insert('', "end", text=name, values=points)
        self.tasks_tree_view.insert('', "end", text=name, values=points)

    def __create_this_week_ui(self):
        # self.__create_refresh_btn()
        # self.__create_spinner()
        # self.__create_winner_image_label()
        # self.__create_user_image_profile()
        # self.__create_tasks_tree_view()
        # self.__create_combobox_status()
        # self.__create_update_btn()
        self.__create_winner_image_label()

    def __create_user_image_profile(self):
        img_label = self.__create_image_label(image_path.user_image_saved)
        img_label.grid(row=1, column=4, padx=(100, 0))

    def __create_image_label(self, img_path):
        image = Image.open(img_path)
        image_resize = image.resize((150, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image_resize)

        image_label = tk.Label(self.__master, image=photo)
        image_label.image = photo

        return image_label

    def __create_winner_image_label(self, user_winners_dict=None):
        top_users_label = tk.Label(self.__master, text="Top in this week")
        top_users_label.grid(row=0, column=0)

        if not user_winners_dict:

            self.top_place_1 = self.__create_image_label(image_path.user_image_default)
            self.top_place_2 = self.__create_image_label(image_path.user_image_default)
            self.top_place_3 = self.__create_image_label(image_path.user_image_default)

            self.top_place_1.grid(row=1, column=0, padx=(10, 0))
            self.top_place_2.grid(row=1, column=1, pady=(0, 90))
            self.top_place_3.grid(row=1, column=2, pady=(0, 30))



    # def __create_winner_top_users(self):
    #
    #     image = Image.open(self.__user_image_saved)
    #     image_resize = image.resize((150, 150), Image.ANTIALIAS)
    #     photo = ImageTk.PhotoImage(image_resize)
    #
    #     self.image_label = tk.Label(self.__master, image=photo)
    #     self.image_label.image = photo
    #     self.image_label.grid(row=1, column=0, padx=(10, 0))
    #
    #     self.image_label = tk.Label(self.__master, image=photo)
    #     self.image_label.image = photo
    #     self.image_label.grid(row=1, column=1, pady=(0, 90))
    #
    #     self.image_label = tk.Label(self.__master, image=photo)
    #     self.image_label.image = photo
    #     self.image_label.grid(row=1, column=2, pady=(0, 30))

    def __create_tasks_tree_view(self):
        task_tree_label = tk.Label(self.__master, text="Your tasks")
        task_tree_label.grid(row=2, column=0)
        self.tasks_tree_view = ttk.Treeview(self.__master)

        # Creation of columns then the headings (tkinter logic)
        self.__create_tasks_column()
        self.__create_tasks_heading()
        self.__create_tasks_scrollbar()

    def print_ceva(self):
        print("name")

    def __create_tasks_heading(self):
        self.tasks_tree_view["show"] = "headings"
        # TODO command if its pressed
        # TODO realized points + left points
        # TODO list of check buttons
        # probably with lambda
        self.tasks_tree_view.heading("name", text="Name", command=self.print_ceva)
        self.tasks_tree_view.heading("type", text="Type")
        self.tasks_tree_view.heading("points", text="Points")
        self.tasks_tree_view.heading("status", text="Status")

    def __create_tasks_column(self):
        self.tasks_tree_view["columns"] = ("name", "type", "points", "status")
        self.tasks_tree_view.column("name", width=250, stretch=False)
        self.tasks_tree_view.column("type", width=50, stretch=False)
        self.tasks_tree_view.column("points", width=50, stretch=True)
        self.tasks_tree_view.column("status", stretch=False)

    def __create_tasks_scrollbar(self):
        ysb = ttk.Scrollbar(self.__master, orient="vertical", command=self.tasks_tree_view.yview)
        self.tasks_tree_view.grid(row=3, column=0, columnspan=4, sticky='nsew')
        ysb.grid(row=3, column=1, columnspan=3, sticky='nes')
        self.tasks_tree_view.configure(yscroll=ysb.set)
        #
        # for i in range(10):
        #     self.insert_data_tree_view()
        # for i in range(10):
        #     self.insert_data_tree_view("2", 1)

    def __create_refresh_btn(self):
        self.refresh_btn = tk.Button(self.__master, text="Refresh me")
        self.refresh_btn.grid(row=2, column=4, padx=(100, 0))

    def __create_combobox_status(self):
        status_label = tk.Label(self.__master, text="Select task state")
        status_label.grid(row=3, column=4, pady=(50, 0), sticky="n")

        __status_list = ("done", "todo")
        self.status_combobox = ttk.Combobox(self.__master,
                                            values=__status_list,
                                            state="readonly")
        self.status_combobox.grid(row=3, column=4,
                                  rowspan=3, pady=(0, 150),
                                  sticky="we")

    def __create_update_btn(self):
        self.update_btn = tk.Button(self.__master, text="Update task")
        self.update_btn.grid(row=3, column=4, pady=(0, 20), sticky="s")

    def __create_spinner(self):
        self.image_spinner_label = tk.Label(self.__master)
        self.image_spinner_label.config(height=100, width=100)
        self.image_spinner_label.grid(row=4, column=2, pady=(30, 0))

        self.image_spinner_frames = [tk.PhotoImage(file=spinner_path,
                                                   format="gif -index %i" % i) for i in range(GIF_FRAMES_COUNT)
                                     ]
        self.__update_spinner()

    def __update_spinner(self, ind=0):

        ind %= GIF_FRAMES_COUNT
        spinner_frame = self.image_spinner_frames[ind]
        ind += 1
        self.image_spinner_label.configure(image=spinner_frame)
        self.__master.after(100, self.__update_spinner, ind)

    def __disable_refresh_btn(self):
        self.refresh_btn.configure(state="disabled")

    def __enable_refresh_btn(self):
        self.refresh_btn.configure(state="normal")
