import curses
from time import sleep

def main(stdscr):
    curses.echo()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(True)
    while True:
        stdscr.erase()

        stdscr.addstr(5, 5, 'Hello from Curses!', curses.A_BOLD)
        stdscr.addstr(6, 5, 'Press q to close this screen', curses.A_STANDOUT)

        stdscr.refresh()
        key = stdscr.getch()

        if key == ord('a'):
            continue
        elif key == ord('q'):
            break
        else:
            sleep(1)

curses.wrapper(main)