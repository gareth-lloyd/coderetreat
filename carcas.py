# -*- coding: utf-8 -*-
import random

FIELD = 0
ROAD = 1

N  =  (0, 1)
NE =  (1, 1)
E  =  (1, 0)
SE =  (1, -1)
S  =  (0, -1)
SW =  (-1, -1)
W  =  (-1, 0)
NW =  (-1, 1)

position_deltas = [N, NE, E, SE, S, SW, W, NW,]
opposites = {N: E, E: W, S: N, W: E}

class Tile(object):
    TILES = {
        (0, 0, 0, 0): '#',

        (0, 0, 0, 1): u'\u2574',
        (0, 1, 0, 0): u'\u2576',
        (1, 0, 0, 0): u'\u2575',
        (0, 0, 1, 0): u'\u2577',

        (0, 1, 0, 1): u'\u2500',
        (1, 0, 1, 0): u'\u2502',
        (1, 1, 0, 0): u'\u2514',
        (0, 1, 1, 0): u'\u250c',
        (0, 0, 1, 1): u'\u2510',
        (1, 0, 0, 1): u'\u2518',

        (0, 1, 1, 1): u'\u252c',
        (1, 0, 1, 1): u'\u2524',
        (1, 1, 0, 1): u'\u2534',
        (1, 1, 1, 0): u'\u251c',

        (1, 1, 1, 1): u'\u253c',
    }

    def __init__(self, north, east, south, west):
        self.edges = dict([(N, north), (E, east), (S, south), (W, west)])

    def edge(self, direction):
        return self.edges[direction]

    def __unicode__(self):
        return self.TILES[()]

def random_tile():
    return Tile(*[random.choice([ROAD, FIELD]) for _ in range(4)])

def alter_position(position, delta):
    return (position[0] + delta[0], position[1] + delta[1])

def a_to_b(a, b):
    return (b[0] - a[0], b[1] - a[1])

class Surface(object):
    def __init__(self):
        self.tiles = {}

    def grow_randomly(self):
        new_tile = random_tile()
        if not self.tiles:
            self.place(new_tile, (0, 0))
            return

        for position, tile in self.tiles.iteritems():
            for delta in position_deltas:
                desired = alter_position(position, delta)
                if not desired in self.tiles:
                    try:
                        self.place(new_tile, desired)
                        return
                    except ValueError:
                        pass

    def legal(self, new_position, new_tile, existing_position):
        try:
            existing_tile = self.tiles[existing_position]
        except KeyError:
            return True

        direction = a_to_b(existing_position, new_position)
        if direction in (NE, SE, SW, NW):
            return True
        else:
            return existing_tile.edge(direction) == new_tile.edge(opposites[direction])

    def place(self, new_tile, new_position):
        for delta in position_deltas:
            if not self.legal(new_position, new_tile, alter_position(new_position, delta)):
                raise ValueError

        self.tiles[new_position] = new_tile


if __name__ == '__main__':
    import locale
    locale.setlocale(locale.LC_ALL, '')
    encoding = locale.getpreferredencoding()

    import curses
    from time import sleep
    surface = Surface()

    try:
        window = curses.initscr()
        while True:
            window.clear()
            display = filter(lambda pt: pt[0][0] + 20 >= 0 and pt[0][1] + 20 >= 0, surface.tiles.iteritems())
            for position, tile in display:
                window.addstr(position[0] + 20, position[1] + 20, CHARS[tuple(tile.edges.values())].encode('utf-8'))
            window.refresh()
            sleep(.01)
            surface.grow_randomly()
    finally:
        curses.endwin()
