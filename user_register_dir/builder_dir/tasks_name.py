# Pattern Part


class TaskName:
    def __init__(self, task_name=None):
        self._task_name = task_name

    @property
    def task_name(self):
        print("Getting task name")
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        if self._task_name is None:
            raise ValueError("Error: task name is None")
        self._task_name = task_name
