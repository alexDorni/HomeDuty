import os
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence


class Spinner(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame().__init__(self, parent)
        self.controller = controller
        self.label_loading = tk.Label(self, text="Loading data... Please wait...")
        self.label_loading.place(relx=.5, rely=.1, anchor="center")
        self.btn_del_obj = tk.Button(self, text="DELETE", command=self.del_obj())
        self.btn_del_obj.place(relx=.9, rely=.5, anchor="center")
        self.__spinner_path_gif = os.getcwd() + "/images/spinner/spinner.gif"

        self.canvas = tk.Canvas(self.__master, width=350, height=350)
        self.canvas.place(relx=.5, rely=.5, anchor="center")
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                                    Image.open(self.__spinner_path_gif))]

        self.image = self.canvas.create_image(150, 150, image=self.sequence[0])
        self.animating = True
        self.animate(0)

    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        if not self.animating:
            return
        self.__master.after(33, lambda: self.animate((counter + 1) % len(self.sequence)))
        print("animate")
#
# import os
# import tkinter as tk
# from PIL import Image, ImageTk, ImageSequence
#
#
# class Spinner:
#     def __init__(self, master):
#         self.__master = master
#         self.label_loading = tk.Label(self.__master, text="Loading data... Please wait...")
#         self.label_loading.place(relx=.5, rely=.1, anchor="center")
#         self.__spinner_path_gif = os.getcwd() + "/images/spinner/spinner.gif"
#
#         self.canvas = tk.Canvas(self.__master, width=350, height=350)
#         self.canvas.place(relx=.5, rely=.5, anchor="center")
#         # self.canvas.pack()
#         self.sequence = [ImageTk.PhotoImage(img)
#                          for img in ImageSequence.Iterator(
#                                     Image.open(self.__spinner_path_gif))]
#
#         self.image = self.canvas.create_image(150, 150, image=self.sequence[0])
#         self.animating = True
#
#     def animate(self, counter):
#         self.canvas.itemconfig(self.image, image=self.sequence[counter])
#         if not self.animating:
#             return
#         self.__master.after(33, lambda: self.animate((counter + 1) % len(self.sequence)))
#         print("animate")
#
