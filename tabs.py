from enum import Enum, unique


# make the enums unique
@unique
class Tab(Enum):
    LWW = "Last Week Winners"
    PROFILE = "Your Profile"
    TW = "This week"

    def get_name(self):
        return self.name

    def get_val(self):
        return self.value
