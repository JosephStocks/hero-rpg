import io
from contextlib import redirect_stdout
from curses_utilities import print_centered_string
from time import sleep
import curses

def main_screen(screen):
    curses.noecho()
    curses.curs_set(0)
    while True:
        f = io.StringIO()
        with redirect_stdout(f):
            print("This is a test of its capabilities!\n" * 2 + 
                "This is a test of its capabilities!")
            print("\nHere is some new stuff!!")
        input_str = f.getvalue()
        win1 = print_centered_string(input_str)

        screen.refresh()
        win1.refresh()
        key = screen.getch()

        if key == ord('q'):
            break
        else:
            sleep(0.25)

curses.wrapper(main_screen)

class WindowDraw:
    def __init__(self, screen):
        self.f = io.StringIO()
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        screen.refresh()
        win1.refresh()