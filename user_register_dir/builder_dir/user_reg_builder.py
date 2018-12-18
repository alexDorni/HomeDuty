from user_register_dir.builder_dir import task_types, builder_database as builder, tasks_attr, tasks_name
from user_register_dir.builder_dir import task_type_enum as type_enum


# User get pattern
class UserRegBuilder(builder.Builder):

    def __init__(self, task_name=None, task_attr=None):
        self.__task_type = type_enum.TaskTypeEnum()
        self.__task_name = task_name
        self.__task_attr = task_attr

    def get_task_type(self):
        task_type = task_types.TaskType()
        task_type._task_type = self.__task_type
        return task_type

    def get_task_name(self):
        task_name = tasks_name.TaskName()
        task_name._task_name = self.__task_name
        return tasks_name

    def get_task_attr(self):
        task_attr = tasks_attr.TaskAttr()
        task_attr._task_attr = self.__task_attr
        return task_attr
