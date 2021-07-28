import tkinter as tk
import math


CANVAS_WIDTH = 90
CANVAS_HEIGHT = 80
TILE_EASY = "tile.easy"
TILE_DIFF = "tile.diff"
TILE_TOWN = "tile.town"
TILE_CITY = "tile.city"
TILE_MCITY = "tile.city.major"
TILE_IMAGES = {}

mouse_x = None
mouse_y = None


def mouse_update(event):
    global mouse_x, mouse_y
    mouse_x = event.x
    mouse_y = event.y


class App:
    def __init__(self, width, height):
        self.__root = tk.Tk()
        self.__canvas = tk.Canvas(self.__root, width=width * 3, height=height * 3)
        self.__canvas.bind('<Enter>', mouse_update)
        self.__canvas.bind('<Motion>', mouse_update)
        self.__canvas.pack()
        TILE_IMAGES.update({TILE_EASY: tk.PhotoImage(file="../img/easy.png")})
        TILE_IMAGES.update({TILE_DIFF: tk.PhotoImage(file="../img/diff.png")})
        TILE_IMAGES.update({TILE_TOWN: tk.PhotoImage(file="../img/town.png")})
        TILE_IMAGES.update({TILE_CITY: tk.PhotoImage(file="../img/city.png")})
        TILE_IMAGES.update({TILE_MCITY: tk.PhotoImage(file="../img/mcity.png")})

    def get_canvas(self):
        return self.__canvas

    def run_mainloop(self):
        self.__root.mainloop()


class Tile:
    def __init__(self, canvas, pos_x, pos_y):
        self.__canvas = canvas
        photo_image = TILE_IMAGES.get(TILE_EASY)
        self.__image_id = self.__canvas.create_image(pos_x, pos_y, image=photo_image)
        self.__canvas.tag_bind(self.__image_id, '<Button-1>', lambda e: self.on_click())
        self.__image_width = photo_image.width()
        self.__image_height = photo_image.height()
        self.__radius_bound = self.__image_height / 2
        self.__is_selected = False

    def inbound(self):
        global mouse_x, mouse_y
        pos = self.__canvas.coords(self.__image_id)
        centre_x, centre_y = pos[0], pos[1]
        res_x = centre_x - mouse_x
        res_y = centre_y - mouse_y
        dis = math.sqrt((res_x ** 2) + (res_y ** 2))

        return dis <= self.__radius_bound

    def on_click(self, value=None):
        if not self.inbound():
            return

        if value is None:
            value = self.__is_selected

        easy = TILE_IMAGES.get(TILE_EASY)
        diff = TILE_IMAGES.get(TILE_DIFF)

        self.__canvas.itemconfig(self.__image_id, image=(easy if value else diff))
        self.__is_selected = not value

        print(self.__image_id, "at", self.__canvas.coords(self.__image_id), "is selected:", self.__is_selected)


if __name__ == '__main__':
    app = App(CANVAS_WIDTH, CANVAS_HEIGHT)
    tile = Tile(app.get_canvas(), CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)

    app.run_mainloop()
