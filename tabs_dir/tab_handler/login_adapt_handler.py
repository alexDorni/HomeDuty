from tkinter import messagebox

from firebase_database import database_obj
from tabs_dir.tab_controller_logic.tab_controller_logic import ControllerUiLogic
from tabs_dir.tab_handler.adapter_handler import AdaptHandler
from tabs_dir.tab_handler.tab_services import service_login


class LoginAdaptHandler(AdaptHandler):
    def __init__(self, login_info):
        self.__login_info = login_info

    def execute(self):
        if service_login.LoginService().login_user(self.__login_info):
            database_obj.user_name_login = self.__login_info.user_name.get()

            ControllerUiLogic.disable_login_tab()
            ControllerUiLogic.enable_tabs_after_login()

            messagebox.showinfo("Login", "Successful Login")

        else:
            messagebox.showinfo("Login", "Incorrect username or password")

        # # TODO start thread when tab is selected
        # TODO DAO DATA BASE
        # profile_thread = UiProfileUpdateThread()
        # profile_thread.start


