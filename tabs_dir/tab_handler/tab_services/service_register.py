from user_builder.user_tasks_builder import task_data_creation_dao
from user_builder.user_info_builder import user_info_creation_dao, user_info_builder
from firebase_database import database_obj
from firebase_database import password_crypt


class RegService:

    @staticmethod
    def __validate(register_info):

        # Return a bool if all the entry's are filled
        return (register_info.user_name.get()
                and register_info.first_name.get()
                and register_info.last_name.get()
                and register_info.password_ins.get()
                and register_info.password_ret.get())

    @staticmethod
    def reg_user(register_info):
        if RegService.__validate(register_info):
            # Register user into database

            db = database_obj.db_users.document()

            # Creation of user info
            user_info_obj = RegService.__user_info(register_info)
            user_info_collection = user_info_creation_dao.UserInfoDAO(user_db=db, user_info_taped=user_info_obj)
            user_info_collection.creation_user_info()

            # Creation of user tasks
            task_collection = task_data_creation_dao.TaskCreationDAO(user_db=db)
            task_collection.creation_task()
            return True
        else:
            return False

    @staticmethod
    def __user_info(register_info):
        # Crypt password
        crypt_password = password_crypt.hash_password(register_info.password_ins.get())

        # Create user info object
        user_info_obj = user_info_builder.UserInfoBuilder().user_name(register_info.user_name.get()).\
                                                            first_name(register_info.first_name.get()).\
                                                            last_name(register_info.last_name.get()).\
                                                            password(crypt_password).\
                                                            build()

        return user_info_obj
