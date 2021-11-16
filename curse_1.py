from curses import wrapper

def main(stdscr):
    stdscr.clear()
    #stdscr.refresh()
    stdscr.addstr(0,50,"HELLO WORLD")
    stdscr.getch()

wrapper(main)