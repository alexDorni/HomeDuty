from firebase_database.database_obj import db_users
from firebase_database.database_obj import user_name_login

# TODO modify all data in the project with DatabaseUserInfoDao


class DatabaseUserInfoDao:
    """
    Database structure

    DB_users(coll) -> [user_name_login(doc) -> [Tasks_coll(coll) -> [Tasks_name -> {points: integer,
                                                                                   state: bool,
                                                                                   type: Daily/Weekly}
                                                                    ],
                                                User_info        -> [Credentials -> {password: encrypted_string},
                                                                     History     -> {winning_rounds: integer},
                                                                     Username    -> {first_name: string,
                                                                                     image: bytes_string,
                                                                                     last_name: string
                                                                     ],
                                                {alive_document: true}
                                                ]
                       ]

    """

    # Collections
    user_info_collection = "User_info"

    # Documents
    username_doc = "Username"
    user_history_doc = "History"
    user_credentials_doc = "Credentials"

    @staticmethod
    def update_username(dict_info={}):
        """
        Update the fields from firecloud database:

        first_name
        last_name
        image

        """
        db_users.document(user_name_login).\
                 collection(DatabaseUserInfoDao.user_info_collection).\
                 document(DatabaseUserInfoDao.username_doc).\
                 update(dict_info)

    @staticmethod
    def update_history(dict_info={}):
        """
        Update the fields from firecloud database:

        winning_rounds

        """
        db_users.document(user_name_login).\
                 collection(DatabaseUserInfoDao.user_info_collection).\
                 document(DatabaseUserInfoDao.user_history_doc).\
                 update(dict_info)

    @staticmethod
    def update_credentials(dict_info={}):
        """
            Update the fields from firecloud database:

            password

        """
        db_users.document(user_name_login).\
                 collection(DatabaseUserInfoDao.user_info_collection).\
                 document(DatabaseUserInfoDao.user_credentials_doc).\
                 update(dict_info)

    @staticmethod
    def set_username(dict_info={}):
        """
        Set the fields from firecloud database:

        first_name
        last_name
        image

        """
        db_users.document(user_name_login). \
            collection(DatabaseUserInfoDao.user_info_collection). \
            document(DatabaseUserInfoDao.username_doc). \
            set(dict_info)

    @staticmethod
    def set_history(dict_info={}):
        """
        Set the fields from firecloud database:

        winning_rounds

        """
        db_users.document(user_name_login).\
            collection(DatabaseUserInfoDao.user_info_collection).\
            document(DatabaseUserInfoDao.user_history_doc).\
            set(dict_info)

    @staticmethod
    def set_credentials(dict_info={}):
        """
        Set the fields from firecloud database:

        password

        """
        db_users.document(user_name_login).\
            collection(DatabaseUserInfoDao.user_info_collection).\
            document(DatabaseUserInfoDao.user_credentials_doc).\
            set(dict_info)

