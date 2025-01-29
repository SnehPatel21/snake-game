import curses

class InputHandler:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def get_input(self):
        key = self.stdscr.getch()
        if key == curses.KEY_UP:
            return 'UP'
        elif key == curses.KEY_DOWN:
            return 'DOWN'
        elif key == curses.KEY_LEFT:
            return 'LEFT'
        elif key == curses.KEY_RIGHT:
            return 'RIGHT'
        elif key == ord('q'):
            return 'QUIT'
        return None
