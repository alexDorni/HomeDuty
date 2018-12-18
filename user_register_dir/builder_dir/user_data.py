# Skeleton assembler pattern


class DataPattern:
    def __init__(self):
        self._task_type = None
        self._task_name = None
        self._task_attr = None

    def set_type(self, task_type):
        self._task_type = task_type

    def set_name(self, task_name):
        self._task_name = task_name

    def set_attr(self, task_attr):
        self._task_attr = task_attr


