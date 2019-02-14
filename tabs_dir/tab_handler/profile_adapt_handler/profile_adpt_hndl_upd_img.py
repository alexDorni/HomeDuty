import global_instances
from tabs_dir.tab_handler.adapter_handler import AdaptHandler
from tabs_dir.tabs_ui.tabs_threads.tab_profile_threads.profile_upd_img_thread import ProfileUpdateImgThread


class ProfileHandlerUpdImg(AdaptHandler):
    def __init__(self, profile_info, img_path):
        self.__profile_info = profile_info
        self.__img_path = img_path

    def execute(self):
        profile_update_img_thread = ProfileUpdateImgThread(self.__profile_info,
                                                           self.__img_path)

        global_instances.THREADS_DICT[ProfileUpdateImgThread.THREAD_NAME] = profile_update_img_thread

        profile_update_img_thread.start()


