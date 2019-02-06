from firebase_database.database_user_dao.user_info_dao import DatabaseUserInfoDao
from firebase_database.database_obj import user_name_login
import threading


class UiProfileUpdateThread(threading.Thread):
    def __init__(self, profile_obj=None):
        threading.Thread.__init__(self)
        self.profile_obj = profile_obj

    def update_first_name(self):
        first_name_string = DatabaseUserInfoDao.get_username_first_name(user_name=user_name_login)
        self.profile_obj.entry_first_name.set(first_name_string)

    def update_last_name(self):
        last_name_string = DatabaseUserInfoDao.get_username_last_name(user_name=user_name_login)
        self.profile_obj.entry_last_name.set(last_name_string)

    def update_image_label(self):
        img_string = DatabaseUserInfoDao.get_username_image(user_name=user_name_login)
        self.profile_obj.convert_bytes_to_img(img_string)


    # TODO buttons lock
    # TODO start thread
