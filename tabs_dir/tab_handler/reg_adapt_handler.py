from tabs_dir.tab_handler.adapter_handler import AdaptHandler
from tabs_dir.tab_handler.tab_services.service_register import RegService


class RegAdaptHandler(AdaptHandler):
    def __init__(self, register_info):
        self.register_info = register_info

    def execute(self):
        if RegService.reg_user(self.register_info):
            print("User successful register")
        else:
            print("User register error")
