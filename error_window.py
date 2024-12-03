from tkinter import  Tk, Label

class ErrorGui:

    title_text = "Error message box"

    def __init__(self, message_tuple):
        # Оформление окна
        self._window = Tk()
        self._window.title(self.title_text)
        self._window.geometry("300x100")

        self.message_text = ""
        for tuple_element in message_tuple:
            self.message_text += tuple_element

        # Сообщение об ошибке
        self._error_text = Label(text=self.message_text)
        self._error_text.grid(column=0, row=0)

        self._window.mainloop()
