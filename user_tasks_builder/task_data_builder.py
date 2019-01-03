import user_tasks_builder.task_data as task_data


class TaskDataBuilder:
    def __init__(self):
        self.task = task_data.TaskData()

    def user_id(self, user_id):
        self.task.user_id = user_id
        return self

    def type(self, _type):
        self.task.type = _type
        return self

    def state(self, state):
        self.task.state = state
        return self

    def points(self, points):
        self.task.points = points
        return self

    def build(self):
        return self.task
