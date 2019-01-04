from user_tasks_builder import task_data_builder as builder
from user_tasks_builder import task_data_daily_enum as daily_enum
from user_tasks_builder import task_data_weekly_enum as weekly_enum
from firebase_database import database_obj


class TaskCreation:
    def __init__(self, id_token=None):
        self.__task_daily_name = ["Garbage_disposal", "Washing_dishes", "Broom_cleaning"]

        self.__task_weekly_name = ["Mop_wash", "Vacuum_cleaning", "Microwave_cleaning", "Refrigerator_cleaning",
                                   "Big_bath_cleaning", "Small_bath_cleaning", "Room_cleaning", "Balcony_cleaning"]

        self.__task_daily_type = "Daily"
        self.__task_weekly_type = "Weekly"
        self.__task_state = "False"
        self.__id_token = id_token

    def task_creation(self):
        self.task_daily_creation()
        self.task_weekly_creation()

    def task_daily_creation(self):
        for task_daily in self.__task_daily_name:
            for enum_task_daily in daily_enum.TaskDaily:
                if enum_task_daily.name is task_daily:
                    task = builder.TaskDataBuilder().user_id(self.__id_token).\
                                            type(self.__task_daily_type).\
                                            state(self.__task_state).\
                                            points(enum_task_daily.value).\
                                            build()
            database_obj.db_tasks.document(task_daily).set(task.obj_to_dict())

    def task_weekly_creation(self):
        for task_weekly in self.__task_weekly_type:
            for enum_task_weekly in weekly_enum.TaskWeekly:
                if enum_task_weekly is task_weekly:
                    task = builder.TaskDataBuilder().user_id(self.__id_token). \
                        type(self.__task_weekly_type). \
                        state(self.__task_state). \
                        points(enum_task_weekly.value).\
                        build()
            database_obj.db_tasks.document(task_weekly).set(task.obj_to_dict())

