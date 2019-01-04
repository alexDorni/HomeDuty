from enum import Enum, unique


@unique
class Tab(Enum):
    Login = "Login"
    Register = "Register"
    RecoverPass = "RecoverPass"
    Profile = "Profile"
    LastWeek = "LastWeek"
    ThisWeek = "ThisWeek"
