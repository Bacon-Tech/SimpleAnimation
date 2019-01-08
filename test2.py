import tkinter as tk
from os import walk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.image_names = []
        self.index_tracker = 0
        self.location = 1
        self.canvas = tk.Canvas(self, width=2000)
        self.canvas.pack()
        for(dirpath, dirnames, filenames) in walk('./Flip/'):
            for name in filenames:
                self.image_names.append(tk.PhotoImage(file="{}{}".format(dirpath, name)))

        tk.Button(self, text='Start animation!', command=self.start_animation).pack()

    def start_animation(self):
        if self.location < 80:
            self.canvas.delete('all')
            if self.index_tracker < len(self.image_names):
                self.canvas.create_image(self.location * 10, 75, image=self.image_names[self.index_tracker])
                self.location += 1
                self.index_tracker += 1

            else:
                self.index_tracker = 0
                self.start_animation()


if __name__ == "__main__":
    App().mainloop()
