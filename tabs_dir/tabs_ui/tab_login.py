import tkinter as tk
import os

import global_instances
from firebase_database import database_obj
from tabs_dir.tab_upd_logic.tab_profile_update import ProfileUiUpdate
from tabs_dir.tab_controller_logic.tab_controller_logic import ControllerUiLogic
from tabs_dir.tab_handler.login_adapt_handler import LoginAdaptHandler
from images.spinner.spinner_path import spinner_path, GIF_FRAMES_COUNT

# pip install pillow ( the new PIL )
from PIL import Image, ImageTk

from tabs_dir.tabs_ui.tabs_threads.tab_login_threads.login_thread import LoginThread


class LoginUi:
    def __init__(self, master=None):
        self.__master = master

        self.image_label = None
        self.image_spinner_label = None
        self.user_name = None
        self.password_ins = None
        self.login_btn = None

        self.image_spinner_frames = []
        self.login_in_progress = False

        self.__create_ui_login()

    def on_login_done(self, is_successful=False):
        self.login_in_progress = False

        if is_successful:
            # Update the current user in the app
            database_obj.user_name_login = self.user_name.get()

            ProfileUiUpdate().update_profile_ui()
            ControllerUiLogic.disable_login_tab()
            ControllerUiLogic.enable_tabs_after_login()
            tk.messagebox.showinfo("Login", "Login successful")
        else:
            tk.messagebox.showinfo("Login", "Username or password incorrect")

        self.__enable_user_actions()

        self.image_spinner_label.grid_remove()

        # Kill the thread
        global_instances.THREADS_DICT.pop(LoginThread.THREAD_NAME)

    def __on_login_started(self):
        self.login_in_progress = True

        self.__disable_user_actions()

        # Make the spinner visible
        self.image_spinner_label.grid(row=9, column=5)

        # Start the spinner
        self.__update_spinner(0)

        LoginAdaptHandler(self).execute()

    def __create_ui_login(self):
        self.__create_image()
        self.__create_username()
        self.__create_password()
        self.__create_login_btn()
        self.__create_spinner()

    def __create_image(self):
        image_path = os.getcwd() + "\images" + "\default_img_user.png"
        image = Image.open(image_path)
        image_resize = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image_resize)

        self.image_label = tk.Label(self.__master, image=photo)
        self.image_label.image = photo
        self.image_label.grid(row=0, column=2)

    def __create_username(self):
        tk.Label(self.__master, text="User Name").grid(row=4)
        self.user_name = tk.Entry(self.__master)
        self.user_name.grid(row=4, column=1)

    def __create_password(self):
        tk.Label(self.__master, text="Password").grid(row=5)
        self.password_ins = tk.Entry(self.__master)
        self.password_ins.grid(row=5, column=1)

    def __create_login_btn(self):
        self.login_btn = tk.Button(self.__master,
                                   activebackground='green',
                                   text="Login", command=self.__command_login_btn)
        self.login_btn.grid(row=6, column=2)

    def __command_login_btn(self):
        self.__on_login_started()

    def __create_spinner(self):
        self.image_spinner_label = tk.Label(self.__master)
        self.image_spinner_label.config(height=250, width=250)
        self.image_spinner_label.grid(row=9, column=5)

        self.image_spinner_frames = [tk.PhotoImage(file=spinner_path,
                                                   format="gif -index %i" % i) for i in range(GIF_FRAMES_COUNT)
                                     ]

    def __update_spinner(self, ind):
        if not self.login_in_progress:
            return

        ind %= GIF_FRAMES_COUNT
        spinner_frame = self.image_spinner_frames[ind]
        ind += 1
        self.image_spinner_label.configure(image=spinner_frame)
        self.__master.after(100, self.__update_spinner, ind)

    def __disable_user_actions(self):
        self.user_name.configure(state="disabled")
        self.password_ins.configure(state="disabled")
        self.login_btn.configure(state="disabled")

    def __enable_user_actions(self):
        self.user_name.configure(state="normal")
        self.password_ins.configure(state="normal")
        self.login_btn.configure(state="normal")

        # Reset fields
        self.user_name.delete(0, "end")
        self.password_ins.delete(0, "end")
