# Pattern Part


class TaskType:
    def __init__(self, task_type=None):
        self._task_type = task_type

    @property
    def task_type(self):
        print("Getting task type")
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        if task_type is None:
            raise ValueError("Error: task type is None")
        self._task_type = task_type
