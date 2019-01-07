from user_builder.user_info_builder import user_info_data as user_info


class UserInfoBuilder:
    def __init__(self):
        self.user_info = user_info.UserInfo()

    def user_name(self, user_name):
        self.user_info.user_name = user_name
        return self

    def first_name(self, first_name):
        self.user_info.first_name = first_name
        return self

    def last_name(self, last_name):
        self.user_info.last_name = last_name
        return self

    def password(self, password):
        self.user_info.password = password
        return self

    def last_week_winner(self, last_week_winner):
        self.user_info.last_week_winner = last_week_winner
        return self

    def winning_rounds(self, winning_rounds):
        self.user_info.winning_rounds = winning_rounds
        return self

    def build(self):
        return self.user_info
