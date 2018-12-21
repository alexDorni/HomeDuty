from tabs_dir.tab_handler.adapter_handler import AdaptHandler
from tabs_dir.tab_handler.tab_services.service_register import RegService


class RegAdaptHandler(AdaptHandler):
    def __init__(self, obj):
        self.handler = AdaptHandler(obj)

    def execute(self, register_info):
        if RegService.reg_user(register_info):
            print("User successful register")
        else:
            print("User register error")
