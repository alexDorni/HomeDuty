import threading
import time

from firebase_database import database_obj
from tabs_dir.tab_handler.tab_services import service_login


class LoginThread(threading.Thread):
    THREAD_NAME = "Login"

    def __init__(self, login_info):
        threading.Thread.__init__(self)
        self.__login_info = login_info

    def run(self):
        is_successful = service_login.LoginService().login_user(self.__login_info)
        self.__login_info.on_login_done(is_successful)

