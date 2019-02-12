from tkinter import messagebox

from firebase_database import database_obj
from tabs_dir.tab_controller_logic.tab_controller_logic import ControllerUiLogic
from tabs_dir.tab_handler.adapter_handler import AdaptHandler
from tabs_dir.tab_handler.tab_services import service_login
from tabs_dir.tab_upd_logic.tab_profile_upd_thread import ProfileUiUpdate
from images.spinner.spinner import Spinner
from global_instances import TABS_MAP_FRAMES
from tabs_dir.tabs_ui.login_thread import LoginThread
import global_instances


class LoginAdaptHandler(AdaptHandler):
    def __init__(self, login_info):
        self.__login_info = login_info

    def execute(self):

        login_thread = LoginThread(self.__login_info)
        global_instances.THREADS_DICT[LoginThread.THREAD_NAME] = login_thread

        login_thread.start()
        # spinner_thread = Spinner(self.__login_info)
        # spinner_thread.start()
        # TODO DISABLE ENTRYS ON LOG IN AND BTN

# ControllerUiLogic.disable_login_tab()
# ControllerUiLogic.enable_tabs_after_login()
        # if service_login.LoginService().login_user(self.__login_info):
        #     database_obj.user_name_login = self.__login_info.user_name.get()
        #
        #     # ControllerUiLogic.disable_login_tab()
        #     # ControllerUiLogic.enable_tabs_after_login()
        #
        #     messagebox.showinfo("Login", "Successful Login")
        #
        #     # TODO MOVE IN PROFILE TAB / ON TAB IS SELECTED
        #     ProfileUiUpdate().update_profile_ui()
        #
        # else:
        #     messagebox.showinfo("Login", "Incorrect username or password")

        # profile_thread = UiProfileUpdateThread()
        # profile_thread.start
