from firebase_database.database_obj import db_users
from firebase_database import database_obj


class DatabaseUserInfoDao:
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
    user_info_collection = "User_info"

    # Documents
    username_doc = "Username"
    user_history_doc = "History"
    user_credentials_doc = "Credentials"

    # Database update structure
    @staticmethod
    def update_structure():
        __db_users = db_users.document(database_obj.user_name_login).\
            collection(DatabaseUserInfoDao.user_info_collection)

        return __db_users

    # Database set structure
    @staticmethod
    def set_structure(user_name):
        __db_users = db_users.document(user_name).\
            collection(DatabaseUserInfoDao.user_info_collection)

        return __db_users

    # Database update methods
    @staticmethod
    def update_username(dict_info_user={}):
        """
        Update the fields from firecloud database:

        first_name: str
        last_name: str
        image: str_bytes

        """
        __db_users = DatabaseUserInfoDao.update_structure()

        __db_users.document(DatabaseUserInfoDao.username_doc).update(dict_info_user)

    @staticmethod
    def update_history(dict_info_user={}):
        """
        Update the fields from firecloud database:

        winning_rounds: integer

        """
        __db_users = DatabaseUserInfoDao.update_structure()

        __db_users.document(DatabaseUserInfoDao.user_history_doc).update(dict_info_user)

    @staticmethod
    def update_credentials(dict_info_user={}):
        """
            Update the fields from firecloud database:

            password: str

        """
        __db_users = DatabaseUserInfoDao.update_structure()

        __db_users.document(DatabaseUserInfoDao.user_credentials_doc).update(dict_info_user)

    # Database set methods
    @staticmethod
    def set_username(user_name, dict_info_user={}):
        """
        Set the fields from firecloud database:

        first_name: str
        last_name: str
        image: str_bytes

        """
        __db_users = DatabaseUserInfoDao.set_structure(user_name)

        __db_users.document(DatabaseUserInfoDao.username_doc).set(dict_info_user)

    @staticmethod
    def set_history(user_name, dict_info_user={}):
        """
        Set the fields from firecloud database:

        winning_rounds: integer

        """
        __db_users = DatabaseUserInfoDao.set_structure(user_name)

        __db_users.document(DatabaseUserInfoDao.user_history_doc).set(dict_info_user)

    @staticmethod
    def set_credentials(user_name, dict_info_user={}):
        """
        Set the fields from firecloud database:

        password: str

        """
        __db_users = DatabaseUserInfoDao.set_structure(user_name)

        __db_users.document(DatabaseUserInfoDao.user_credentials_doc).set(dict_info_user)

    # Database get methods
    @staticmethod
    def get_user_name(user_name):
        """
        Get the fields from firecloud database:

        user_name: str

        """
        # Returns the user document name
        return db_users.document(user_name).get()

    @staticmethod
    def get_user_password(user_name):
        """
        Get the fields from firecloud database:

        password: str

        """
        __db_users = DatabaseUserInfoDao.set_structure(user_name)

        # Returns a json {password: hash_string}
        password_json = __db_users.document(DatabaseUserInfoDao.user_credentials_doc).get()

        # Returns the value of the password key
        return password_json.to_dict()["password"]

    @staticmethod
    def get_user_winning_rounds(user_name):
        """
        Get the fields from firecloud database:

        winning_rounds: integer

        """
        __db_users = DatabaseUserInfoDao.set_structure(user_name)

        # Returns a json {winning_rounds: integer}
        winning_rounds_json = __db_users.document(DatabaseUserInfoDao.user_history_doc).get()

        # Returns the value of the winning_rounds key
        return winning_rounds_json.to_dict()["winning_rounds"]

    @staticmethod
    def __get_username_json(user_name):
        """
        Get the fields from firecloud database:

        {first_name: str,
        image: str_bytes,
        last_name: str}

        """
        __db_users = DatabaseUserInfoDao.set_structure(user_name)

        # Return a json {first_name: str, image: str_bytes, last_name: str}
        return __db_users.document(DatabaseUserInfoDao.username_doc).get()

    @staticmethod
    def get_username_first_name(user_name):
        """
        Get the fields from firecloud database:

        first_name: str

        """
        username_json = DatabaseUserInfoDao.__get_username_json(user_name)

        # Return the value of the first_name key
        return username_json.to_dict()["first_name"]

    @staticmethod
    def get_username_image(user_name):
        """
        Get the fields from firecloud database:

        image: str_bytes

        """
        username_json = DatabaseUserInfoDao.__get_username_json(user_name)

        # Return the value of the first_name key
        return username_json.to_dict()["image"]

    @staticmethod
    def get_username_last_name(user_name):
        """
        Get the fields from firecloud database:

        last_name: str

        """
        username_json = DatabaseUserInfoDao.__get_username_json(user_name)

        # Return the value of the first_name key
        return username_json.to_dict()["last_name"]
