import tkinter as tk
import os

import global_instances
from firebase_database import database_obj
from tabs_dir.tab_controller_logic.tab_controller_logic import ControllerUiLogic
from tabs_dir.tab_handler.login_adapt_handler import LoginAdaptHandler
from images.spinner.spinner_path import spinner_path

# pip install pillow ( the new PIL )
from PIL import Image, ImageTk

from tabs_dir.tabs_ui.login_thread import LoginThread


class LoginUi:
    GIF_FRAMES_COUNT = 50

    def __init__(self, master=None):
        self._master = master

        self.image_label = None
        self.image_spinner_label = None
        self.image_spinner_frames = None
        self.user_name = None
        self.password_ins = None
        self.login_btn = None

        self.in_progress = False

        self.create_ui_login()

    def create_ui_login(self):
        self.__create_image()
        self.__create_username()
        self.__create_password()
        self.__create_login_btn()
        self.create_spinner()

    def create_spinner(self):
        self.image_spinner_label = tk.Label(self._master)
        self.image_spinner_label.grid(row=9, column=10)
        self.image_spinner_frames = [tk.PhotoImage(file=spinner_path, format="gif -index %i" % i) for i in range(LoginUi.GIF_FRAMES_COUNT)]

    def update_spinner(self, ind):
        if not self.in_progress:
            return

        ind %= LoginUi.GIF_FRAMES_COUNT
        spinner_frame = self.image_spinner_frames[ind]
        ind += 1
        self.image_spinner_label.configure(image=spinner_frame)
        self._master.after(100, self.update_spinner, ind)

    def on_login_done(self, is_successful=False):
        self.in_progress = False
        # TODO enable fields
        # TODO HIDE SPINNER
        # TODO THINK DESTROY SPINNER
        if is_successful:
            # message box
            self.image_spinner_label.grid_remove()
            database_obj.user_name_login = self.user_name.get()
            ControllerUiLogic.disable_login_tab()
            ControllerUiLogic.enable_tabs_after_login()
            print("Login Successful")
        else:
            print("Login Failed")

        global_instances.THREADS_DICT.pop(LoginThread.THREAD_NAME)
        print("POP", global_instances.THREADS_DICT)

    def on_login_started(self):
        self.in_progress = True
        self.image_spinner_label.grid(row=9, column=10)
        self.update_spinner(0)

        login_thread = LoginThread(self)
        global_instances.THREADS_DICT[LoginThread.THREAD_NAME] = login_thread
        print("ADD", global_instances.THREADS_DICT)
        login_thread.start()

    def __create_image(self):
        image_path = os.getcwd() + "\images" + "\default_img_user.png"
        image = Image.open(image_path)
        image_resize = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image_resize)

        self.image_label = tk.Label(self._master, image=photo)
        self.image_label.image = photo
        self.image_label.grid(row=0, column=10)

    def __create_username(self):
        tk.Label(self._master, text="User Name").grid(row=4)
        self.user_name = tk.Entry(self._master)
        self.user_name.grid(row=4, column=1)

    def __create_password(self):
        tk.Label(self._master, text="Password").grid(row=5)
        self.password_ins = tk.Entry(self._master)
        self.password_ins.grid(row=5, column=1)

    def __create_login_btn(self):
        self.login_btn = tk.Button(self._master,
                                   activebackground='green',
                                   text="Login", command=self.__command_login_btn)
        self.login_btn.grid(row=8, column=10)

    def __command_login_btn(self):
        self.on_login_started()
        # LoginAdaptHandler(self).execute()

    # Getters
    @property
    def user_name(self):
        return self._user_name

    @property
    def password_ins(self):
        return self._password_ins

    @property
    def login_btn(self):
        return self._login_btn

    # Setters
    @user_name.setter
    def user_name(self, val):
        self._user_name = val

    @password_ins.setter
    def password_ins(self, val):
        self._password_ins = val

    @login_btn.setter
    def login_btn(self, val):
        self._login_btn = val
