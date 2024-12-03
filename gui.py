from tkinter import Tk, Label


class Gui:

    title_text = "wire_cacl 0.0"

    def __init__(self):
        self._window = Tk()
        self._window.title(self.title_text)
        self._window.geometry("500x300")

        self.p_label = Label(text="Мощность")
        self.p_label.grid(columnspan=1, rowspan=2, column=0, row=0)

        self.u_label = Label(text="Напряжение питания")
        self.u_label.grid(columnspan=1, rowspan=2, column=0, row=2)

        self.cos_label = Label(text="Характеристика нагрузки cos(fi)")
        self.cos_label.grid(columnspan=1, rowspan=2, column=0, row=5)

        self.length_label = Label(text="Длина кабеля")
        self.length_label.grid(columnspan=1, rowspan=2, column=0, row=8)

        self._window.mainloop()
