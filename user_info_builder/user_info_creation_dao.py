from user_info_builder import user_info_builder


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

    def user_info_creation(self):
        self.__username_creation()
        self.__credentials_creation()
        self.__history_creation()

    def __username_creation(self):
        username_attr = user_info_builder.UserInfoBuilder().first_name(self.__user_info_taped.first_name).\
                                                            last_name(self.__user_info_taped.last_name).\
                                                            user_name(self.__user_info_taped.user_name).\
                                                            build()

        user_info_json = UserInfoDAO.__get_valid_json_for_user_info(username_attr)
        self.__user_db.collection(self.__user_info).document(self.__username).set(user_info_json)

    def __credentials_creation(self):
        user_credentials = user_info_builder.UserInfoBuilder().password_crypt(self.__user_info_taped.password_crypt).\
                                                                build()

        user_credentials_json = UserInfoDAO.__get_valid_json_for_user_credentials(user_credentials)
        self.__user_db.collection(self.__user_info).document(self.__credentials).set(user_credentials_json)

    def __history_creation(self):
        user_history = user_info_builder.UserInfoBuilder().last_week_winner(self.__last_week_winner).\
                                                            winning_rounds(self.__winning_rounds).\
                                                            build()
        user_history_json = UserInfoDAO.__get_valid_json_for_user_history(user_history)
        self.__user_db.collection(self.__user_info).document(self.__history).set(user_history_json)

    @staticmethod
    def __get_valid_json_for_user_info(user_info):
        json = user_info.obj_to_dict()

        json.pop("last_week_winner")
        json.pop("password_crypt")
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
        json.pop("password_crypt")
        json.pop("user_name")

        return json
