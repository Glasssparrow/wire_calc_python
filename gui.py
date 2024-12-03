from tkinter import Tk, Label, Radiobutton, IntVar, Text, END, Button
from calculation import calculate


class Gui:

    title_text = "wire_cacl 0.5"

    @staticmethod
    def _check_input_from_user(user_input):
        return user_input

    def calculate(self):
        P = self.p_text.get(1.0)
        P = self._check_input_from_user(P)
        U = self.u_text.get(1.0)
        U = self._check_input_from_user(U)
        cos_fi = self.cos_text.get(1.0)
        cos_fi = self._check_input_from_user(cos_fi)
        L = self.length_text.get(1.0)
        L = self._check_input_from_user(L)
        phases_radiobutton = self.u_radiobutton_position.get()
        if phases_radiobutton == 0:
            phases = 3
        elif phases_radiobutton == 1:
            phases = 1
        else:
            raise Exception(f"Случилось что-то странное.")
        load_type_radiobutton = self.cos_radiobutton_position.get()
        if load_type_radiobutton == 0:
            load_type = "реактивная"
        elif load_type_radiobutton == 1:
            load_type = "активная"
        else:
            raise Exception(f"Случилось что-то странное.")
        length_radiobutton = self.length_radiobutton_position.get()
        if length_radiobutton == 0:
            cable_type = "медь"
        elif length_radiobutton == 1:
            cable_type = "алюминий"
        else:
            raise Exception(f"Случилось что-то странное.")

        calculate(
            P=P, U=U, cos_fi=cos_fi, L=L,
            phases=phases, load_type=load_type, cable_type=cable_type,
        )

    def u_radiobutton_command(self):
        print(self.u_text.get(1.0, END))

    def cos_radiobutton_command(self):
        print(self.cos_text.get(1.0, END))

    def length_radiobutton_command(self):
        print(self.length_text.get(1.0, END))

    def __init__(self):
        self._window = Tk()
        self._window.title(self.title_text)
        self._window.geometry("500x300")

        # Исходные данные по мощности
        self.p_label = Label(text="Мощность нагрузки, кВт")
        self.p_label.grid(columnspan=2, rowspan=1, column=0, row=0, sticky="W")
        self.p_text = Text(height=1, width=10)
        self.p_text.grid(columnspan=1, rowspan=1, column=1, row=1, sticky="W")

        # Исходные данные по напряжению
        self.u_label = Label(text="Напряжение питания, В")
        self.u_label.grid(columnspan=2, rowspan=1, column=0, row=2, sticky="W")
        self.u_radiobutton_position = IntVar(value=0)
        self.u_radiobutton1 = Radiobutton(
            text="Трехфазная сеть",
            variable=self.u_radiobutton_position,
            value=0, command=self.u_radiobutton_command)
        self.u_radiobutton2 = Radiobutton(
            text="Однофазная сеть",
            variable=self.u_radiobutton_position,
            value=1, command=self.u_radiobutton_command)
        self.u_radiobutton1.grid(column=0, row=3, sticky="W")
        self.u_radiobutton2.grid(column=0, row=4, sticky="W")
        self.u_text = Text(height=1, width=10)
        self.u_text.insert(1.0, "380")
        self.u_text.grid(columnspan=1, rowspan=2, column=1, row=3, sticky="W")

        # Исходные данные по характеру нагрузки
        self.cos_label = Label(text="Характеристика нагрузки, cos(fi)")
        self.cos_label.grid(columnspan=2, rowspan=1, column=0, row=5, sticky="W")
        self.cos_radiobutton_position = IntVar(value=0)
        self.cos_radiobutton1 = Radiobutton(
            text="Реактивная",
            variable=self.cos_radiobutton_position,
            value=0, command=self.cos_radiobutton_command)
        self.cos_radiobutton2 = Radiobutton(
            text="Активная",
            variable=self.cos_radiobutton_position,
            value=1, command=self.cos_radiobutton_command)
        self.cos_radiobutton1.grid(column=0, row=6, sticky="W")
        self.cos_radiobutton2.grid(column=0, row=7, sticky="W")
        self.cos_text = Text(height=1, width=10)
        self.cos_text.insert(1.0, "0.8")
        self.cos_text.grid(columnspan=1, rowspan=2, column=1, row=6, sticky="W")

        # Исходные данные по кабелю
        self.length_label = Label(text="Длина кабеля, м")
        self.length_label.grid(columnspan=2, rowspan=1, column=0, row=8, sticky="W")
        self.length_radiobutton_position = IntVar(value=0)
        self.length_radiobutton1 = Radiobutton(
            text="Медный",
            variable=self.length_radiobutton_position,
            value=0, command=self.length_radiobutton_command)
        self.length_radiobutton2 = Radiobutton(
            text="Алюминиевый",
            variable=self.length_radiobutton_position,
            value=1, command=self.length_radiobutton_command)
        self.length_radiobutton1.grid(column=0, row=9, sticky="W")
        self.length_radiobutton2.grid(column=0, row=10, sticky="W")
        self.length_text = Text(height=1, width=10)
        self.length_text.insert(1.0, "10")
        self.length_text.grid(columnspan=1, rowspan=2, column=1, row=9, sticky="W")

        # Результат
        self.load_current_label = Label(text="Ток нагрузки, А")
        self.load_current_label.grid(columnspan=1, rowspan=1, column=3, row=0, sticky="W")
        self.load_current_text = Text(height=1, width=10)
        self.load_current_text.grid(columnspan=1, rowspan=1, column=4, row=0, sticky="W")

        self.max_cable_current_label = Label(text="Максимальный ток кабеля, А")
        self.max_cable_current_label.grid(columnspan=1, rowspan=1, column=3, row=1, sticky="W")
        self.max_cable_current_text = Text(height=1, width=10)
        self.max_cable_current_text.grid(columnspan=1, rowspan=1, column=4, row=1, sticky="W")

        self.s_label = Label(text="Сечение жил кабеля, мм2")
        self.s_label.grid(columnspan=1, rowspan=1, column=3, row=2, sticky="W")
        self.s_text = Text(height=1, width=10)
        self.s_text.grid(columnspan=1, rowspan=1, column=4, row=2, sticky="W")

        self.current_breaker_label = Label(text="Номинальный ток автомата, А")
        self.current_breaker_label.grid(columnspan=1, rowspan=1, column=3, row=3, sticky="W")
        self.current_breaker_text = Text(height=1, width=10)
        self.current_breaker_text.grid(columnspan=1, rowspan=1, column=4, row=3, sticky="W")

        self.load_u_label = Label(text="Напряжение на нагрузке")
        self.load_u_label.grid(columnspan=1, rowspan=1, column=3, row=4, sticky="W")
        self.load_u_text = Text(height=1, width=10)
        self.load_u_text.grid(columnspan=1, rowspan=1, column=4, row=4, sticky="W")

        # Button
        self.button = Button(
                self._window, text="Выполнить расчет",
                width= 36,
                command=self.calculate,
                bg="green",
            )
        self.button.grid(columnspan=2, rowspan=1, column=3, row=5, sticky="W")

        self._window.mainloop()
