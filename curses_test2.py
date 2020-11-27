import curses
import os
from time import sleep

def return_starting_screen():
    return r"""
   _____ _                 _        _____       _   _                 
  / ____(_)               | |      |  __ \     | | | |                
 | (___  _ _ __ ___  _ __ | | ___  | |__) |   _| |_| |__   ___  _ __  
  \___ \| | '_ ` _ \| '_ \| |/ _ \ |  ___/ | | | __| '_ \ / _ \| '_ \ 
  ____) | | | | | | | |_) | |  __/ | |   | |_| | |_| | | | (_) | | | |
 |_____/|_|_| |_| |_| .__/|_|\___| |_|    \__, |\__|_| |_|\___/|_| |_|
                    | |                    __/ |                      
                    |_|                   |___/                       
          _____  _____   _____      _____                      
         |  __ \|  __ \ / ____|    / ____|                     
         | |__) | |__) | |  __    | |  __  __ _ _ __ ___   ___ 
         |  _  /|  ___/| | |_ |   | | |_ |/ _` | '_ ` _ \ / _ \
         | | \ \| |    | |__| |   | |__| | (_| | | | | | |  __/
         |_|  \_\_|     \_____|    \_____|\__,_|_| |_| |_|\___|
                                                               
                                                               
                              _,.
                            ,` -.)
                           ( _/-\\-._
                          /,|`--._,-^|            ,
                          \_| |`-._/||          ,'|
                            |  `-, / |         /  /
                            |     || |        /  /
                             `r-._||/   __   /  /
                         __,-<_     )`-/  `./  /
                        '  \   `---'   \   /  /
                            |           |./  /
                            /           //  /
                        \_/' \         |/  /
                         |    |   _,^-'/  /
                         |    , ``  (\/  /_
                          \,.->._    \X-=/^
                          (  /   `-._//^`
                           `Y-.____(__}
                            |     {__)
                                  ()
    """

def widest_width(input_str):
    return len(max(input_str.split("\n"), key=len))

def string_height(input_str):
    return input_str.count("\n") + 1

def print_centered_string(string_input, offset=(0, 0)):
    x_offset, y_offset = offset
    cols, lines = os.get_terminal_size()
    center_col = cols // 2 - 1
    center_line = lines // 2 - 1
    width = widest_width(string_input) + 1
    height = string_height(string_input) + 1
    starting_col = center_col - widest_width(string_input) // 2 + x_offset
    starting_line = center_line - string_height(string_input) // 2 - y_offset
    win1 = curses.newwin(height,
                               width, 
                               starting_line, 
                               starting_col)
    win1.addstr(0, 0, string_input)
    return win1

def main(screen):
    curses.noecho()
    curses.curs_set(0)
    while True:
        input_str = return_starting_screen()
        win1 = print_centered_string(input_str)
        screen.refresh()
        win1.refresh()
        key = screen.getch()
        del win1

        if key == ord('q'):
            break
        else:
            sleep(0.25)
curses.wrapper(main)