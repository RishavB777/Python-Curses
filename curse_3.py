import curses
import time
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    YELLOW_AND_BLACK = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)

    stdscr.addstr(0,50,"HELLO WORLD",curses.A_BLINK)
    stdscr.addstr(0,63,"HELLO WORLD",curses.A_BOLD)
    stdscr.addstr(1,50,"HELLO WORLD",curses.A_REVERSE)
    stdscr.addstr(1,63,"HELLO WORLD",curses.A_DIM)
    stdscr.addstr(2,57,"HELLO WORLD",curses.A_STANDOUT)
    stdscr.addstr(3,57,"HELLO WORLD",YELLOW_AND_BLACK)

    
    stdscr.addstr(4,57,"HELLO WORLD",curses.A_UNDERLINE|YELLOW_AND_BLACK)

    #       ****CREATING WINDOWS****
    """counter_win = curses.newwin(1,20,10,10)
    for i in range(50):
        counter_win.clear()
        color = YELLOW_AND_BLACK
        if i%2 == 0:
            color = GREEN_AND_BLACK
        counter_win.addstr(f"Count: {i}",color)
        time.sleep(1)
        counter_win.refresh()"""
    #       ****CREATING PADS****
    mypad = curses.newpad(100,100)
    for j in range(100):
        for i in range(26):
            char = chr(i+65)
            mypad.addstr(char,GREEN_AND_BLACK)
    for i in range(50):
    #       ****MOVING/SCROLLING PADS
        # Scrolling through the pad
        """mypad.refresh(0,i,5,5,10,25)
        time.sleep(0.5)"""
        stdscr.clear()
        stdscr.refresh()
        # Moving pad with same values
        """mypad.refresh(0,0,5,i,10,25+i)
        time.sleep(0.2)"""
        # Moving pad with different values
        """mypad.refresh(0,i,5,i,10,25+i)
        time.sleep(0.2)"""
        # Moving pad diagonally with different values
        mypad.refresh(0,i,5+i,i,10,25+i)
        time.sleep(0.2)
        
    stdscr.getch()

wrapper(main)