#!/usr/bin/env python2

import sys

from gi.repository import Gtk, Wnck


def set_width(win, w):
    win.set_geometry(
        None, Wnck.WindowMoveResizeMask.WIDTH,
        0, 0,
        w, 0,
    )


def set_height(win, h):
    win.set_geometry(
        None, Wnck.WindowMoveResizeMask.HEIGHT,
        0, 0,
        0, h,
    )

def move_to(win, x, y):
    win.set_geometry(
        Wnck.WindowGravity.NORTHWEST,
        Wnck.WindowMoveResizeMask.X | Wnck.WindowMoveResizeMask.Y,
        x, y,
        0, 0,
    )


def tile_to_left(win, screen):
    # work out desired horizontal dimensions:
    set_width(win, int(screen.get_width() / 2)
    set_height(win, screen.get_height())
    move_to(win, 0, 0)
    

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
