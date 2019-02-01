from tabs_dir.tabs_ui import tab_register, tab_login, tab_profile


class Login:
    def __init__(self, master=None):
        self._master = master
        tab_login.LoginUi(master=self._master)


class Register:
    def __init__(self, master=None):
        self._master = master
        tab_register.RegUi(master=self._master)


class Profile:
    def __init__(self, master=None):
        self._master = master
        tab_profile.ProfileUi(master=self._master)


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
