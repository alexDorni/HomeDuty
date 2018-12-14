# Pattern Part


class TaskAttr:
    def __init__(self, task_attr=None):
        self._task_attr = task_attr

    @property
    def task_name(self):
        print("Getting task name")
        return self._task_attr

    @task_name.setter
    def task_name(self, task_attr):
        if self._task_attr is None:
            raise ValueError("Error: task name is None")
        self._task_attr = task_attr

