import curses
from .renderer import Renderer

class TerminalRenderer(Renderer):
    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)
        self.stdscr.nodelay(1)
        self.stdscr.timeout(100)

    def render(self, game_state):
        self.stdscr.clear()
        for y, row in enumerate(game_state):
            for x, cell in enumerate(row):
                if cell:
                    self.stdscr.addstr(y, x, '#')
        self.stdscr.refresh()
