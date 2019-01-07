from tabs_dir.tab_handler.adapter_handler import AdaptHandler
from tabs_dir.tab_handler.tab_services.service_register import RegService


class RegAdaptHandler(AdaptHandler):
    def __init__(self, register_info):
        self.__register_info = register_info

    def execute(self):
        return RegService.reg_user(self.__register_info)

