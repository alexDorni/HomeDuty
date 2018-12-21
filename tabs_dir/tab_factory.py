from tabs_dir import tab_recover, tab_register, tab_login


class Login:
    def __init__(self, master=None):
        self._master = master
        tab_login.LoginUi(master=self._master)


class Register:
    def __init__(self, master=None):
        self._master = master
        tab_register.RegUi(master=self._master)


class Recoverpass:
    def __init__(self, master=None):
        self._master = master
        tab_recover.RecoverUiPass(master=self._master)


class Profile:
    def __init__(self, master=None):
        self._master = master


class Lastweek:
    def __init__(self, master=None):
        self._master = master


class Thisweek:
    def __init__(self, master=None):
        self._master = master


class TabFactory(object):
    @staticmethod
    def create_tab(typ, **kwargs):
        target_class = typ.capitalize()
        return globals()[target_class](**kwargs)
