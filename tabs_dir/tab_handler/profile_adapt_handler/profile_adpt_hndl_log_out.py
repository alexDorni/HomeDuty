from tabs_dir.tab_handler.adapter_handler import AdaptHandler
from tabs_dir.tab_handler.tab_services.service_profile import ProfileService


class ProfileLogOut(AdaptHandler):

    def execute(self):
        ProfileService.update_user_log_out()
