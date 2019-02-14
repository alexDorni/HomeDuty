from enum import Enum, unique


@unique
class Tab(Enum):
    Login = 0
    Profile = 1
    ThisWeek = 2
    LastWeek = 3
    Register = 4
