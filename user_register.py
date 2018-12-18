
class UserRegister:
    def __init__(self, email):
        try:
            self.email = email
        except ValueError:
            print("Invalid email")

