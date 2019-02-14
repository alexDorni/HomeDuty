from tabs_dir.tab_handler.adapter_handler import AdaptHandler
from tabs_dir.tabs_ui.tabs_threads.tab_login_threads.login_thread import LoginThread
import global_instances


class LoginAdaptHandler(AdaptHandler):
    def __init__(self, login_info):
        self.__login_info = login_info

    def execute(self):

        login_thread = LoginThread(self.__login_info)
        global_instances.THREADS_DICT[LoginThread.THREAD_NAME] = login_thread

        login_thread.start()
