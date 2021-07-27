import tkinter as tk
import math


TILE_EASY = "tile.easy"
TILE_DIFF = "tile.diff"
TILE_TOWN = "tile.town"
TILE_CITY = "tile.city"
TILE_MCITY = "tile.city.major"

TILE_IMAGES = {
    TILE_EASY: "easy.png",
    TILE_DIFF: "diff.png",
    TILE_TOWN: "town.png",
    TILE_CITY: "city.png",
    TILE_MCITY: "mcity.png",
}

mouse_x = None
mouse_y = None


def mouse_update(event):
    global mouse_x
    global mouse_y

    mouse_x = event.x
    mouse_y = event.y


class App:
    __root = None
    __canvas = None

    def __init__(self, width, height):
        self.__root = tk.Tk()
        self.__canvas = tk.Canvas(self.__root, width=width * 3, height=height * 3)
        self.__canvas.bind('<Enter>', mouse_update)
        self.__canvas.bind('<Motion>', mouse_update)
        self.__canvas.pack()

    def get_canvas(self):
        return self.__canvas

    def run_mainloop(self):
        self.__root.mainloop()


class Tile:

    def __init__(self, canvas, pos_x, pos_y, image_filepath):
        self.__canvas = canvas
        photo_image = tk.PhotoImage(file=image_filepath)
        self.__image_id = self.__canvas.create_image(pos_x, pos_y, image=photo_image)
        self.__canvas.tag_bind(self.__image_id, '<Button-1>', lambda e: self.on_click())

        self.__image_width = photo_image.width()
        self.__image_height = photo_image.height()
        self.__radius_bound = self.__image_height / 2
        self.__is_selected = False

    def inbound(self):
        global mouse_x
        global mouse_y
        pos = self.__canvas.coords(self.__image_id)
        centre_x = pos[0]
        centre_y = pos[1]

        x = centre_x - mouse_x
        y = centre_y - mouse_y
        dis = math.sqrt((x ** 2) + (y ** 2))

        return dis <= self.__radius_bound

    def on_click(self, value=None):
        if not self.inbound():
            return

        if value is None:
            value = self.__is_selected

        # self.__canvas.itemconfig(self.image_id, image=(easy_tile if value else diff_tile))
        self.__is_selected = not value

        print(self.__image_id, "at", self.__canvas.coords(self.__image_id), "is selected:", self.__is_selected)


if __name__ == '__main__':
    canvas_width = 90
    canvas_height = 80

    app = App(canvas_width, canvas_height)
    tile = Tile(app.get_canvas(), canvas_width/2, canvas_height/2, TILE_IMAGES[TILE_EASY])

    app.run_mainloop()
