import json


class TaskData:
    def __init__(self):
        self.type = None
        self.state = None
        self.points = 0

    def obj_to_dict(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    def dict_to_obj(self):
        return json.loads(self.obj_to_dict())
