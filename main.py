import ui_app as ui
import firestore_database


def main():
    root = ui.tk.Tk()
    app = ui.InterfaceDuty(root)
    fd = firestore_database.FireData()
    fd.push_data({u'cevaaa': u'altceva'})
    fd.get_data()
    app.mainloop()


if __name__ == "__main__":
    main()
