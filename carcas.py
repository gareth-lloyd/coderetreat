# -*- coding: utf-8 -*-
import random
from collections import OrderedDict

FIELD = 0
ROAD = 1

N  =  (0, 1)
E  =  (1, 0)
S  =  (0, -1)
W  =  (-1, 0)
OPPOSITES = {N: S, E: W, S: N, W: E}
TILES = {
    (1, 0, 1, 1) : u'┤',
    (1, 1, 0, 1) : u'┴',
#   (1, 0, 0, 0) : u'╵',
    (0, 1, 1, 0) : u'┌',
    (1, 0, 1, 0) : u'│',
#   (0, 0, 0, 1) : u'╴',
    (0, 0, 1, 1) : u'┐',
    (1, 0, 0, 1) : u'┘',
#   (0, 1, 0, 0) : u'╶',
    (1, 1, 1, 1) : u'┼',
    (0, 0, 0, 0) : u'\u25A2',
#   (0, 0, 1, 0) : u'╷',
    (0, 1, 0, 1) : u'─',
    (1, 1, 1, 0) : u'├',
    (0, 1, 1, 1) : u'┬',
    (1, 1, 0, 0) : u'└',
}

class Tile(object):
    def __init__(self, north, east, south, west):
        self.edges = OrderedDict([(N, north), (E, east), (S, south), (W, west)])

    def edge(self, direction):
        return self.edges[direction]

    def __unicode__(self):
        return TILES[(tuple(self.edges.values()))]

def random_tile():
    if random.random() > .5:
        return Tile(0, 0, 0, 0)
    return Tile(*random.choice(TILES.keys()))

def alter_position(position, delta):
    return (position[0] + delta[0], position[1] + delta[1])

class Surface(object):
    def __init__(self):
        self.tiles = {}

    def grow_randomly(self):
        new_tile = random_tile()
        if not self.tiles:
            self.place(new_tile, (0, 0))
            return

        for position, tile in self.tiles.iteritems():
            for delta in (N, E, S, W):
                desired = alter_position(position, delta)
                try:
                    self.place(new_tile, desired)
                    return
                except ValueError:
                    pass

    def place(self, new_tile, desired_position):
        if desired_position in self.tiles:
            raise ValueError("Can't place here")

        for direction in (N, E, S, W):
            test_position = alter_position(desired_position, direction)
            if test_position in self.tiles:
                existing_tile = self.tiles[test_position]
            else:
                continue

            if new_tile.edge(direction) == existing_tile.edge(OPPOSITES[direction]):
                continue

            raise ValueError("Can't place here")
        self.tiles[desired_position] = new_tile

if __name__ == '__main__':
    import locale, sys, curses, time
    locale.setlocale(locale.LC_ALL, '')
    encoding = locale.getpreferredencoding()

    surface = Surface()
    try:
        window = curses.initscr()
        while True:
            window.clear()
            display = filter(lambda pt: pt[0][0] + 20 >= 0 and (-1 * pt[0][1]) + 20 >= 0, surface.tiles.iteritems())
            for position, tile in display:
                window.addstr((-1 * position[1]) + 20, position[0] + 20, unicode(tile).encode(encoding))
            window.refresh()
            time.sleep(.05)
            surface.grow_randomly()
    finally:
        curses.endwin()
