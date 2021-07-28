import tkinter as tk
import constants as const
from objects import Tile


class App:
    def __init__(self, width, height):
        self.__root = tk.Tk()
        self.__canvas = tk.Canvas(self.__root, width=width, height=height)
        self.__canvas.bind('<Enter>', const.mouse_update)
        self.__canvas.bind('<Motion>', const.mouse_update)
        self.__canvas.pack()
        const.TILE_IMAGES.update({const.TILE_NONE: tk.PhotoImage(file="img/none.png")})
        const.TILE_IMAGES.update({const.TILE_EASY: tk.PhotoImage(file="img/easy.png")})
        const.TILE_IMAGES.update({const.TILE_DIFF: tk.PhotoImage(file="img/diff.png")})
        const.TILE_IMAGES.update({const.TILE_TOWN: tk.PhotoImage(file="img/town.png")})
        const.TILE_IMAGES.update({const.TILE_CITY: tk.PhotoImage(file="img/city.png")})
        const.TILE_IMAGES.update({const.TILE_MCITY: tk.PhotoImage(file="img/mcity.png")})
        const.TILE_IMAGES.update({const.TILE_SELECT: tk.PhotoImage(file="img/select.png")})
        const.TILE_IMAGES.update({const.TILE_UNSELECT: tk.PhotoImage(file="img/unselect.png")})

    def get_canvas(self):
        return self.__canvas

    def run_mainloop(self):
        self.__root.mainloop()


if __name__ == '__main__':
    app = App(const.CANVAS_WIDTH, const.CANVAS_HEIGHT)
    Tile(app.get_canvas(), 50, 50, const.TILE_NONE)
    Tile(app.get_canvas(), 150, 50, const.TILE_EASY)
    Tile(app.get_canvas(), 250, 50, const.TILE_DIFF)
    Tile(app.get_canvas(), 50, 150, const.TILE_TOWN)
    Tile(app.get_canvas(), 150, 150, const.TILE_CITY)
    Tile(app.get_canvas(), 250, 150, const.TILE_MCITY)

    Tile(app.get_canvas(), 250, 250, const.TILE_EASY)

    app.run_mainloop()
