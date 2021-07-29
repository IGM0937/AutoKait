import tkinter as tk
from constants import *
from objects import Tile


class App:
    def __init__(self, width, height):
        self.__root = tk.Tk()
        self.__canvas = tk.Canvas(self.__root, width=width, height=height)
        self.__canvas.bind('<Enter>', mouse_update)
        self.__canvas.bind('<Motion>', mouse_update)
        self.__canvas.pack()
        TILE_IMAGES.update({TILE_NONE: tk.PhotoImage(file="img/none.png")})
        TILE_IMAGES.update({TILE_EASY: tk.PhotoImage(file="img/easy.png")})
        TILE_IMAGES.update({TILE_DIFF: tk.PhotoImage(file="img/diff.png")})
        TILE_IMAGES.update({TILE_TOWN: tk.PhotoImage(file="img/town.png")})
        TILE_IMAGES.update({TILE_CITY: tk.PhotoImage(file="img/city.png")})
        TILE_IMAGES.update({TILE_MCITY: tk.PhotoImage(file="img/mcity.png")})
        TILE_IMAGES.update({TILE_SELECT: tk.PhotoImage(file="img/select.png")})
        TILE_IMAGES.update({TILE_UNSELECT: tk.PhotoImage(file="img/unselect.png")})

    def get_canvas(self):
        return self.__canvas

    def run_mainloop(self):
        self.__root.mainloop()


if __name__ == '__main__':
    # app = App(CANVAS_WIDTH, CANVAS_HEIGHT)
    #
    # locations = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10',
    #              'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10',
    #              'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10',
    #              'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10',
    #              'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10',
    #              'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10',
    #              'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'g10',
    #              'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10']
    #
    # for location in locations:
    #     Tile(app.get_canvas(), location, TILE_EASY)
    #
    # app.run_mainloop()

    root = tk.Tk()
    frame = tk.Frame(root, width=300, height=300)
    frame.pack(expand=True, fill=tk.BOTH)  # .grid(row=0,column=0)
    canvas = tk.Canvas(frame, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 500, 500))
    canvas.bind_all()
    hbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
    hbar.pack(side=tk.BOTTOM, fill=tk.X)
    hbar.config(command=canvas.xview)
    vbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
    vbar.pack(side=tk.RIGHT, fill=tk.Y)
    vbar.config(command=canvas.yview)
    canvas.config(width=300, height=300)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    root.mainloop()
