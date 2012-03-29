# -*- coding: utf-8 -*-
FIELD = 0
ROAD = 1

# Directions defined as positive or negative movements in the
# x- and y-axis, respectively
N  =  (0, 1)
E  =  (1, 0)
S  =  (0, -1)
W  =  (-1, 0)

TYPES = ('cloisters', 'straight', 'bend', 't-junction')

# These are some useful unicode characters, organized according to
# a rudimentary coding system which you can use or improve.
TILES = {
#    N      E      S      W
    (FIELD, FIELD, FIELD, FIELD) : u'.', # cloisters

    ( ROAD, FIELD,  ROAD, FIELD) : u'│', # straight
    (FIELD,  ROAD, FIELD,  ROAD) : u'─',

    ( ROAD,  ROAD, FIELD, FIELD) : u'└', # bend
    ( ROAD, FIELD, FIELD,  ROAD) : u'┘',
    (FIELD, FIELD,  ROAD,  ROAD) : u'┐',
    (FIELD,  ROAD,  ROAD, FIELD) : u'┌',

    ( ROAD,  ROAD,  ROAD, FIELD) : u'├', # t
    ( ROAD,  ROAD, FIELD,  ROAD) : u'┴',
    ( ROAD, FIELD,  ROAD,  ROAD) : u'┤',
    (FIELD,  ROAD,  ROAD,  ROAD) : u'┬',
}

ORIENTATIONS = {
    N: 0,
    0: N,
    E: 1,
    1: E,
    S: 2,
    2: S,
    W: 3,
    3: W,
}


TILE_ORIENTATIONS = {
    'bend' :  {
        0: ( ROAD,  ROAD, FIELD, FIELD),
        1: ( ROAD, FIELD, FIELD,  ROAD),
        2: (FIELD, FIELD,  ROAD,  ROAD),
        3: (FIELD,  ROAD,  ROAD, FIELD),
    },
    'cloisters' :  {
        0: (FIELD, FIELD, FIELD, FIELD),
        1: (FIELD, FIELD, FIELD, FIELD),
        2: (FIELD, FIELD, FIELD, FIELD),
        3: (FIELD, FIELD, FIELD, FIELD),
    },
    'straight' :  {
        0: ( ROAD, FIELD,  ROAD, FIELD),
        1: (FIELD,  ROAD, FIELD,  ROAD),
        2: ( ROAD, FIELD,  ROAD, FIELD),
        3: (FIELD,  ROAD, FIELD,  ROAD),
    },
    't-junction' :  {
        0: ( ROAD,  ROAD,  ROAD, FIELD),
        1: ( ROAD,  ROAD, FIELD,  ROAD),
        2: ( ROAD, FIELD,  ROAD,  ROAD),
        3: (FIELD,  ROAD,  ROAD,  ROAD),
    },
}

class RotatableTile(object):
    def __init__(self, _type):
        self._type = _type
        self.orientation = 0

    def rotate(self):
        self.orientation += 1
        self.orientation %= 4

    def edge(self, direction):
        topography = TILE_ORIENTATIONS[self._type][self.orientation]
        edge_index = ORIENTATIONS[direction]
        return topography[edge_index]

    def __unicode__(self):
        topography = TILE_ORIENTATIONS[self._type][self.orientation]
        return TILES[topography]
