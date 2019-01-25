from firebase_database import database_obj
from firebase_database import password_crypt


class LoginService:
    @staticmethod
    def __validate(login_info):
        return (login_info.user_name.get() and
                login_info.password_ins.get())

    @staticmethod
    def login_user(login_info):
        if LoginService().__validate(login_info):
            return LoginService.__check_password(login_info)

    @staticmethod
    def __check_password(login_info):
        if LoginService.__validate(login_info):
            # User field
            username_field = login_info.user_name.get()

            if LoginService.__check_username_exists(username_field):

                # Password field
                password_field = login_info.password_ins.get()

                password_from_db = database_obj.db_users.document(username_field).\
                    collection("User_info").document("Credentials").get()

                # Key of the hashed password
                crypt_pass = password_from_db.to_dict()['password']

                # Return a bool
                return password_crypt.verify_password(crypt_pass, password_field)
            else:
                return False

    @staticmethod
    def __check_username_exists(username):
        # Document(username) exists only if it has a .set({})
        return database_obj.db_users.document(username).get().exists
