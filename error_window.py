from tkinter import  Tk, Label

class ErrorGui:

    title_text = "Error message box"

    def __init__(self, message_tuple):
        # Оформление окна
        self._window = Tk()
        self._window.title(self.title_text)
        self._window.geometry("300x100")

        self._window.mainloop()
