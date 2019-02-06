from firebase_database.database_user_dao.user_info_dao import DatabaseUserInfoDao
from images.image_convert.image_converter import ImageConverter
from user_builder.user_info_builder import user_info_builder
import os


class UserInfoService:
    def __init__(self, user_info_taped=None):
        # Current user info taped by him
        self.__user_info_taped = user_info_taped

        # Current user name
        self.__user_info__username = self.__user_info_taped.user_name

        # History attributes
        self.__last_week_winner = None
        self.__winning_rounds = 0

        # Username image attribute must be converted to bytes
        self.image_default_path = os.getcwd() + "\images" + "\default_img_user.png"

    def creation_user_info(self):
        self.__creation_username()
        self.__creation_credentials()
        self.__creation_history()

    def __creation_username(self):
        # Create the image bytes
        image_bytes = ImageConverter.convert_img_to_bytes(self.image_default_path)

        # Decode bytes to string for serializing json
        image_bytes = image_bytes.decode('utf-8')

        # Create the username obj
        username_attr = user_info_builder.UserInfoBuilder().\
            first_name(self.__user_info_taped.first_name).\
            last_name(self.__user_info_taped.last_name).\
            image(image_bytes).\
            build()

        user_info_json = UserInfoService.__get_valid_json_for_user_info(username_attr)

        # Push username into db
        DatabaseUserInfoDao.set_username(self.__user_info__username, user_info_json)

    def __creation_credentials(self):
        # Create obj with crypt password
        user_credentials = user_info_builder.UserInfoBuilder().password(self.__user_info_taped.password).\
                                                               build()

        user_credentials_json = UserInfoService.__get_valid_json_for_user_credentials(user_credentials)

        # Push crypt password into db
        DatabaseUserInfoDao.set_credentials(self.__user_info__username, user_credentials_json)

    def __creation_history(self):
        # Create user history obj
        user_history = user_info_builder.UserInfoBuilder().last_week_winner(self.__last_week_winner).\
                                                           winning_rounds(self.__winning_rounds).\
                                                           build()

        user_history_json = UserInfoService.__get_valid_json_for_user_history(user_history)

        # Push user history into db
        DatabaseUserInfoDao.set_history(self.__user_info__username, user_history_json)

    @staticmethod
    def __get_valid_json_for_user_info(user_info):
        json = user_info.obj_to_dict()

        json.pop("user_name")
        json.pop("last_week_winner")
        json.pop("password")
        json.pop("winning_rounds")

        return json

    @staticmethod
    def __get_valid_json_for_user_credentials(user_credentials):
        json = user_credentials.obj_to_dict()

        json.pop("user_name")
        json.pop("first_name")
        json.pop("last_name")
        json.pop("image")
        json.pop("last_week_winner")
        json.pop("winning_rounds")

        return json

    @staticmethod
    def __get_valid_json_for_user_history(user_history):
        json = user_history.obj_to_dict()

        json.pop("user_name")
        json.pop("first_name")
        json.pop("last_name")
        json.pop("image")
        json.pop("last_week_winner")
        json.pop("password")

        return json
