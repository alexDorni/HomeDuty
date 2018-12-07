import register_tab


class Login:
    def __init__(self, master=None):
        self._master = master


class Register(register_tab.RegUi):
    def __init__(self, master=None):
        self._master = master
        register_tab.RegUi(master=self._master)


class Recoverpass:
    def __init__(self, master=None):
        self._master = master


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
