

class RegService:

    @staticmethod
    def __validate(register_info):
        # Validate fields from Register Tab
        # Return a bool
        if register_info.user_name.get() is '' and register_info.password_ins.get() is '':
            if register_info.password_ret.get() is '':
                return False

        return True

    # The validate param is the validate function
    @staticmethod
    def reg_user(register_info):
        if RegService.__validate(register_info):
            # Register user into database
            # Return (true) a message that the user is successful register
            return True
        else:
            return False
