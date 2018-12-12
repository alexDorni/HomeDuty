

class TaskType:
    def __init__(self, _type=None):
        self.element_task(_type)

    @property
    def element_task(self):
        print("Getting the element task")
        return self.element_task

    @element_task.setter
    def element_task(self, val):
        self.element_task = val
