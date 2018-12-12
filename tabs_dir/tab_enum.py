from enum import Enum, unique


# make the enums unique
@unique
class Tab(Enum):
    Login = "Login"
    Register = "Register"
    RecoverPass = "RecoverPass"
    Profile = "Profile"
    LastWeek = "LastWeek"
    ThisWeek = "ThisWeek"

    def get_name(self):
        return self.name

    def get_val(self):
        return self.value
