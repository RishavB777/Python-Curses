#                   <------USER INPUT AND TEXTBOXES----->

import curses
import time
from curses import wrapper
from curses.textpad import Textbox,rectangle

def main(stdscr):
    
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    YELLOW_AND_BLACK = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)


    #       ****GETTING USER KEYSTROKES****
    """key = stdscr.getkey() # Returns the key we typed
    stdscr.addstr(25,25,f"Key:{key}")"""

    """x,y=(0,0)
    x_STRING = 0
    while True:
    #       ****KEYSTROKES WITOUT DELAY
        stdscr.nodelay(True)
        try:
            key = stdscr.getkey()
        except:
            key = None
        if key == "KEY_UP":
            y-=1
        elif key == "KEY_DOWN":
            y+=1
        elif key == "KEY_RIGHT":
            x+=1
        elif key == "KEY_LEFT":
            x-=1
        stdscr.clear()
        x_STRING+=1
        stdscr.addstr(0,x_STRING//50,"HELLO WORLD")
        
        stdscr.addstr(y,x,"RB")
        stdscr.refresh()
"""
           
    #       ****TEXTBOXES AND USER INPUT****
    stdscr.clear()
    win = curses.newwin(8,8,2,2)
    box = Textbox(win) # Creates a textbox the size of the window
    rectangle(stdscr,1,1,10,10)
    stdscr.refresh()
    box.edit() # Lets the user edit the the textbox
    # Hit CTRL+G to exit th textbox
    text = box.gather().replace("\n","") # Gather the contents of the textbox
    stdscr.addstr(10,40,text)
    stdscr.getch()

wrapper(main)