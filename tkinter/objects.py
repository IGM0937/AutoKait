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
        self.__pos_x, self.__pos_y = calculate_xy_location([row, column])
        self.__canvas = canvas
        self.__image_width = image_base.width()
        self.__image_height = image_base.height()
        self.__layer_base_id = self.__canvas.create_image(self.__pos_x, self.__pos_y, image=image_base)

        if tile_type is TILE_NONE:
            return

        LOCATION_MAP.update({location: self})
        self.__is_selected = False
        self.__trains_type_w_id = {}
        self.__radius_bound = self.__image_height / 2
        self.__layer_selection_id = self.__canvas.create_image(self.__pos_x, self.__pos_y,
                                                               image=TILE_IMAGES.get(TILE_UNSELECT))
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

    def add_train(self, train_type):
        if train_type in self.__trains_type_w_id.keys():
            return

        self.__trains_type_w_id.update({train_type: None})

        # render trains on tile
        train_rel_pos_list = TRAIN_RELATIVE_POSITIONS.get(len(self.__trains_type_w_id))
        train_count = 0

        for train_type, train_id in self.__trains_type_w_id.items():
            rel_pos = train_rel_pos_list[train_count]
            train_count += 1

            if train_id is None:
                rel_pos_x, rel_pos_y = self.__pos_x + rel_pos[0], self.__pos_y + rel_pos[1]
                new_train_id = self.__canvas.create_image(rel_pos_x, rel_pos_y, image=TRAIN_IMAGES.get(train_type))
                self.__canvas.tag_lower(new_train_id, self.__layer_selection_id)
                self.__trains_type_w_id.update({train_type: new_train_id})
            else:
                self.__canvas.move(train_id, rel_pos[0], rel_pos[1])

    def click_inbound(self):
        res_x = self.__pos_x - con.MOUSE_X
        res_y = self.__pos_y - con.MOUSE_Y
        centre_dist = math.sqrt((res_x ** 2) + (res_y ** 2))
        return centre_dist <= self.__radius_bound

    def on_click(self, forced_state=None, overlap=None):
        tile = self if overlap is None else overlap
        if not tile.click_inbound():
            return

        tile.is_selected((not tile.is_selected()) if forced_state is None else forced_state)
        image = TILE_IMAGES.get(TILE_SELECT) if tile.is_selected() else TILE_IMAGES.get(TILE_UNSELECT)
        tile.get_canvas().itemconfig(tile.get_layer_selection_id(), image=image)
