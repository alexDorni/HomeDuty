from firebase_database.database_user_dao.user_info_dao import DatabaseUserInfoDao
from firebase_database import database_obj
from images.image_convert.image_converter import ImageConverter
from images.spinner.spinner import Spinner
from tabs_dir.tab_controller_logic.tab_enum import Tab

import global_instances


class ProfileUiUpdate:
    def __init__(self):
        # self.__spinner = Spinner()
        self.profile_obj = global_instances.TABS_MAP_FRAMES.get(Tab.Profile.name)

    def update_profile_ui(self):
        self.__update_first_name()
        self.__update_last_name()
        self.__update_image_label()

    def __update_first_name(self):
        first_name_string = DatabaseUserInfoDao.get_username_first_name(user_name=database_obj.user_name_login)
        self.profile_obj.entry_first_name.insert(0, first_name_string)

    def __update_last_name(self):
        last_name_string = DatabaseUserInfoDao.get_username_last_name(user_name=database_obj.user_name_login)
        self.profile_obj.entry_last_name.insert(0, last_name_string)

    def __update_image_label(self):
        img_string = DatabaseUserInfoDao.get_username_image(user_name=database_obj.user_name_login)
        # self.profile_obj.convert_bytes_to_img(img_string)
        ImageConverter().convert_bytes_to_img(img_string)
        self.profile_obj.create_image_label()
