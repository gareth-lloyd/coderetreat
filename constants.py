# -*- coding: utf-8 -*-
FIELD = 0
ROAD = 1

# These are some useful unicode characters, organized according to
# a rudimentary coding system which you can use or improve.
TILES = {
#    N      E      S      W
    (FIELD, FIELD, FIELD, FIELD) : u'.', # cloisters

    ( ROAD, FIELD,  ROAD, FIELD) : u'│',
    (FIELD,  ROAD, FIELD,  ROAD) : u'─',

    ( ROAD,  ROAD, FIELD, FIELD) : u'└',
    ( ROAD, FIELD, FIELD,  ROAD) : u'┘',
    (FIELD, FIELD,  ROAD,  ROAD) : u'┐',
    (FIELD,  ROAD,  ROAD, FIELD) : u'┌',

    ( ROAD,  ROAD,  ROAD, FIELD) : u'├',
    ( ROAD,  ROAD, FIELD,  ROAD) : u'┴',
    ( ROAD, FIELD,  ROAD,  ROAD) : u'┤',
    (FIELD,  ROAD,  ROAD,  ROAD) : u'┬',
}
