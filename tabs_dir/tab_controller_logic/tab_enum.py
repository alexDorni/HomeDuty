from enum import Enum, unique


@unique
class Tab(Enum):
    Login = 0
    Profile = 1
    LastWeek = 2
    ThisWeek = 3
    Register = 4
