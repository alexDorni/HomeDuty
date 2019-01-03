from user_tasks_builder import task_data_creation


class RegService:

    @staticmethod
    def __validate(register_info):
        if register_info.user_name.get() is '':
            return False
        if register_info.password_ins.get() is '':
            return False
        if register_info.password_ret.get() is '':
            return False
        return True

    @staticmethod
    def reg_user(register_info):
        if RegService.__validate(register_info):
            # Register user into database
            # # Return (true) a message that the user is successful register
            # db_data = builder.TaskDataBuilder().name(register_info.user_name)
            # database.FireData.db
            task_data_creation.TaskCreation().task_creation()
            return True
        else:
            return False
