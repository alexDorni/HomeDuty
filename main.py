import ui_app as ui
import user_register_dir.builder_dir.task_types as tt
import firestore_database as db


def main():
    root = ui.tk.Tk()
    app = ui.InterfaceDuty(root)
    d = db.FireData()
    lista = ("email", "daily", "tasks", "garbage")
    d.push_data(lista,)
    d.get_data()
    app.mainloop()


if __name__ == "__main__":
    main()
