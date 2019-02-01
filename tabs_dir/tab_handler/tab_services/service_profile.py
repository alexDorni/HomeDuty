from tabs_dir.tab_controller_logic.tab_controller_logic import ControllerUiLogic
from firebase_database import database_obj
from firebase_database.database_obj import db_users


class ServiceProfile:
    @staticmethod
    def update_img_into_db(img_bytes=b''):
        # DB(users) -> user(doc) -> User_info(col) -> Username(doc) -> set {img : img_bytes}
        db_users.document(database_obj.user_name_login).collection("User_info").document("Username").update({"img": img_bytes})
        return True

    @staticmethod
    def update_user_name(first_name, last_name):
        # DB(users) -> user(doc) -> User_info(col) -> Username(doc) -> update {img : img_bytes} (set overwrites)
        _first_name = "first_name"
        _last_name = "last_name"
        db_users.document(database_obj.user_name_login).collection("User_info").\
                                                        document("Username").\
                                                        update({_first_name: first_name, _last_name: last_name})

    @staticmethod
    def update_user_log_out():
        database_obj.user_name_login = None
        ControllerUiLogic.enable_login_tab()
        ControllerUiLogic.select_login_tab()
