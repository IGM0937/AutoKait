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
        image_base = TILE_IMAGES.get(tile_type)
        row, column = convert_location(location)
        pos_x, pos_y = calculate_xy_location([row, column])
        self.__canvas = canvas
        self.__image_width = image_base.width()
        self.__image_height = image_base.height()
        self.__layer_base_id = self.__canvas.create_image(pos_x, pos_y, image=image_base)

        if tile_type is TILE_NONE:
            return

        LOCATION_MAP.update({location: self})
        self.__is_selected = False
        self.__radius_bound = self.__image_height / 2
        self.__layer_selection_id = self.__canvas.create_image(pos_x, pos_y, image=TILE_IMAGES.get(TILE_UNSELECT))
        self.__canvas.tag_bind(self.__layer_selection_id, '<Button-1>', lambda e: self.on_click())

        if column == 1:
            return

        overlap_column = column - 1
        upper_row = row if (overlap_column % 2) == 0 else row - 2
        lower_row = row + 2 if (overlap_column % 2) == 0 else row

        upper_row_tile = LOCATION_MAP.get(convert_location([upper_row, overlap_column]))
        lower_row_tile = LOCATION_MAP.get(convert_location([lower_row, overlap_column]))

        if upper_row_tile is not None:
            self.__canvas.tag_bind(self.__layer_selection_id, '<Button-1>',
                                   lambda e: self.on_click(overlap=upper_row_tile), add=True)

        if lower_row_tile is not None:
            self.__canvas.tag_bind(self.__layer_selection_id, '<Button-1>',
                                   lambda e: self.on_click(overlap=lower_row_tile), add=True)

    def get_canvas(self):
        return self.__canvas

    def get_layer_selection_id(self):
        return self.__layer_selection_id

    def is_selected(self, value=None):
        if value is None:
            return self.__is_selected
        else:
            self.__is_selected = value

    train_count = 0

    def inbound(self):
        pos = self.__canvas.coords(self.__layer_base_id)
        centre_x, centre_y = pos[0], pos[1]
        res_x = centre_x - con.MOUSE_X
        res_y = centre_y - con.MOUSE_Y
        centre_dist = math.sqrt((res_x ** 2) + (res_y ** 2))
        return centre_dist <= self.__radius_bound

    def on_click(self, forced_state=None, overlap=None):
        tile = self if overlap is None else overlap
        if not tile.inbound():
            return

        tile.is_selected((not tile.is_selected()) if forced_state is None else forced_state)
        image = TILE_IMAGES.get(TILE_SELECT) if tile.is_selected() else TILE_IMAGES.get(TILE_UNSELECT)
        tile.get_canvas().itemconfig(tile.get_layer_selection_id(), image=image)

        if self.train_count == 0:
            add_train(tile, TRAIN_BLUE)
        elif self.train_count == 1:
            add_train(tile, TRAIN_ORANGE)
        elif self.train_count == 2:
            add_train(tile, TRAIN_PURPLE)
        elif self.train_count == 3:
            add_train(tile, TRAIN_RED)
        elif self.train_count == 4:
            add_train(tile, TRAIN_YELLOW)

        self.train_count += 1
        print("CLICKED!")


def add_train(tile, train_type):
    pos = tile.get_canvas().coords(tile.get_layer_selection_id())
    centre_x, centre_y = pos[0], pos[1]
    train_id = tile.get_canvas().create_image(centre_x, centre_y, image=TRAIN_IMAGES.get(train_type))
    tile.get_canvas().tag_lower(train_id, tile.get_layer_selection_id())