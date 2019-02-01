from tabs_dir.tab_handler.adapter_handler import AdaptHandler
from tabs_dir.tab_handler.tab_services.service_profile import ServiceProfile


class ProfileHandlerUpdImg(AdaptHandler):
    def __init__(self, img_bytes):
        self.__img_bytes = img_bytes

    def execute(self):
        return ServiceProfile.update_img_into_db(self.__img_bytes)
