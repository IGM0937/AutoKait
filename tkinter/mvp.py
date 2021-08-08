import random
import tkinter as tk
from constants import *
from objects import Tile


def add_train():
    """
    Added for testing purposes
    """
    train_type = random.choice([TRAIN_BLUE, TRAIN_YELLOW, TRAIN_PURPLE, TRAIN_ORANGE, TRAIN_RED])
    for tile_location, tile in LOCATION_MAP.items():
        if tile.is_selected() is True:
            tile.add_train(train_type)
            tile.is_selected(False)


def add_special_interest():
    """
    Added for testing purposes
    """
    for tile_location, tile in LOCATION_MAP.items():
        if tile.is_selected() is True:
            tile.add_special_interest(SI_BLACK)
            tile.is_selected(False)


def toggle_location_names():
    """
    Added for testing purposes
    """
    for tile_location, tile in LOCATION_MAP.items():
        tile.show_location_name(not tile.show_location_name())


class App:
    def __init__(self, app_width, app_height):
        self.__root = tk.Tk()
        self.__hbar = tk.Scrollbar(self.__root, orient=tk.HORIZONTAL)
        self.__vbar = tk.Scrollbar(self.__root, orient=tk.VERTICAL)
        self.__canvas = tk.Canvas(self.__root, width=app_width, height=app_height,
                                  yscrollcommand=self.__vbar.set, xscrollcommand=self.__hbar.set,
                                  scrollregion=(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT))
        self.__hbar['command'] = self.__canvas.xview
        self.__vbar['command'] = self.__canvas.yview

        self.__canvas.bind('<Enter>', on_mouse_update)
        self.__canvas.bind('<Motion>', on_mouse_update)
        self.__canvas.bind('<Button-3>', on_mouse_drag_press)
        self.__canvas.bind('<ButtonRelease-3>', on_mouse_drag_release)
        self.__canvas.bind('<MouseWheel>', on_mouse_vertical_update)
        self.__canvas.bind('<Shift-MouseWheel>', on_mouse_horizontal_update)
        self.__canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.__hbar.grid(column=0, row=1, sticky=(tk.W, tk.E))
        self.__vbar.grid(column=1, row=0, sticky=(tk.N, tk.S))
        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_rowconfigure(0, weight=1)

        TILE_IMAGES.update({TILE_NONE: tk.PhotoImage(file="img/tile_none.png")})
        TILE_IMAGES.update({TILE_EASY: tk.PhotoImage(file="img/tile_easy.png")})
        TILE_IMAGES.update({TILE_DIFF: tk.PhotoImage(file="img/tile_diff.png")})
        TILE_IMAGES.update({TILE_TOWN: tk.PhotoImage(file="img/tile_town.png")})
        TILE_IMAGES.update({TILE_CITY: tk.PhotoImage(file="img/tile_city.png")})
        TILE_IMAGES.update({TILE_MCITY: tk.PhotoImage(file="img/tile_mcity.png")})
        TILE_IMAGES.update({TILE_SELECT: tk.PhotoImage(file="img/tile_select.png")})
        TILE_IMAGES.update({TILE_UNSELECT: tk.PhotoImage(file="img/tile_unselect.png")})
        TRAIN_IMAGES.update({TRAIN_BLUE: tk.PhotoImage(file="img/train_blue.png")})
        TRAIN_IMAGES.update({TRAIN_ORANGE: tk.PhotoImage(file="img/train_orange.png")})
        TRAIN_IMAGES.update({TRAIN_PURPLE: tk.PhotoImage(file="img/train_purple.png")})
        TRAIN_IMAGES.update({TRAIN_RED: tk.PhotoImage(file="img/train_red.png")})
        TRAIN_IMAGES.update({TRAIN_YELLOW: tk.PhotoImage(file="img/train_yellow.png")})
        SI_IMAGES.update({SI_BLACK: tk.PhotoImage(file="img/si_black.png")})
        SI_IMAGES.update({SI_WHITE: tk.PhotoImage(file="img/si_white.png")})
        SI_IMAGES.update({SI_PINK: tk.PhotoImage(file="img/si_pink.png")})

    def get_canvas(self):
        return self.__canvas

    def get_root(self):
        return self.__root


if __name__ == '__main__':
    app = App(APP_WIDTH, APP_HEIGHT)

    # Tile(app.get_canvas(), 'a1', TILE_EASY)
    # Tile(app.get_canvas(), 'a2', TILE_DIFF)
    # b2 = Tile(app.get_canvas(), 'b2', TILE_EASY)

    locations = {'a1': TILE_NONE, 'b1': TILE_NONE, 'c1': TILE_NONE, 'd1': TILE_NONE, 'e1': TILE_DIFF,
                 'f1': TILE_DIFF, 'g1': TILE_DIFF, 'h1': TILE_EASY, 'i1': TILE_NONE, 'j1': TILE_NONE,
                 'k1': TILE_NONE, 'l1': TILE_EASY, 'm1': TILE_EASY, 'n1': TILE_TOWN, 'o1': TILE_DIFF,
                 'p1': TILE_NONE}

    locations.update({'a2': TILE_NONE, 'b2': TILE_NONE, 'c2': TILE_NONE, 'd2': TILE_NONE, 'e2': TILE_EASY,
                      'f2': TILE_TOWN, 'g2': TILE_EASY, 'h2': TILE_EASY, 'i2': TILE_EASY, 'j2': TILE_NONE,
                      'k2': TILE_EASY, 'l2': TILE_EASY, 'm2': TILE_DIFF, 'n2': TILE_DIFF, 'o2': TILE_DIFF,
                      'p2': TILE_DIFF})

    locations.update({'a3': TILE_NONE, 'b3': TILE_NONE, 'c3': TILE_NONE, 'd3': TILE_NONE, 'e3': TILE_DIFF,
                      'f3': TILE_EASY, 'g3': TILE_EASY, 'h3': TILE_MCITY, 'i3': TILE_NONE, 'j3': TILE_EASY,
                      'k3': TILE_TOWN, 'l3': TILE_EASY, 'm3': TILE_DIFF, 'n3': TILE_DIFF, 'o3': TILE_EASY,
                      'p3': TILE_NONE})

    locations.update({'a4': TILE_NONE, 'b4': TILE_NONE, 'c4': TILE_NONE, 'd4': TILE_TOWN, 'e4': TILE_DIFF,
                      'f4': TILE_EASY, 'g4': TILE_EASY, 'h4': TILE_EASY, 'i4': TILE_EASY, 'j4': TILE_EASY,
                      'k4': TILE_EASY, 'l4': TILE_CITY, 'm4': TILE_EASY, 'n4': TILE_DIFF, 'o4': TILE_CITY,
                      'p4': TILE_NONE})

    locations.update({'a5': TILE_EASY, 'b5': TILE_EASY, 'c5': TILE_NONE, 'd5': TILE_EASY, 'e5': TILE_EASY,
                      'f5': TILE_EASY, 'g5': TILE_EASY, 'h5': TILE_EASY, 'i5': TILE_EASY, 'j5': TILE_EASY,
                      'k5': TILE_DIFF, 'l5': TILE_EASY, 'm5': TILE_EASY, 'n5': TILE_EASY, 'o5': TILE_NONE,
                      'p5': TILE_NONE})

    locations.update({'a6': TILE_DIFF, 'b6': TILE_DIFF, 'c6': TILE_EASY, 'd6': TILE_EASY, 'e6': TILE_EASY,
                      'f6': TILE_EASY, 'g6': TILE_EASY, 'h6': TILE_EASY, 'i6': TILE_EASY, 'j6': TILE_EASY,
                      'k6': TILE_DIFF, 'l6': TILE_EASY, 'm6': TILE_EASY, 'n6': TILE_EASY, 'o6': TILE_NONE,
                      'p6': TILE_NONE})

    locations.update({'a7': TILE_EASY, 'b7': TILE_DIFF, 'c7': TILE_EASY, 'd7': TILE_EASY, 'e7': TILE_EASY,
                      'f7': TILE_EASY, 'g7': TILE_EASY, 'h7': TILE_TOWN, 'i7': TILE_DIFF, 'j7': TILE_EASY,
                      'k7': TILE_EASY, 'l7': TILE_EASY, 'm7': TILE_DIFF, 'n7': TILE_NONE, 'o7': TILE_NONE,
                      'p7': TILE_NONE})

    locations.update({'a8': TILE_EASY, 'b8': TILE_CITY, 'c8': TILE_EASY, 'd8': TILE_DIFF, 'e8': TILE_EASY,
                      'f8': TILE_EASY, 'g8': TILE_EASY, 'h8': TILE_EASY, 'i8': TILE_EASY, 'j8': TILE_EASY,
                      'k8': TILE_EASY, 'l8': TILE_CITY, 'm8': TILE_EASY, 'n8': TILE_NONE, 'o8': TILE_NONE,
                      'p8': TILE_NONE})

    locations.update({'a9': TILE_DIFF, 'b9': TILE_DIFF, 'c9': TILE_DIFF, 'd9': TILE_TOWN, 'e9': TILE_EASY,
                      'f9': TILE_EASY, 'g9': TILE_EASY, 'h9': TILE_EASY, 'i9': TILE_EASY, 'j9': TILE_DIFF,
                      'k9': TILE_EASY, 'l9': TILE_TOWN, 'm9': TILE_CITY, 'n9': TILE_NONE, 'o9': TILE_NONE,
                      'p9': TILE_NONE})

    locations.update({'a10': TILE_EASY, 'b10': TILE_EASY, 'c10': TILE_EASY, 'd10': TILE_DIFF, 'e10': TILE_EASY,
                      'f10': TILE_EASY, 'g10': TILE_EASY, 'h10': TILE_EASY, 'i10': TILE_EASY, 'j10': TILE_EASY,
                      'k10': TILE_EASY, 'l10': TILE_DIFF, 'm10': TILE_EASY, 'n10': TILE_NONE, 'o10': TILE_NONE,
                      'p10': TILE_NONE})

    locations.update({'a11': TILE_EASY, 'b11': TILE_EASY, 'c11': TILE_EASY, 'd11': TILE_EASY, 'e11': TILE_EASY,
                      'f11': TILE_TOWN, 'g11': TILE_EASY, 'h11': TILE_MCITY, 'i11': TILE_DIFF, 'j11': TILE_DIFF,
                      'k11': TILE_EASY, 'l11': TILE_EASY, 'm11': TILE_NONE, 'n11': TILE_NONE, 'o11': TILE_NONE,
                      'p11': TILE_NONE})

    locations.update({'a12': TILE_DIFF, 'b12': TILE_DIFF, 'c12': TILE_MCITY, 'd12': TILE_DIFF, 'e12': TILE_DIFF,
                      'f12': TILE_NONE, 'g12': TILE_NONE, 'h12': TILE_NONE, 'i12': TILE_NONE, 'j12': TILE_TOWN,
                      'k12': TILE_TOWN, 'l12': TILE_NONE, 'm12': TILE_NONE, 'n12': TILE_NONE, 'o12': TILE_NONE,
                      'p12': TILE_NONE})

    for location, tile_type in locations.items():
        Tile(app.get_canvas(), location, tile_type)

    app.get_root().bind("<space>", lambda e: add_train())
    app.get_root().bind("<b>", lambda e: add_special_interest())
    app.get_root().bind("<l>", lambda e: toggle_location_names())

    app.get_root().mainloop()
