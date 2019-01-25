from user_builder.user_tasks_builder import task_data_creation_dao
from user_builder.user_info_builder import user_info_creation_dao, user_info_builder
from firebase_database import database_obj
from firebase_database import password_crypt


class RegService:

    @staticmethod
    def __validate_fields(register_info):
        # Return a bool if all the entry's are filled
        return (register_info.user_name.get()
                and register_info.first_name.get()
                and register_info.last_name.get()
                and register_info.password_ins.get()
                and register_info.password_ret.get())

    @staticmethod
    def __check_logic_fields(register_info):
        if RegService.__validate_fields(register_info):
            return register_info.password_ins.get() == register_info.password_ret.get()

    @staticmethod
    def reg_user(register_info):
        if RegService.__check_logic_fields(register_info):
            _user_name = register_info.user_name.get()

            # Check if user is already in database
            if RegService.__check_username_exists(_user_name):
                return False

            # Creation of a new user document
            db = database_obj.db_users.document(_user_name)

            # Creation of user info
            user_info_obj = RegService.__user_info(register_info)
            user_info_collection = user_info_creation_dao.UserInfoDAO(user_db=db, user_info_taped=user_info_obj)
            user_info_collection.creation_user_info()

            # Creation of user tasks
            task_collection = task_data_creation_dao.TaskCreationDAO(user_db=db)
            task_collection.creation_task()

            # Set for current user an existence flag
            db.set({"alive_document": True})
            return True
        else:
            return False

    @staticmethod
    def __check_username_exists(username):
        # Document(username) exists only if it has a .set({})
        return database_obj.db_users.document(username).get().exists

    @staticmethod
    def __user_info(register_info):
        # Crypt password
        crypt_password = password_crypt.crypt_password(register_info.password_ins.get())

        # Create user info object
        user_info_obj = user_info_builder.UserInfoBuilder().first_name(register_info.first_name.get()).\
                                                            last_name(register_info.last_name.get()).\
                                                            password(crypt_password).\
                                                            build()

        return user_info_obj
