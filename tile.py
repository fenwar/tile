#!/usr/bin/env python2

from gi.repository import Gtk, Wnck


if __name__ == "__main__":

    screen = Wnck.Screen.get_default()
    screen.force_update()

    # window_list = screen.get_windows()
    active_window = screen.get_active_window()

    print dir(active_window)
