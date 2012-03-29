# -*- coding: utf-8 -*-
import locale, curses, time

class Display(object):
    """
    Example Usage:
    with Display() as display:
        while True:
            for x, y, tile in tiles:
                display.place_char(unicode(tile), x, y)
            display.refresh(sleep_time=0.1)
    """
    def __enter__(self):
        locale.setlocale(locale.LC_ALL, '')
        self.encoding = locale.getpreferredencoding()

        self.window = curses.initscr()
        self.height, self.width = self.window.getmaxyx()
        self.center_x, self.center_y = self.width / 2, self.height / 2
        return self

    def __exit__(self, type, value, traceback):
        curses.endwin()

    def place_char(self, ch, x, y):
        """Call this method for each character that you want to place within
        a particular frame.

        ch must be an 8-bit or unicode string of length 1

        The x/y space is a grid with 0, 0 at the centre of the screen. The x
        and y args can be arbitrarily large positive or negative numbers: only
        points within the window will be drawn.
        """
        # the window's vertical axis grows from top to bottom
        y *= -1
        y += self.center_y
        x += self.center_x

        if 0 < x < self.width  and 0 < y < self.height:
            self.window.addstr(y, x, ch.encode(self.encoding))

    def refresh(self, sleep_time=0.1):
        self.window.refresh()
        time.sleep(sleep_time)
        self.window.clear()
