from tabs_dir.tab_controller_logic.tab_controller_logic import ControllerUiLogic
from images.image_convert.image_converter import ImageConverter
from firebase_database.database_user_dao.user_info_dao import DatabaseUserInfoDao
from firebase_database import database_obj

from tkinter import messagebox


class ProfileService:
    @staticmethod
    def update_img_into_db(image_path=None):
        img_bytes = ProfileService().__convert_image_to_bytes(image_path)
        if not img_bytes:
            return False

        # DB(users) -> user(doc) -> User_info(col) -> Username(doc) -> update {image : img_bytes}
        image_dict = {"image": img_bytes}
        DatabaseUserInfoDao.update_username(image_dict)

        return True

    @staticmethod
    def update_user_name(first_name, last_name):
        # DB(users) -> user(doc) -> User_info(col) -> Username(doc) -> update {img : img_bytes} (set overwrites)
        _first_name = "first_name"
        _last_name = "last_name"
        user_name_dict = {_first_name: first_name, _last_name: last_name}

        DatabaseUserInfoDao.update_username(user_name_dict)
        return True

    @staticmethod
    def update_user_log_out():
        database_obj.user_name_login = None
        ControllerUiLogic.enable_login_tab()
        ControllerUiLogic.select_login_tab()

    @staticmethod
    def __convert_image_to_bytes(image_path=None):
        image_converter = ImageConverter()
        is_converted = image_converter.resize_img_resolution(image_path)
        if is_converted:
            return image_converter.convert_img_to_bytes_()
        else:
            messagebox.showinfo("Image", "Wrong image format")
            return None
