from firebase_database.database_user_dao.user_info_dao import DatabaseUserInfoDao
from firebase_database import database_obj
from firebase_database import password_crypt


# TODO LOG IN THREAD REQUEST ON DB
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

                # Return hashed password from database into password_from_db
                password_from_db = DatabaseUserInfoDao.get_user_password(user_name=username_field)

                # Return a bool
                return password_crypt.verify_password(password_from_db, password_field)
            else:
                return False

    @staticmethod
    def __check_username_exists(username):
        # Document(username) exists only if it has a .set({})
        check_username = DatabaseUserInfoDao.get_user_name(username)

        return check_username.exists
