from tkinter import Tk, Label, Radiobutton, IntVar


class Gui:

    title_text = "wire_cacl 0.0"

    def u_radiobutton_command(self):
        pass

    def __init__(self):
        self._window = Tk()
        self._window.title(self.title_text)
        self._window.geometry("500x300")

        self.p_label = Label(text="Мощность нагрузки, кВт")
        self.p_label.grid(columnspan=1, rowspan=2, column=0, row=0)

        self.u_label = Label(text="Напряжение питания, В")
        self.u_label.grid(columnspan=1, rowspan=2, column=0, row=2)
        self.u_radiobutton_position = IntVar(value=0)
        self.u_radiobutton1 = Radiobutton(
            text="Трехфазная сеть",
            variable=self.u_radiobutton_position,
            value=0, command=self.u_radiobutton_command)
        self.u_radiobutton2 = Radiobutton(
            text="Однофазная сеть",
            variable=self.u_radiobutton_position,
            value=1, command=self.u_radiobutton_command)
        self.u_radiobutton1.grid(column=0, row=4)
        self.u_radiobutton2.grid(column=0, row=5)

        self.cos_label = Label(text="Характеристика нагрузки, cos(fi)")
        self.cos_label.grid(columnspan=1, rowspan=2, column=0, row=6)

        self.length_label = Label(text="Длина кабеля, м")
        self.length_label.grid(columnspan=1, rowspan=2, column=0, row=7)

        self._window.mainloop()
