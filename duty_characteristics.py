

class CharacterDuty:
    def __init__(self, _date, points, state):
        self._date  = _date
        self.points = points
        self.state  = state

    @property
    def _date(self):
        print("Getting date value")
        return self._date

    @_date.setter
    def _date(self, val):
        self._date = val

    @property
    def points(self):
        print("Getting points")
        return self.points

    @points.setter
    def points(self, val):
        self.points = val

    @property
    def state(self):
        print("Getting state")
        return self.state

    @state.setter
    def state(self, val):
        self.state = val
