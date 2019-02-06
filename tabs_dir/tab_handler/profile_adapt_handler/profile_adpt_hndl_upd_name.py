from tabs_dir.tab_handler.adapter_handler import AdaptHandler
from tabs_dir.tab_handler.tab_services.service_profile import ProfileService


class ProfileHandlerUdpName(AdaptHandler):
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def execute(self):
        return ProfileService.update_user_name(self.__first_name, self.__last_name)
