import tkinter as tk
import os

from tabs_dir.tab_handler.login_adapt_handler import LoginAdaptHandler

# pip install pillow ( the new PIL )
from PIL import Image, ImageTk


class LoginUi:
    def __init__(self, master=None):
        self._master = master

        self.image_label = None
        self.user_name = None
        self.password_ins = None
        self.login_btn = None

        self.create_ui_login()

    def create_ui_login(self):
        self.__create_image()
        self.__create_username()
        self.__create_password()
        self.__create_login_btn()

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
        self.login_btn = tk.Button(self._master, text="Login", command=self.__command_login_btn)
        self.login_btn.grid(row=8, column=10)

    def __command_login_btn(self):
        LoginAdaptHandler(self).execute()

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
