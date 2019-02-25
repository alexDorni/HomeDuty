from tabs_dir.tabs_ui import tab_register, tab_login, tab_profile, tab_this_week
from tabs_dir.tab_controller_logic.tab_enum import Tab


class TabFactory:
    TAB_MAP = {
        Tab.Login.name: tab_login.LoginUi,
        Tab.Profile.name: tab_profile.ProfileUi,
        Tab.Register.name: tab_register.RegUi,
        Tab.ThisWeek.name: tab_this_week.ThisWeek
    }

    @staticmethod
    def create(tab_name=None, master_frame=None):
        class_ref = TabFactory.TAB_MAP.get(tab_name)
        if class_ref:
            return class_ref(master_frame)

        return None

