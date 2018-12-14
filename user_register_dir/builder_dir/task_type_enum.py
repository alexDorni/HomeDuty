from enum import Enum, unique


@unique
class TaskTypeEnum(Enum):
    DAILY = "Daily Tasks"
    WEEKLY = "Weekly Tasks"
    CHALLENGE = "Challenge Tasks"
