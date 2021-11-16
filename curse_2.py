#                   <------ATTRIBUTES AND COLORS----->


import curses
import time
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    
    #       ****ADDING COLORS****
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    YELLOW_AND_BLACK = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)

    #      ****TEXT STYLING WITH ATTRIBUTES****
    stdscr.addstr(0,50,"HELLO WORLD",curses.A_BLINK)
    stdscr.addstr(0,63,"HELLO WORLD",curses.A_BOLD)
    stdscr.addstr(1,50,"HELLO WORLD",curses.A_REVERSE)
    stdscr.addstr(1,63,"HELLO WORLD",curses.A_DIM)
    stdscr.addstr(2,57,"HELLO WORLD",curses.A_STANDOUT)
    stdscr.addstr(3,57,"HELLO WORLD",YELLOW_AND_BLACK)

    #       ****COMBINING TWO ATTRIBUTES****
    stdscr.addstr(4,57,"HELLO WORLD",curses.A_UNDERLINE|YELLOW_AND_BLACK)

    #       ****UPDATING THE SCREEN LIVE****
    for i in range(50):
        stdscr.clear()
        color = YELLOW_AND_BLACK
        if i%2 == 0:
            color = GREEN_AND_BLACK
        stdscr.addstr(f"Count: {i}",color)
        time.sleep(1)
        stdscr.refresh()

    stdscr.getch()

wrapper(main)