from user_builder.user_info_builder import user_info_builder


class UserInfoDAO:
    def __init__(self, user_db=None, user_info_taped=None):
        # Current user info taped by him
        self.__user_info_taped = user_info_taped

        # Current user in database
        self.__user_db = user_db

        # User info collection
        self.__user_info = "User_info"

        # Current user info
        self.__username = "Username"
        self.__credentials = "Credentials"

        self.__history = "History"
        # History attributes
        self.__last_week_winner = None
        self.__winning_rounds = 0

    def creation_user_info(self):
        self.__creation_username()
        self.__creation_credentials()
        self.__creation_history()

    def __creation_username(self):
        # Create the username obj
        username_attr = user_info_builder.UserInfoBuilder().first_name(self.__user_info_taped.first_name).\
                                                            last_name(self.__user_info_taped.last_name).\
                                                            user_name(self.__user_info_taped.user_name).\
                                                            build()

        user_info_json = UserInfoDAO.__get_valid_json_for_user_info(username_attr)

        # Push username into db
        self.__user_db.collection(self.__user_info).document(self.__username).set(user_info_json)

    def __creation_credentials(self):
        # Create obj with crypt password
        user_credentials = user_info_builder.UserInfoBuilder().password(self.__user_info_taped.password).\
                                                               build()

        user_credentials_json = UserInfoDAO.__get_valid_json_for_user_credentials(user_credentials)

        # Push crypt password into db
        self.__user_db.collection(self.__user_info).document(self.__credentials).set(user_credentials_json)

    def __creation_history(self):
        # Create user history obj
        user_history = user_info_builder.UserInfoBuilder().last_week_winner(self.__last_week_winner).\
                                                           winning_rounds(self.__winning_rounds).\
                                                           build()

        user_history_json = UserInfoDAO.__get_valid_json_for_user_history(user_history)

        # Push user history into db
        self.__user_db.collection(self.__user_info).document(self.__history).set(user_history_json)

    @staticmethod
    def __get_valid_json_for_user_info(user_info):
        json = user_info.obj_to_dict()

        json.pop("last_week_winner")
        json.pop("password")
        json.pop("winning_rounds")

        return json

    @staticmethod
    def __get_valid_json_for_user_credentials(user_credentials):
        json = user_credentials.obj_to_dict()

        json.pop("first_name")
        json.pop("last_name")
        json.pop("last_week_winner")
        json.pop("winning_rounds")
        json.pop("user_name")

        return json

    @staticmethod
    def __get_valid_json_for_user_history(user_history):
        json = user_history.obj_to_dict()

        json.pop("first_name")
        json.pop("last_name")
        json.pop("last_week_winner")
        json.pop("password")
        json.pop("user_name")

        return json
