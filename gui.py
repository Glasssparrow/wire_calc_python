from tkinter import Tk


class Gui:

    title_text = "wire_cacl 0.0"

    def __init__(self):
        self._window = Tk()
        self._window.title(self.title_text)
        self._window.geometry("500x300")
        self._window.mainloop()
