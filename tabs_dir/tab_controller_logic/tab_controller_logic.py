from tabs_dir.tab_controller_logic import tab_enum
from images.spinner.spinner import Spinner
import global_instances


class ControllerUiLogic:

    # Disabled tabs
    @staticmethod
    def disable_tabs_before_login():
        global_instances.TABS.tab_control.tab(tab_enum.Tab.Profile.value, state="disabled")
        global_instances.TABS.tab_control.tab(tab_enum.Tab.LastWeek.value, state="disabled")
        global_instances.TABS.tab_control.tab(tab_enum.Tab.ThisWeek.value, state="disabled")

    @staticmethod
    def disable_login_tab():
        global_instances.TABS.tab_control.tab(tab_enum.Tab.Login.value, state="disabled")

    @staticmethod
    def disable_register_tab():
        global_instances.TABS.tab_control.tab(tab_enum.Tab.Register.value, state="disabled")

    # Enabled tabs
    @staticmethod
    def enable_tabs_after_login():
        global_instances.TABS.tab_control.tab(tab_enum.Tab.Profile.value, state="normal")
        global_instances.TABS.tab_control.tab(tab_enum.Tab.LastWeek.value, state="normal")
        global_instances.TABS.tab_control.tab(tab_enum.Tab.ThisWeek.value, state="normal")
        global_instances.TABS.tab_control.select(tab_enum.Tab.Profile.value)
        # global_instances.TABS.tab_frame_dic.get(tab_enum.Tab.Profile.name).spinner.animate(0)

    @staticmethod
    def enable_login_tab():
        global_instances.TABS.tab_control.tab(tab_enum.Tab.Login.value, state="normal")
        ControllerUiLogic.disable_tabs_before_login()

    # Selected tabs
    @staticmethod
    def select_login_tab():
        global_instances.TABS.tab_control.select(tab_enum.Tab.Login.value)

