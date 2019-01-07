from firebase_database import database_obj


class LoginService:
    @staticmethod
    def __validate(login_info):
        return (login_info.email_ins.get() and
                login_info.password_ins.get())

    @staticmethod
    def login_user(login_info):
        if LoginService().__validate(login_info):
            db = database_obj.db_users.get()
            for doc in db:
                print(doc.id, doc)

            return True
        else:
            return False
