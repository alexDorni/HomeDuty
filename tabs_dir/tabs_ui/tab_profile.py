import tkinter as tk
import easygui
import os

# pip install pillow ( the new PIL )
from PIL import Image, ImageTk
from firebase_database import database_obj
from tabs_dir.tab_handler.profile_adapt_handler.profile_adpt_hndl_log_out import ProfileLogOut
from tabs_dir.tab_handler.profile_adapt_handler.profile_adpt_hndl_upd_img import ProfileHandlerUpdImg
from tabs_dir.tab_handler.profile_adapt_handler.profile_adpt_hndl_upd_name import ProfileHandlerUdpName


# class ProfileUi:
#     def __init__(self, master=None):
#         self.__master = master
#         self.image_label = None
#         self.entry_first_name = None
#         self.entry_last_name = None
#         self.btn_update_name = None
#         self.btn_img_upload = None
#         self.btn_log_out = None
#
#         self.__user_image_default = os.getcwd() + "\images" + "\default_img_user.png"
#         self.__user_image_saved = os.getcwd() + "\images" + "\image_user.png"
#         self.__create_ui()
#
#     def __create_ui(self):
#         self.create_image_label()
#         self.__create_entry_name()
#         self.__create_btn_img_upload()
#         self.__create_btn_upd_name()
#         self.__create_btn_log_out()
#
#     # Creation of the user image
#     def create_image_label(self):
#         try:
#             if not database_obj.user_name_login:
#                 self.__create_image_path_file(self.__user_image_default)
#             else:
#                 self.__create_image_path_file(self.__user_image_saved)
#         except OSError:
#             tk.messagebox.showinfo("Upload Image Error", "Wrong image format")
#
#     def __create_image_path_file(self, image_path):
#         image = Image.open(image_path)
#         image_resize = image.resize((250, 250), Image.ANTIALIAS)
#         photo = ImageTk.PhotoImage(image_resize)
#
#         self.image_label = tk.Label(self.__master, image=photo)
#         self.image_label.image = photo
#         self.image_label.grid(row=0, column=0)
#
#     # Creation of entry
#     def __create_entry_name(self):
#         self.__create_entry_first_name()
#         self.__create_entry_last_name()
#
#     def __create_entry_first_name(self):
#         self.entry_first_name = tk.Entry(self.__master)
#         self.entry_first_name.grid(row=1, column=0)
#
#     def __create_entry_last_name(self):
#         self.entry_last_name = tk.Entry(self.__master)
#         self.entry_last_name.grid(row=1, column=1)
#
#     # Creation of buttons
#     def __create_btn_img_upload(self):
#         self.btn_img_upload = tk.Button(self.__master, text="Upload Image", command=self.__command_img_upload)
#         self.btn_img_upload.grid(row=0, column=1)
#
#     def __create_btn_upd_name(self):
#         self.btn_update_name = tk.Button(self.__master, text="Update Name", command=self.__command_btn_upd_name)
#         self.btn_update_name.grid(row=1, column=2)
#
#     def __create_btn_log_out(self):
#         self.btn_log_out = tk.Button(self.__master, text="Log out", command=self.__command_btn_log_out)
#         self.btn_log_out.grid(row=5, column=1)
#
#     # Command of buttons
#     @staticmethod
#     def __command_img_upload():
#         # Open windows explorer interface
#         image_path = easygui.fileopenbox()
#
#         # Execute update into db with new image
#         if ProfileHandlerUpdImg(image_path).execute():
#             tk.messagebox.showinfo("Image updated", "Image updated successful")
#         else:
#             tk.messagebox.showinfo("Image updated", "Something went wrong")
#
#     def __command_btn_upd_name(self):
#         if ProfileHandlerUdpName(self.entry_first_name.get(), self.entry_last_name.get()).execute():
#             tk.messagebox.showinfo("User name", "User name updated successful")
#         else:
#             tk.messagebox.showinfo("User name", "User name failed to update")
#
#     @staticmethod
#     def __command_btn_log_out():
#         ProfileLogOut().execute()
#         tk.messagebox.showinfo("Log out", "Log out successful")


class ProfileUi(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.image_label = None
        self.entry_first_name = None
        self.entry_last_name = None
        self.btn_update_name = None
        self.btn_img_upload = None
        self.btn_log_out = None

        self.__user_image_default = os.getcwd() + "\images" + "\default_img_user.png"
        self.__user_image_saved = os.getcwd() + "\images" + "\image_user.png"
        self.__create_ui()

    def __create_ui(self):
        self.create_image_label()
        self.__create_entry_name()
        self.__create_btn_img_upload()
        self.__create_btn_upd_name()
        self.__create_btn_log_out()

    # Creation of the user image
    def create_image_label(self):
        try:
            if not database_obj.user_name_login:
                self.__create_image_path_file(self.__user_image_default)
            else:
                self.__create_image_path_file(self.__user_image_saved)
        except OSError:
            tk.messagebox.showinfo("Upload Image Error", "Wrong image format")

    def __create_image_path_file(self, image_path):
        image = Image.open(image_path)
        image_resize = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image_resize)

        self.image_label = tk.Label(self, image=photo)
        self.image_label.image = photo
        self.image_label.grid(row=0, column=0)

    # Creation of entry
    def __create_entry_name(self):
        self.__create_entry_first_name()
        self.__create_entry_last_name()

    def __create_entry_first_name(self):
        self.entry_first_name = tk.Entry(self)
        self.entry_first_name.grid(row=1, column=0)

    def __create_entry_last_name(self):
        self.entry_last_name = tk.Entry(self)
        self.entry_last_name.grid(row=1, column=1)

    # Creation of buttons
    def __create_btn_img_upload(self):
        self.btn_img_upload = tk.Button(self, text="Upload Image", command=self.__command_img_upload)
        self.btn_img_upload.grid(row=0, column=1)

    def __create_btn_upd_name(self):
        self.btn_update_name = tk.Button(self, text="Update Name", command=self.__command_btn_upd_name)
        self.btn_update_name.grid(row=1, column=2)

    def __create_btn_log_out(self):
        self.btn_log_out = tk.Button(self, text="Log out", command=self.__command_btn_log_out)
        self.btn_log_out.grid(row=5, column=1)

    # Command of buttons
    @staticmethod
    def __command_img_upload():
        # Open windows explorer interface
        image_path = easygui.fileopenbox()

        # Execute update into db with new image
        if ProfileHandlerUpdImg(image_path).execute():
            tk.messagebox.showinfo("Image updated", "Image updated successful")
        else:
            tk.messagebox.showinfo("Image updated", "Something went wrong")

    def __command_btn_upd_name(self):
        if ProfileHandlerUdpName(self.entry_first_name.get(), self.entry_last_name.get()).execute():
            tk.messagebox.showinfo("User name", "User name updated successful")
        else:
            tk.messagebox.showinfo("User name", "User name failed to update")

    @staticmethod
    def __command_btn_log_out():
        ProfileLogOut().execute()
        tk.messagebox.showinfo("Log out", "Log out successful")
