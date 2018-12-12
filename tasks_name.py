
class TaskName:
    def __init__(self, string_name):
        self.task_name = string_name

    @property
    def task_name(self):
        print("Getting task name")
        return self.task_name

    @task_name.setter
    def task_name(self, val):
        self.task_name = val
