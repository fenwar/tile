#!/usr/bin/env python2

import sys

from gi.repository import Gtk, Wnck



def tile_to_left(win, screen):
    # work out desired horizontal dimensions:
    win.set_geometry(
        Wnck.WindowGravity.NORTHWEST,
        (
            Wnck.WindowMoveResizeMask.WIDTH |
            Wnck.WindowMoveResizeMask.X
        ),
        0,
        0,
        int(screen.get_width() / 2),
        0,
    )
    # just maximize vertically
    win.maximize_vertically()
    

def tile_to_right(win, screen):
    win.set_geometry(
        Wnck.WindowGravity.NORTHEAST,
        (
            Wnck.WindowMoveResizeMask.WIDTH |
            Wnck.WindowMoveResizeMask.X
        ),
        screen.get_width(),
        0,
        int(screen.get_width() / 2),
        0,
    )



if __name__ == "__main__":

    screen = Wnck.Screen.get_default()
    screen.force_update()

    # window_list = screen.get_windows()
    active_window = screen.get_active_window()

    if sys.argv[1] == "left":
        tile_to_left(active_window, screen)
    elif sys.argv[1] == "right":
        tile_to_right(active_window, screen)
