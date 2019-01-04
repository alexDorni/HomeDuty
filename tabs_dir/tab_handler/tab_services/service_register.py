from user_tasks_builder import task_data_creation_dao
from user_info_builder import user_info_creation_dao
from firebase_database import database_obj
from user_info_builder import user_info_builder


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
            # # Return (true) a message that the user is successful register
            # db_data = builder.TaskDataBuilder().name(register_info.user_name)
            # database.FireData.db
            db = database_obj.db_users.document()

            # User info creation
            user_info_obj = RegService.__user_info(register_info)
            user_info_collection = user_info_creation_dao.UserInfoDAO(user_db=db, user_info_taped=user_info_obj)
            user_info_collection.user_info_creation()

            # Tasks collection creation
            task_collection = task_data_creation_dao.TaskCreationDAO(user_db=db)
            task_collection.task_creation()
            return True
        else:
            return False

    @staticmethod
    def __user_info(register_info):
        # TODO password crypto
        user_info_obj = user_info_builder.UserInfoBuilder().user_name(register_info.user_name.get()).\
                                                            first_name(register_info.first_name.get()).\
                                                            last_name(register_info.last_name.get()).\
                                                            password_crypt(register_info.password_ins.get()).\
                                                            build()

        return user_info_obj
