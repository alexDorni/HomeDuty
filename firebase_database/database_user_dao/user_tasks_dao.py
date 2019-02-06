from firebase_database.database_obj import db_users
from firebase_database.database_obj import user_name_login


class UserTasksDao:
    """
        Database structure

        DB_users(coll) -> [user_name_login(doc) -> [Tasks_coll(coll) -> [Tasks_name(doc) -> {points: integer,
                                                                                       state: bool,
                                                                                       type: Daily/Weekly}
                                                                        ],
                                                    User_info(coll)  -> [Credentials(doc) -> {password: encrypted_str},
                                                                         History(doc)     -> {winning_rounds: integer},
                                                                         Username(doc)    -> {first_name: str,
                                                                                         image: bytes_str,
                                                                                         last_name: str
                                                                         ],
                                                    {alive_document: true}
                                                    ]
                           ]

    """

    # Collections
    user_tasks_coll = "Tasks_coll"

    # Database update structure
    @staticmethod
    def update_task_coll(task_name_doc, dict_info_task={}):

        __db_tasks = db_users.document(user_name_login).\
            collection(UserTasksDao.user_tasks_coll).\
            document(task_name_doc).\
            update(dict_info_task)

    # Database set structure
    @staticmethod
    def set_task_coll(user_name,
                      task_name_doc,
                      dict_info_task={}):

        __db_tasks = db_users.document(user_name).\
            collection(UserTasksDao.user_tasks_coll).\
            document(task_name_doc).\
            set(dict_info_task)
