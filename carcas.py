# -*- coding: utf-8 -*-
import random
from collections import OrderedDict

from utils import Display
from constants import N, E, S, W, TILES, RotatableTile, TYPES

OPPOSITES = {N: S, E: W, S: N, W: E}
alter_position = lambda pos, drctn: (pos[0] + drctn[0], pos[1] + drctn[1])

class Tile(object):
    def __init__(self, north, east, south, west):
        self.edges = OrderedDict([(N, north), (E, east), (S, south), (W, west)])

    def edge(self, direction):
        return self.edges[direction]

    def __unicode__(self):
        return TILES[(tuple(self.edges.values()))]

class Surface(object):
    def __init__(self):
        self.tiles = {}

    def grow_randomly(self):
        new_tile = RotatableTile(random.choice(TYPES))
        if not self.tiles:
            self.place(new_tile, (0, 0))
            return

        for position, tile in self.tiles.items():
            for direction in (N, E, S, W):
                for _ in range(4):
                    try:
                        desired = alter_position(position, direction)
                        self.place(new_tile, desired)
                        return
                    except AssertionError:
                        new_tile.rotate()

    def place(self, new_tile, desired_position):
        assert desired_position not in self.tiles

        for direction in (N, E, S, W):
            try:
                existing_tile = self.tiles[alter_position(desired_position, direction)]
            except KeyError:
                continue

            assert new_tile.edge(direction) == existing_tile.edge(OPPOSITES[direction])

        self.tiles[desired_position] = new_tile


if __name__ == '__main__':
    surface = Surface()
    with Display() as display:
        while True:
            for position, tile in surface.tiles.iteritems():
                display.place_char(unicode(tile), position[0], position[1])
            display.refresh(sleep_time=.05)
            surface.grow_randomly()

