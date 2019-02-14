import threading

from tabs_dir.tab_handler.tab_services.service_profile import ProfileService
from tabs_dir.tab_upd_logic.tab_profile_update import ProfileUiUpdate


class ProfileUpdUserThread(threading.Thread):
    THREAD_NAME = "Profile"

    def __init__(self, profile_info):
        threading.Thread.__init__(self)
        self.__profile_info = profile_info
        self.__first_name = self.__profile_info.entry_first_name.get()
        self.__last_name = self.__profile_info.entry_last_name.get()

    def run(self):
        is_success = ProfileService.update_user_name(self.__first_name, self.__last_name)

        if is_success:
            ProfileUiUpdate().update_user_name()

        self.__profile_info.on_update_username_done(is_success)
