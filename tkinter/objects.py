import math
import constants as con
from constants import *


class Tile:
    """
    Tile Layers (top-to-bottom):
        * Selection layer
        * Location Sign Layer
        * Pieces Layer
        * Trains Layer
        * Base image layer
    """
    def __init__(self, canvas, location, tile_type):
        column = int(location[1:])
        row = ROW_INDEX.get(location[0]) + (column % 2)

        pos_x = CANVAS_X_START + (CANVAS_X_STEP * column)
        pos_y = CANVAS_Y_START + (CANVAS_Y_STEP * row)

        self.__canvas = canvas
        self.__image_base = TILE_IMAGES.get(tile_type)
        self.__image_width = self.__image_base.width()
        self.__image_height = self.__image_base.height()
        self.__radius_bound = self.__image_height / 2
        self.__image_select = TILE_IMAGES.get(TILE_SELECT)
        self.__image_unselect = TILE_IMAGES.get(TILE_UNSELECT)
        self.__layer_base_id = self.__canvas.create_image(pos_x, pos_y, image=self.__image_base)
        self.__layer_selection_id = self.__canvas.create_image(pos_x, pos_y, image=self.__image_unselect)
        self.__canvas.tag_bind(self.__layer_selection_id, '<Button-1>', lambda e: self.on_click())
        self.__is_selected = False

    def inbound(self):
        pos = self.__canvas.coords(self.__layer_base_id)
        centre_x, centre_y = pos[0], pos[1]
        res_x = centre_x - con.MOUSE_X
        res_y = centre_y - con.MOUSE_Y
        centre_dist = math.sqrt((res_x ** 2) + (res_y ** 2))
        return centre_dist <= self.__radius_bound

    def on_click(self, forced_state=None):
        if not self.inbound():
            return

        self.__is_selected = (not self.__is_selected) if forced_state is None else forced_state
        image = self.__image_select if self.__is_selected else self.__image_unselect
        self.__canvas.itemconfig(self.__layer_selection_id, image=image)
