import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title = "Desktop Assistant"
        self.geometry("800x600")


    def run(self):
        self.mainloop()
if __name__ == "__main__":
    app = App()
    app.run()