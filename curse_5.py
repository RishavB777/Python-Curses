#                   <------OTHER USEFUL METHODS----->

import curses
import time
from curses import wrapper
from curses.textpad import rectangle

def main(stdscr):
    
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    YELLOW_AND_BLACK = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    #       WINDOW BORDER
    stdscr.border()
    #       TOGGLING ATTRIBUTES
    stdscr.attron(GREEN_AND_BLACK) # Works as 'on' switch
    rectangle(stdscr,1,1,10,10)
    stdscr.addstr("Hello world")
    stdscr.attroff(GREEN_AND_BLACK) # Works as 'off' switch
    #       CHANGING CURSOR LOCATION
    #stdscr.move(100,50)
    #       DISPLAYING USERKEY STROKES
    curses.echo(True)
    while True:
        key = stdscr.getkey()
        if key == 'q':
            break


wrapper(main)