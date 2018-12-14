from user_register_dir.builder_dir import user_data


class UserRegTasks:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_builder(self):
        data_pattern = user_data.DataPattern()

        # Create the type task
        _type = self.__builder.get_task_type()
        data_pattern.set_type(_type)

        # Create the name task
        _name = self.__builder.get_task_name()
        data_pattern.set_name(_name)

        # Create the attr task
        _attr = self.__builder.get_task_attr()
        data_pattern.set_attr(_attr)

        # Return the object task pattern
        return data_pattern
