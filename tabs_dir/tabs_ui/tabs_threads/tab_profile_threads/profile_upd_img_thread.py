import threading

from tabs_dir.tab_handler.tab_services.service_profile import ProfileService
from tabs_dir.tab_upd_logic.tab_profile_update import ProfileUiUpdate


class ProfileUpdateImgThread(threading.Thread):
    THREAD_NAME = "Profile"

    def __init__(self, profile_info, image_path):
        threading.Thread.__init__(self)
        self.__profile_info = profile_info
        self.__image_path = image_path

    def run(self):
        is_success = ProfileService().update_img_into_db(self.__image_path)

        if is_success:
            ProfileUiUpdate().update_image_label()

        self.__profile_info.on_update_image_done(is_success)
