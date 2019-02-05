from tabs_dir.tab_controller_logic.tab_controller_logic import ControllerUiLogic
from images.image_convert.image_converter import ImageConverter
from firebase_database import database_obj
from firebase_database.database_obj import db_users


# TODO PRofileService
class ServiceProfile:
    @staticmethod
    def __convert_image_to_bytes(image_path=None):
        image_converter = ImageConverter()

        image_converter.resize_img_resolution(image_path)

        return image_converter.convert_img_to_bytes_()

    @staticmethod
    def update_img_into_db(image_path=None):
        img_bytes = ServiceProfile().__convert_image_to_bytes(image_path)

        # DB(users) -> user(doc) -> User_info(col) -> Username(doc) -> set {image : img_bytes}
        db_users.document(database_obj.user_name_login).collection("User_info").\
                                                        document("Username").\
                                                        update({"image": img_bytes})

        return True

    @staticmethod
    def update_user_name(first_name, last_name):
        # DB(users) -> user(doc) -> User_info(col) -> Username(doc) -> update {img : img_bytes} (set overwrites)
        _first_name = "first_name"
        _last_name = "last_name"
        db_users.document(database_obj.user_name_login).collection("User_info").\
                                                        document("Username").\
                                                        update({_first_name: first_name, _last_name: last_name})
        return True

    @staticmethod
    def update_user_log_out():
        database_obj.user_name_login = None
        ControllerUiLogic.enable_login_tab()
        ControllerUiLogic.select_login_tab()
