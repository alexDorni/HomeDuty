from firebase_database.database_obj import db_users
from firebase_database.database_obj import user_name_login


class ProfileDAO:
    def __init__(self):

        # DB(users) -> user(doc) -> User_info(col) -> Username(doc) -> {first_name, img, last_name}
        self.user_info_db = u'User_info'
        self.username_db = u'Username'

        # User name info json
        print(user_name_login)
        self.db_username = db_users.document(user_name_login).\
                                    collection(self.user_info_db).\
                                    document(self.username_db)

        self.json_obj_db = self.__get_username_data()

    # Get username json
    def __get_username_data(self):
        return self.db_username.get()

    def get_first_name(self):
        return self.json_obj_db.to_dict()["first_name"]

    def get_last_name(self):
        return self.json_obj_db.to_dict()["last_name"]

    def get_img_bytes(self):
        return self.json_obj_db.to_dict()["image"]
