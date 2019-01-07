from tabs_dir.tab_handler.adapter_handler import AdaptHandler
from tabs_dir.tab_handler.tab_services import service_login


class LoginAdaptHandler(AdaptHandler):
    def __init__(self, login_info):
        self.__login_info = login_info

    def execute(self):
        return service_login.LoginService().login_user(self.__login_info)
