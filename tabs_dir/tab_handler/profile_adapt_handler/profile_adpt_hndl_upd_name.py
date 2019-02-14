import global_instances
from tabs_dir.tab_handler.adapter_handler import AdaptHandler
from tabs_dir.tabs_ui.tabs_threads.tab_profile_threads.profile_upd_user_thread import ProfileUpdUserThread


class ProfileHandlerUdpName(AdaptHandler):
    def __init__(self, profile_info):
        self.__profile_info = profile_info

    def execute(self):
        profile_username_thread = ProfileUpdUserThread(self.__profile_info)

        global_instances.THREADS_DICT[ProfileUpdUserThread.THREAD_NAME] = profile_username_thread

        profile_username_thread.start()


