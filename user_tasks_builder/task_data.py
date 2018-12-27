import json


class TaskData:
    def __init__(self):
        self.name = u'None'
        self.user_id = u'None'
        self.type = u'None'
        self.state = u'None'
        self.points = 0

    def obj_to_dict(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    def dict_to_obj(self):
        return json.loads(self.obj_to_dict())
