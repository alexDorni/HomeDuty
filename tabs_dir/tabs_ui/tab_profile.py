import tkinter as tk
import easygui
import os
import base64

# pip install pillow ( the new PIL )
from PIL import Image, ImageTk
from tabs_dir.tab_handler.profile_adapt_handler.profile_adpt_hndl_log_out import ProfileLogOut
from tabs_dir.tab_handler.profile_adapt_handler.profile_adpt_hndl_upd_img import ProfileHandlerUpdImg
from tabs_dir.tab_handler.profile_adapt_handler.profile_adpt_hndl_upd_name import ProfileHandlerUdpName
from firebase_database import database_obj


class ProfileUi:
    def __init__(self, master=None):
        self.__master = master
        self.image_label = None
        self.entry_first_name = None
        self.entry_last_name = None
        self.btn_update_name = None
        self.btn_img_upload = None
        self.btn_log_out = None

        self.__user_image_path = os.getcwd() + "\images" + "\image_user.gif"
        self.__user_image_default = os.getcwd() + "\images" + "\default_img_user.png"
        self.__create_ui()

    def __create_ui(self):
        self.__create_image_label()
        self.__create_entry_name()
        self.__create_btn_img_upload()
        self.__create_btn_upd_name()
        self.__create_btn_log_out()

    # Creation of the user image
    def __create_image_label(self):
        try:
            # Check if user is already in db
            if database_obj.user_name_login:
                self.__create_image_path_file(self.__user_image_path)
            else:
                self.__create_image_path_file(self.__user_image_default)
        except OSError:
            tk.messagebox.showinfo("Upload Image Error", "Wrong image format")

    def __create_image_path_file(self, image_path):
        image = Image.open(image_path)
        image_resize = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image_resize)

        self.image_label = tk.Label(self.__master, image=photo)
        self.image_label.image = photo
        self.image_label.grid(row=0, column=0)

    def __convert_bytes_to_img(self, bytes_string):

        with open(self.__user_image_path, "wb") as f:
            f.write(bytes_string)

    def __resize_img_resolution(self, image_path):
        image = Image.open(image_path)
        image.save(self.__user_image_path, dpi=(600, 600))

    @staticmethod
    def __convert_img_to_bytes(image_path):

        with open(image_path, "rb") as image_file:
            image_bytes = base64.b64encode(image_file.read())

        return image_bytes

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
        # Open windows explorer interface
        image_path = easygui.fileopenbox()

        self.__resize_img_resolution(image_path)
        # Create the image label
        self.__create_image_label()

        # Convert image to bytes
        image_bytes = ProfileUi.__convert_img_to_bytes(self.__user_image_path)

        # Execute update into db with new image
        if ProfileHandlerUpdImg(image_bytes).execute():
            tk.messagebox.showinfo("Image updated", "Image updated successful")
        else:
            tk.messagebox.showinfo("Image updated", "Something went wrong")

    def __command_btn_upd_name(self):
        ProfileHandlerUdpName(self.entry_first_name.get(), self.entry_last_name.get()).execute()

    @staticmethod
    def __command_btn_log_out():
        ProfileLogOut().execute()
        tk.messagebox.showinfo("Log out", "Log out successful")
