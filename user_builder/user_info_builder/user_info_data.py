import json


class UserInfo:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.image = None
        self.password = None
        self.last_week_winner = None
        self.winning_rounds = None

    def obj_to_dict(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    def dict_to_obj(self):
        return json.loads(self.obj_to_dict())
