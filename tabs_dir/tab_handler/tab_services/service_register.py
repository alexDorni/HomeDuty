

class RegService:

    @staticmethod
    def __validate(register_info):
        # Validate fields from Register Tab
        # Return a bool
        print(register_info.user_name.get())
        pass

    # The validate param is the validate function
    @staticmethod
    def reg_user(register_info):
        if RegService.__validate(register_info):
            # Register user into database
            # Return (true) a message that the user is successful register
            pass
        else:
            # Return false
            pass
