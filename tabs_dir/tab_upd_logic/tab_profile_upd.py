from tabs_dir.tab_upd_logic import user_profile_dao
import threading


class ProfileUpdate(threading.Thread):
    def __init__(self, profile_obj=None):
        threading.Thread.__init__(self)
        self.profile_obj = profile_obj
        self.db_user_profile = user_profile_dao.ProfileDAO()

    def update_first_name(self):
        first_name_string = self.db_user_profile.get_first_name()
        self.profile_obj.entry_first_name.set(first_name_string)

    def update_last_name(self):
        last_name_string = self.db_user_profile.get_last_name()
        self.profile_obj.entry_last_name.set(last_name_string)

    def update_image_label(self):
        pass

    # TODO buttons lock
    # TODO start thread
