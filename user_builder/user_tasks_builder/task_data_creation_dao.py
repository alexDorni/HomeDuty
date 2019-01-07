from user_builder.user_tasks_builder import task_data_builder as builder, task_data_daily_enum as daily_enum, \
    task_data_weekly_enum as weekly_enum


class TaskCreationDAO:
    def __init__(self, user_db=None):
        # Current user in database
        self.__user_db = user_db

        # Tasks collection in database
        self.__tasks_coll_db = "Tasks_coll"

        # Name of Tasks
        self.__task_daily_name = ["Garbage_disposal", "Washing_dishes", "Broom_cleaning"]

        self.__task_weekly_name = ["Mop_wash", "Vacuum_cleaning", "Microwave_cleaning", "Refrigerator_cleaning",
                                   "Big_bath_cleaning", "Small_bath_cleaning", "Room_cleaning", "Balcony_cleaning"]

        # Tasks attributes
        self.__task_daily_type = "Daily"
        self.__task_weekly_type = "Weekly"
        self.__task_state = "False"

    def creation_task(self):
        self.__creation_daily_task()
        self.__creation_weekly_task()

    def __creation_daily_task(self):
        for task_daily in self.__task_daily_name:
            for enum_task_daily in daily_enum.TaskDaily:

                # Check if Task Daily Enum is same with the __task_daily_name
                if enum_task_daily.name is task_daily:
                    task = builder.TaskDataBuilder().type(self.__task_daily_type).\
                                                    state(self.__task_state).\
                                                    points(enum_task_daily.value).\
                                                    build()

                    # Push into database
                    self.__user_db.collection(self.__tasks_coll_db).document(task_daily).set(task.obj_to_dict())

    def __creation_weekly_task(self):
        for task_weekly in self.__task_weekly_name:
            for enum_task_weekly in weekly_enum.TaskWeekly:

                # Check if Task Weekly Enum is same with the __task_weekly_name
                if enum_task_weekly.name is task_weekly:
                    task = builder.TaskDataBuilder().type(self.__task_weekly_type).\
                                                    state(self.__task_state).\
                                                    points(enum_task_weekly.value).\
                                                    build()

                    # Push into database
                    self.__user_db.collection(self.__tasks_coll_db).document(task_weekly).set(task.obj_to_dict())

