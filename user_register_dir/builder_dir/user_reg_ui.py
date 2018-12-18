from user_register_dir.builder_dir import user_reg_builder as builder
from user_register_dir.builder_dir import user_regist_tasks as user_tasks

class RegUi:
    def __init__(self, email=None):
        self.email = email

    def register_firestore(self):
        user_builder = builder.UserRegBuilder()
        user_task = user_tasks.UserRegTasks()

        user_task.set_builder(user_builder)

