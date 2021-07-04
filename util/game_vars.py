"""
Program Name:   AutoKait
Description:    The automa A.I. player designed to be used for the board game, Irish Gauge.
Author:         Igor Goran Mačukat
Filename:       game_vars.py

Copyright (C) 2021

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>.

----

List of global game variables and their starting defaults, if relevant.
    POTENTIAL FUTURE DATA POINTS:
        * storing the variables in game_objects
        - company rating
        - interest cube rating
        - player threat rating
"""
import util.tools as tools
import util.output_text as output
from util.constants import *
from util.game_objects import *

current_action = None
data_point = {}
tile_board = {}
tile_company_start = {}
tile_named_locations = None
game_piece_counters = {}

# unsure of the following lists are useful
# but created and populated anyway
tile_black_si_cubes = []
tile_white_si_cubes = []
tile_pink_si_cubes = []
tile_trains_cbsc = []
tile_trains_wlw = []
tile_trains_bcd = []
tile_trains_gsw = []
tile_trains_mgw = []


def setup_players():
    """
    Sets up the players and saves them into the data point dictionary.
    """
    data_point[PLAYER_KAIT] = Player("Kait")


def setup_tile_board():
    """
    Creates the in-memory virtual game board.
    Each of the tiles with locations, types, name and adjacent tiles
    """

    # a-row
    a5 = Tile('a5', TILE_EASY)
    a6 = Tile('a6', TILE_DIFF)
    a7 = Tile('a7', TILE_EASY)
    a8 = Tile('a8', TILE_EASY)
    a9 = Tile('a9', TILE_DIFF)
    a10 = Tile('a10', TILE_EASY)
    a11 = Tile('a11', TILE_EASY)
    a12 = Tile('a12', TILE_DIFF)
    # b-row
    b5 = Tile('b5', TILE_EASY)
    b6 = Tile('b6', TILE_DIFF)
    b7 = Tile('b7', TILE_DIFF)
    b8 = Tile('b8', TILE_CITY, 'Derry')
    b9 = Tile('b9', TILE_DIFF)
    b10 = Tile('b10', TILE_EASY)
    b11 = Tile('b11', TILE_EASY)
    b12 = Tile('b12', TILE_DIFF)
    # c-row
    c6 = Tile('c6', TILE_EASY)
    c7 = Tile('c7', TILE_EASY)
    c8 = Tile('c8', TILE_EASY)
    c9 = Tile('c9', TILE_DIFF)
    c10 = Tile('c10', TILE_EASY)
    c11 = Tile('c11', TILE_EASY)
    c12 = Tile('c12', TILE_MCITY, 'Belfast')
    # d-row
    d4 = Tile('d4', TILE_TOWN, 'Sligo')
    d5 = Tile('d5', TILE_EASY)
    d6 = Tile('d6', TILE_EASY)
    d7 = Tile('d7', TILE_EASY)
    d8 = Tile('d8', TILE_DIFF)
    d9 = Tile('d9', TILE_TOWN, 'Monaghan')
    d10 = Tile('d10', TILE_DIFF)
    d11 = Tile('d11', TILE_EASY)
    d12 = Tile('d12', TILE_DIFF)
    # e-row
    e1 = Tile('e1', TILE_DIFF)
    e2 = Tile('e2', TILE_EASY)
    e3 = Tile('e3', TILE_DIFF)
    e4 = Tile('e4', TILE_DIFF)
    e5 = Tile('e5', TILE_EASY)
    e6 = Tile('e6', TILE_EASY)
    e7 = Tile('e7', TILE_EASY)
    e8 = Tile('e8', TILE_EASY)
    e9 = Tile('e9', TILE_EASY)
    e10 = Tile('e10', TILE_EASY)
    e11 = Tile('e11', TILE_EASY)
    e12 = Tile('e12', TILE_DIFF)
    # f-row
    f1 = Tile('f1', TILE_DIFF)
    f2 = Tile('f2', TILE_TOWN, 'Castlebar')
    f3 = Tile('f3', TILE_EASY)
    f4 = Tile('f4', TILE_EASY)
    f5 = Tile('f5', TILE_EASY)
    f6 = Tile('f6', TILE_EASY)
    f7 = Tile('f7', TILE_EASY)
    f8 = Tile('f8', TILE_EASY)
    f9 = Tile('f9', TILE_EASY)
    f10 = Tile('f10', TILE_EASY)
    f11 = Tile('f11', TILE_TOWN, 'Drogheda')
    # g-row
    g1 = Tile('g1', TILE_DIFF)
    g2 = Tile('g2', TILE_EASY)
    g3 = Tile('g3', TILE_EASY)
    g4 = Tile('g4', TILE_EASY)
    g5 = Tile('g5', TILE_EASY)
    g6 = Tile('g6', TILE_EASY)
    g7 = Tile('g7', TILE_EASY)
    g8 = Tile('g8', TILE_EASY)
    g9 = Tile('g9', TILE_EASY)
    g10 = Tile('g10', TILE_EASY)
    g11 = Tile('g11', TILE_EASY)
    # h-row
    h1 = Tile('h1', TILE_EASY)
    h2 = Tile('h2', TILE_EASY)
    h3 = Tile('h3', TILE_MCITY, 'Galway')
    h4 = Tile('h4', TILE_EASY)
    h5 = Tile('h5', TILE_EASY)
    h6 = Tile('h6', TILE_EASY)
    h7 = Tile('h7', TILE_TOWN, 'Tullamore')
    h8 = Tile('h8', TILE_EASY)
    h9 = Tile('h9', TILE_EASY)
    h10 = Tile('h10', TILE_EASY)
    h11 = Tile('h11', TILE_MCITY, 'Dublin')
    # i-row
    i2 = Tile('i2', TILE_EASY)
    i4 = Tile('i4', TILE_EASY)
    i5 = Tile('i5', TILE_EASY)
    i6 = Tile('i6', TILE_EASY)
    i7 = Tile('i7', TILE_DIFF)
    i8 = Tile('i8', TILE_EASY)
    i9 = Tile('i9', TILE_EASY)
    i10 = Tile('i10', TILE_EASY)
    i11 = Tile('i11', TILE_DIFF)
    # j-row
    j3 = Tile('j3', TILE_EASY)
    j4 = Tile('j4', TILE_EASY)
    j5 = Tile('j5', TILE_EASY)
    j6 = Tile('j6', TILE_EASY)
    j7 = Tile('j7', TILE_EASY)
    j8 = Tile('j8', TILE_EASY)
    j9 = Tile('j9', TILE_DIFF)
    j10 = Tile('j10', TILE_EASY)
    j11 = Tile('j11', TILE_DIFF)
    j12 = Tile('j12', TILE_TOWN, 'Wicklow')
    # k-row
    k2 = Tile('k2', TILE_EASY)
    k3 = Tile('k3', TILE_TOWN, 'Shannon')
    k4 = Tile('k4', TILE_EASY)
    k5 = Tile('k5', TILE_DIFF)
    k6 = Tile('k6', TILE_DIFF)
    k7 = Tile('k7', TILE_EASY)
    k8 = Tile('k8', TILE_EASY)
    k9 = Tile('k9', TILE_EASY)
    k10 = Tile('k10', TILE_EASY)
    k11 = Tile('k11', TILE_EASY)
    k12 = Tile('k12', TILE_TOWN, 'Arklow')
    # l-row
    l1 = Tile('l1', TILE_EASY)
    l2 = Tile('l2', TILE_EASY)
    l3 = Tile('l3', TILE_EASY)
    l4 = Tile('l4', TILE_CITY, 'Limerick')
    l5 = Tile('l5', TILE_EASY)
    l6 = Tile('l6', TILE_EASY)
    l7 = Tile('l7', TILE_EASY)
    l8 = Tile('l8', TILE_CITY, 'Kilkenny')
    l9 = Tile('l9', TILE_TOWN, 'New Ross')
    l10 = Tile('l10', TILE_DIFF)
    l11 = Tile('l11', TILE_EASY)
    # m-row
    m1 = Tile('m1', TILE_EASY)
    m2 = Tile('m2', TILE_DIFF)
    m3 = Tile('m3', TILE_DIFF)
    m4 = Tile('m4', TILE_EASY)
    m5 = Tile('m5', TILE_EASY)
    m6 = Tile('m6', TILE_EASY)
    m7 = Tile('m7', TILE_DIFF)
    m8 = Tile('m8', TILE_EASY)
    m9 = Tile('m9', TILE_CITY, 'Waterford')
    m10 = Tile('m10', TILE_EASY)
    # n-row
    n1 = Tile('n1', TILE_TOWN, 'Killarney')
    n2 = Tile('n2', TILE_DIFF)
    n3 = Tile('n3', TILE_DIFF)
    n4 = Tile('n4', TILE_DIFF)
    n5 = Tile('n5', TILE_EASY)
    n6 = Tile('n6', TILE_EASY)
    # o-row
    o1 = Tile('o1', TILE_DIFF)
    o2 = Tile('o2', TILE_DIFF)
    o3 = Tile('o3', TILE_EASY)
    o4 = Tile('o4', TILE_CITY, 'Cork')
    # p-row
    p2 = Tile('p2', TILE_DIFF)
    # a-row adjacent
    a5.set_adjacent(a6, b6, b5)
    a6.set_adjacent(a7, b6, a5)
    a7.set_adjacent(a8, b8, b7, b6, a6)
    a8.set_adjacent(a9, b8, a7)
    a9.set_adjacent(a10, b10, b9, b8, a8)
    a10.set_adjacent(a11, b10, a9)
    a11.set_adjacent(a12, b12, b11, b10, a10)
    a12.set_adjacent(b12, a11)
    # b-row adjacent
    b5.set_adjacent(a5, b6, c6)
    b6.set_adjacent(a6, a7, b7, c6, b5, a5)
    b7.set_adjacent(a7, b8, c8, c7, c6, b6)
    b8.set_adjacent(a8, a9, b9, c8, b7, a7)
    b9.set_adjacent(a9, b10, c10, c9, c8, b8)
    b10.set_adjacent(a10, a11, b11, c10, b9, a9)
    b11.set_adjacent(a11, b12, c12, c11, c10, b10)
    b12.set_adjacent(a12, c12, b11, a11)
    # c-row adjacent
    c6.set_adjacent(b6, b7, c7, d6, b5)
    c7.set_adjacent(b7, c8, d8, d7, d6, c6)
    c8.set_adjacent(b8, b9, c9, d8, c7, b7)
    c9.set_adjacent(b9, c10, d10, d9, d8, c8)
    c10.set_adjacent(b10, b11, c11, d10, c9, b9)
    c11.set_adjacent(b11, c12, d12, d11, d10, c10)
    c12.set_adjacent(b12, d12, c11, b11)
    # d-row adjacent
    d4.set_adjacent(d5, e4)
    d5.set_adjacent(d6, e6, e5, e4, d4)
    d6.set_adjacent(c6, c7, d7, e6, d5)
    d7.set_adjacent(c7, d8, e8, e7, e6, d6)
    d8.set_adjacent(c8, c9, d9, e8, d7, c7)
    d9.set_adjacent(c9, d10, e10, e9, e8, d8)
    d10.set_adjacent(c10, c11, d11, e10, d9, c9)
    d11.set_adjacent(c11, d12, e12, e11, e10, d10)
    d12.set_adjacent(c12, e12, d11, c11)
    # e-row adjacent
    e1.set_adjacent(e2, f2, f1)
    e2.set_adjacent(e3, f2, e1)
    e3.set_adjacent(e4, f4, f3, f2, e2)
    e4.set_adjacent(d4, d5, e5, f4, e3)
    e5.set_adjacent(d5, e6, f6, f5, f4, e4)
    e6.set_adjacent(d6, d7, e7, f6, e5, d5)
    e7.set_adjacent(d7, e8, f8, f7, f6, e6)
    e8.set_adjacent(d8, d9, e9, f8, e7, d7)
    e9.set_adjacent(d9, e10, f10, f9, f8, e8)
    e10.set_adjacent(d10, d11, e11, f10, e9, d9)
    e11.set_adjacent(d11, e12, f11, f10, e10)
    e12.set_adjacent(d12, e11, d11)
    # f-row adjacent
    f1.set_adjacent(e1, f2, g2, g1)
    f2.set_adjacent(e2, e3, f3, g2, f1, e1)
    f3.set_adjacent(e3, f4, g4, g3, g2, f2)
    f4.set_adjacent(e4, e5, f5, g4, f3, e3)
    f5.set_adjacent(d5, e6, f6, f5, f4, e4)
    f6.set_adjacent(e6, e7, f7, g6, f5, e5)
    f7.set_adjacent(e7, f8, g8, g7, g6, f6)
    f8.set_adjacent(e8, e9, f9, g8, f7, e7)
    f9.set_adjacent(e9, f10, g10, g9, g8, f8)
    f10.set_adjacent(e10, e11, f11, g10, f9, e9)
    f11.set_adjacent(e11, g11, g10, f10)
    # g-row adjacent
    g1.set_adjacent(f1, g2, h2, h1)
    g2.set_adjacent(f2, f3, g3, h2, g1, f1)
    g3.set_adjacent(f3, g4, h4, h3, h2, g2)
    g4.set_adjacent(f4, f5, g5, h4, g3, f3)
    g5.set_adjacent(f5, g6, h6, h5, h4, g4)
    g6.set_adjacent(f6, f7, g7, h6, g5, f5)
    g7.set_adjacent(f7, g8, h8, h7, h6, g6)
    g8.set_adjacent(f8, f9, g9, h8, g7, f7)
    g9.set_adjacent(f9, g10, h10, h9, h8, g8)
    g10.set_adjacent(f10, f11, g11, h10, g9, f9)
    g11.set_adjacent(f11, h11, h10, g10)
    # h-row adjacent
    h1.set_adjacent(g1, h2, i2)
    h2.set_adjacent(g2, g3, h3, i2, h1, g1)
    h3.set_adjacent(g3, h4, i4, i2, h2)
    h4.set_adjacent(g4, g5, h5, i4, h3, g3)
    h5.set_adjacent(g5, h6, i6, i5, i4, h4)
    h6.set_adjacent(g6, g7, h7, i6, h5, g5)
    h7.set_adjacent(g7, h8, i8, i7, i6, h6)
    h8.set_adjacent(g8, g9, h9, i8, h7, g7)
    h9.set_adjacent(g9, h10, i10, i9, i8, h8)
    h10.set_adjacent(g10, g11, h11, i10, h9, g9)
    h11.set_adjacent(g11, i11, i10, h10)
    # i-row adjacent
    i2.set_adjacent(h2, h3, h1)
    i4.set_adjacent(h4, h5, i5, j4, h3)
    i5.set_adjacent(h5, i6, j6, j5, j4, i4)
    i6.set_adjacent(h6, h7, i7, j6, i5, h5)
    i7.set_adjacent(h7, i8, j8, j7, j6, i6)
    i8.set_adjacent(h8, h9, i9, j8, i7, h7)
    i9.set_adjacent(h9, i10, j10, j9, j8, i8)
    i10.set_adjacent(h10, h11, i11, j10, i9, h9)
    i11.set_adjacent(h11, j12, j11, j10, i10)
    # j-row adjacent
    j3.set_adjacent(j4, k4, k3, k2)
    j4.set_adjacent(i4, i5, j5, k4, j3)
    j5.set_adjacent(i5, j6, k6, k5, k4, j4)
    j6.set_adjacent(i6, i7, j7, k6, j5, i5)
    j7.set_adjacent(i7, j8, k8, k7, k6, j6)
    j8.set_adjacent(i8, i9, j9, k8, j7, i7)
    j9.set_adjacent(i9, j10, k10, k9, k8, j8)
    j10.set_adjacent(i10, i11, j11, k10, j9, i9)
    j11.set_adjacent(i11, j12, k12, k11, k10, j10)
    j12.set_adjacent(k12, j11, i11)
    # k-row adjacent
    k2.set_adjacent(j3, k3, l2)
    k3.set_adjacent(j3, k4, l4, l3, l2, k2)
    k4.set_adjacent(j4, j5, k5, l4, k3, j3)
    k5.set_adjacent(j5, k6, l6, l5, l4, k4)
    k6.set_adjacent(j6, j7, k7, l6, k5, j5)
    k7.set_adjacent(j7, k8, l8, l7, l6, k6)
    k8.set_adjacent(j8, j9, k9, l8, k7, j7)
    k9.set_adjacent(j9, k10, l10, l9, l8, k8)
    k10.set_adjacent(j10, j11, k11, l10, k9, j9)
    k11.set_adjacent(j11, k12, l11, l10, k10)
    k12.set_adjacent(j12, k11, j11)
    # l-row adjacent
    l1.set_adjacent(l2, m2, m1)
    l2.set_adjacent(k2, k3, l3, m2, l1)
    l3.set_adjacent(k3, l4, m4, m3, m2, l2)
    l4.set_adjacent(k4, k5, l5, m4, l3, k3)
    l5.set_adjacent(k5, l6, m6, m5, m4, l4)
    l6.set_adjacent(k6, k7, l7, m6, l5, k5)
    l7.set_adjacent(k7, l8, m8, m7, m6, l6)
    l8.set_adjacent(k8, k9, l9, m8, l7, k7)
    l9.set_adjacent(k9, l10, m10, m9, m8, l8)
    l10.set_adjacent(k10, k11, l11, m10, l9, k9)
    l11.set_adjacent(k11, m10, l10)
    # m-row adjacent
    m1.set_adjacent(l1, m2, n2, n1)
    m2.set_adjacent(l2, l3, m3, n2, m1, l1)
    m3.set_adjacent(l3, m4, n4, n3, n2, m2)
    m4.set_adjacent(l4, l5, m5, n4, m3, l3)
    m5.set_adjacent(l5, m6, n6, n5, n4, m4)
    m6.set_adjacent(l6, l7, m7, n6, m5, l5)
    m7.set_adjacent(l7, m8, n6, m6)
    m8.set_adjacent(l8, l9, m9, m7, l7)
    m9.set_adjacent(l9, m10, m8)
    m10.set_adjacent(l10, l11, m9, l9)
    # n-row adjacent
    n1.set_adjacent(m1, n2, o2, o1)
    n2.set_adjacent(m2, m3, n3, o2, n1, m1)
    n3.set_adjacent(m3, n4, o4, o3, o2, n2)
    n4.set_adjacent(m4, m5, n5, o4, n3, m3)
    n5.set_adjacent(m5, n6, o4, n4)
    n6.set_adjacent(m6, m7, n5, m5)
    # o-row adjacent
    o1.set_adjacent(n1, o2, p2)
    o2.set_adjacent(n2, n3, o3, p2, o1, n1)
    o3.set_adjacent(n3, o4, p2, o2)
    o4.set_adjacent(n4, n5, o3, n3)
    # p-row adjacent
    p2.set_adjacent(o2, o3, o1)

    # a-row dictionary
    tile_board.update({
        a5.location(): a5,
        a6.location(): a6,
        a7.location(): a7,
        a8.location(): a8,
        a9.location(): a9,
        a10.location(): a10,
        a11.location(): a11,
        a12.location(): a12
    })
    # b-row dictionary
    tile_board.update({
        b5.location(): b5,
        b6.location(): b6,
        b7.location(): b7,
        b8.location(): b8,
        b9.location(): b9,
        b10.location(): b10,
        b11.location(): b11,
        b12.location(): b12
    })
    # c-row dictionary
    tile_board.update({
        c6.location(): c6,
        c7.location(): c7,
        c8.location(): c8,
        c9.location(): c9,
        c10.location(): c10,
        c11.location(): c11,
        c12.location(): c12
    })
    # d-row dictionary
    tile_board.update({
        d4.location(): d4,
        d5.location(): d5,
        d6.location(): d6,
        d7.location(): d7,
        d8.location(): d8,
        d9.location(): d9,
        d10.location(): d10,
        d11.location(): d11,
        d12.location(): d12
    })
    # e-row dictionary
    tile_board.update({
        e1.location(): e1,
        e2.location(): e2,
        e3.location(): e3,
        e4.location(): e4,
        e5.location(): e5,
        e6.location(): e6,
        e7.location(): e7,
        e8.location(): e8,
        e9.location(): e9,
        e10.location(): e10,
        e11.location(): e11,
        e12.location(): e12
    })
    # f-row dictionary
    tile_board.update({
        f1.location(): f1,
        f2.location(): f2,
        f3.location(): f3,
        f4.location(): f4,
        f5.location(): f5,
        f6.location(): f6,
        f7.location(): f7,
        f8.location(): f8,
        f9.location(): f9,
        f10.location(): f10,
        f11.location(): f11,
    })
    # g-row dictionary
    tile_board.update({
        g1.location(): g1,
        g2.location(): g2,
        g3.location(): g3,
        g4.location(): g4,
        g5.location(): g5,
        g6.location(): g6,
        g7.location(): g7,
        g8.location(): g8,
        g9.location(): g9,
        g10.location(): g10,
        g11.location(): g11,
    })
    # h-row dictionary
    tile_board.update({
        h1.location(): h1,
        h2.location(): h2,
        h3.location(): h3,
        h4.location(): h4,
        h5.location(): h5,
        h6.location(): h6,
        h7.location(): h7,
        h8.location(): h8,
        h9.location(): h9,
        h10.location(): h10,
        h11.location(): h11,
    })
    # i-row dictionary
    tile_board.update({
        i2.location(): i2,
        i4.location(): i4,
        i5.location(): i5,
        i6.location(): i6,
        i7.location(): i7,
        i8.location(): i8,
        i9.location(): i9,
        i10.location(): i10,
        i11.location(): i11,
    })
    # j-row dictionary
    tile_board.update({
        j3.location(): j3,
        j4.location(): j4,
        j5.location(): j5,
        j6.location(): j6,
        j7.location(): j7,
        j8.location(): j8,
        j9.location(): j9,
        j10.location(): j10,
        j11.location(): j11,
    })
    # k-row dictionary
    tile_board.update({
        k2.location(): k2,
        k3.location(): k3,
        k4.location(): k4,
        k5.location(): k5,
        k6.location(): k6,
        k7.location(): k7,
        k8.location(): k8,
        k9.location(): k9,
        k10.location(): k10,
        k11.location(): k11,
    })
    # l-row dictionary
    tile_board.update({
        l1.location(): l2,
        l2.location(): l2,
        l3.location(): l3,
        l4.location(): l4,
        l5.location(): l5,
        l6.location(): l6,
        l7.location(): l7,
        l8.location(): l8,
        l9.location(): l9,
        l10.location(): l10,
        l11.location(): l11,
    })
    # m-row dictionary
    tile_board.update({
        m1.location(): m1,
        m2.location(): m2,
        m3.location(): m3,
        m4.location(): m4,
        m5.location(): m5,
        m6.location(): m6,
        m7.location(): m7,
        m8.location(): m8,
        m9.location(): m9,
        m10.location(): m10,
    })
    # n-row dictionary
    tile_board.update({
        n1.location(): n1,
        n2.location(): n2,
        n3.location(): n3,
        n4.location(): n4,
        n5.location(): n5,
        n6.location(): n6
    })
    # o-row dictionary
    tile_board.update({
        o1.location(): o1,
        o2.location(): o2,
        o3.location(): o3,
        o4.location(): o4
    })
    # p-row dictionary
    tile_board.update({
        p2.location(): p2
    })
    # setup tile variables
    global tile_named_locations
    tile_named_locations = (b8, c12, d4, d9, f2, f11, h3, h7, h11, j12, k3, k12, l4, l8, l9, m9, n1, o4)


def setup_init_game_pieces(in_dev_mode=False):
    """
    Sets up the initial counts of the representative board game pieces.
    It also places the initial train locations of each company.
    See map_cheat_sheet for more details.

    In developer mode, additional train pieces added to the board
    and the initial special interest cube places are prepopulated.
    """

    # setup a list of game piece counters
    game_piece_counters.update({
        TRAIN_CBSC: game_vars.pieces_trains_cbsc,
        TRAIN_WLW: game_vars.pieces_trains_wlw,
        TRAIN_BCD: game_vars.pieces_trains_bcd,
        TRAIN_GSW: game_vars.pieces_trains_gsw,
        TRAIN_MGW: game_vars.pieces_trains_mgw,
        CUBE_SI_BLACK: game_vars.pieces_cubes_si_black,
        CUBE_SI_WHITE: game_vars.pieces_cubes_si_white,
        CUBE_SI_PINK: game_vars.pieces_cubes_si_pink
    })

    # place initial company train tracks
    o4 = tile_board.get('o4')
    o4.add_train(TRAIN_CBSC)
    tile_company_start.update({RAILWAY_CBSC: o4})

    l4 = tile_board.get('l4')
    l4.add_train(TRAIN_WLW)
    tile_company_start.update({RAILWAY_WLW: l4})

    c12 = tile_board.get('c12')
    c12.add_train(TRAIN_BCD)
    tile_company_start.update({RAILWAY_BCD: c12})

    h11 = tile_board.get('h11')
    h11.add_train(TRAIN_GSW)
    tile_company_start.update({RAILWAY_GSW: h11})
    h11.add_train(TRAIN_MGW)
    tile_company_start.update({RAILWAY_MGW: h11})

    if in_dev_mode:
        # additional train placements for development purposes
        mgw_location_list = ('h10', 'g9', 'h8', 'h7')
        for location in mgw_location_list:
            tile = tile_board.get(location)
            tile.add_train(TRAIN_MGW)

    print(output.setup_starting_trains_placed(in_dev_mode))

    # place initial special interest cubes
    locations = ['c12', 'h11', 'h3', 'b8', 'l8', 'm9', 'l4', 'o4']
    dev_si_cubes = [CUBE_SI_BLACK, CUBE_SI_WHITE, CUBE_SI_PINK]
    dev_si_count = 0

    for location in locations:
        tile: Tile = tile_board.get(location)
        if in_dev_mode:
            cube = dev_si_cubes[dev_si_count % len(dev_si_cubes)]
            dev_si_count += 1
        else:
            while True:
                cube = tools.ask_user_get_special_interest_cube(f"{output.setup_si_question_prefix()} {tile.name()}? ")
                if cube == BACK:
                    print(output.setup_si_back_function_none_text())
                else:
                    cube = cube[0]
                    break

        tile.set_special_interest(cube)

    print(output.setup_si_completed_text())
