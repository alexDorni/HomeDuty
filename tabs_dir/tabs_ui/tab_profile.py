import tkinter as tk
import easygui
import os

# pip install pillow ( the new PIL )
from PIL import Image, ImageTk
from tkinter import messagebox

import global_instances
from firebase_database import database_obj
from images.spinner.spinner_path import GIF_FRAMES_COUNT, spinner_path
from tabs_dir.tab_handler.profile_adapt_handler.profile_adpt_hndl_log_out import ProfileLogOut
from tabs_dir.tab_handler.profile_adapt_handler.profile_adpt_hndl_upd_img import ProfileHandlerUpdImg
from tabs_dir.tab_handler.profile_adapt_handler.profile_adpt_hndl_upd_name import ProfileHandlerUdpName
from tabs_dir.tabs_ui.tabs_threads.tab_profile_threads.profile_upd_img_thread import ProfileUpdateImgThread
from tabs_dir.tabs_ui.tabs_threads.tab_profile_threads.profile_upd_user_thread import ProfileUpdUserThread


class ProfileUi:
    def __init__(self, master=None):
        self.__master = master
        self.image_label = None
        self.entry_first_name = None
        self.entry_last_name = None
        self.btn_update_name = None
        self.btn_img_upload = None
        self.btn_log_out = None

        self.update_in_progress = False

        self.__user_image_default = os.getcwd() + "\images" + "\default_img_user.png"
        self.__user_image_saved = os.getcwd() + "\images" + "\image_user.png"
        self.__create_ui()

    def on_update_image_started(self):
        self.__on_update_template_started()

        # Open windows explorer interface
        image_path = easygui.fileopenbox()

        ProfileHandlerUpdImg(self, image_path).execute()

    def on_update_image_done(self, is_success=None):
        self.__on_update_template_done()

        # Kill the thread
        global_instances.THREADS_DICT.pop(ProfileUpdateImgThread.THREAD_NAME)

        if is_success:
            messagebox.showinfo("Image", "Image updated successful")

    def on_update_username_started(self):
        self.__on_update_template_started()

        ProfileHandlerUdpName(self).execute()

    def on_update_username_done(self, is_success=None):
        self.__on_update_template_done()

        # Kill the thread
        global_instances.THREADS_DICT.pop(ProfileUpdUserThread.THREAD_NAME)

        if is_success:
            messagebox.showinfo("Username", "Username updated successfully")

    def update_image_label(self):
        try:
            if not database_obj.user_name_login:
                self.__create_image_label(self.__user_image_default)
            else:
                self.__create_image_label(self.__user_image_saved)
        except OSError:
            tk.messagebox.showinfo("Upload Image Error", "Wrong image format")

    def __on_update_template_started(self):
        self.update_in_progress = True

        self.__disable_user_actions()

        self.image_spinner_label.grid(row=6, column=5)

        self.__update_spinner()

    def __on_update_template_done(self):
        self.update_in_progress = False
        self.__enable_user_actions()

        self.image_spinner_label.grid_remove()

    def __create_spinner(self):
        self.image_spinner_label = tk.Label(self.__master)
        self.image_spinner_label.config(height=250, width=250)
        self.image_spinner_label.grid(row=6, column=5)

        self.image_spinner_frames = [tk.PhotoImage(file=spinner_path,
                                                   format="gif -index %i" % i) for i in range(GIF_FRAMES_COUNT)
                                     ]

    def __update_spinner(self, ind=0):
        if not self.update_in_progress:
            return

        ind %= GIF_FRAMES_COUNT
        spinner_frame = self.image_spinner_frames[ind]
        ind += 1
        self.image_spinner_label.configure(image=spinner_frame)
        self.__master.after(100, self.__update_spinner, ind)

    def __create_ui(self):
        self.update_image_label()
        self.__create_entry_name()
        self.__create_btn_img_upload()
        self.__create_btn_upd_name()
        self.__create_btn_log_out()
        self.__create_spinner()

    def __create_image_label(self, image_path):
        image = Image.open(image_path)
        image_resize = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image_resize)

        self.image_label = tk.Label(self.__master, image=photo)
        self.image_label.image = photo
        self.image_label.grid(row=0, column=0)

    # Creation of entry
    def __create_entry_name(self):
        self.__create_entry_first_name()
        self.__create_entry_last_name()

    def __create_entry_first_name(self):
        self.entry_first_name = tk.Entry(self.__master)
        self.entry_first_name.grid(row=1, column=0)

    def __create_entry_last_name(self):
        self.entry_last_name = tk.Entry(self.__master)
        self.entry_last_name.grid(row=1, column=1)

    # Creation of buttons
    def __create_btn_img_upload(self):
        self.btn_img_upload = tk.Button(self.__master, text="Upload Image", command=self.__command_img_upload)
        self.btn_img_upload.grid(row=0, column=1)

    def __create_btn_upd_name(self):
        self.btn_update_name = tk.Button(self.__master, text="Update Name", command=self.__command_btn_upd_name)
        self.btn_update_name.grid(row=1, column=2)

    def __create_btn_log_out(self):
        self.btn_log_out = tk.Button(self.__master, text="Log out", command=self.__command_btn_log_out)
        self.btn_log_out.grid(row=5, column=1)

    # Command of buttons
    def __command_img_upload(self):
        self.on_update_image_started()

    def __command_btn_upd_name(self):
        self.on_update_username_started()

    def __command_btn_log_out(self):
        ProfileLogOut().execute()
        self.__refresh_user_name()
        tk.messagebox.showinfo("Log out", "Log out successful")

    # User actions
    def __disable_user_actions(self):
        self.btn_img_upload.configure(state="disabled")
        self.btn_update_name.configure(state="disabled")
        self.btn_log_out.configure(state="disabled")

        self.entry_last_name.configure(state="disabled")
        self.entry_first_name.configure(state="disabled")

    def __enable_user_actions(self):
        self.btn_img_upload.configure(state="normal")
        self.btn_update_name.configure(state="normal")
        self.btn_log_out.configure(state="normal")

        self.entry_last_name.configure(state="normal")
        self.entry_first_name.configure(state="normal")

    def __refresh_user_name(self):
        self.entry_last_name.delete(0, "end")
        self.entry_first_name.delete(0, "end")
