from tabs_dir.tab_handler.adapter_handler import AdaptHandler
from tabs_dir.tab_handler.tab_services.service_profile import ServiceProfile


class ProfileLogOut(AdaptHandler):

    def execute(self):
        ServiceProfile.update_user_log_out()
