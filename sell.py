from handleInput import handleInput

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

def isFull(pos, row): # returns true if a row is full and false otherwise
    for i in pos[row]:
        if i == '*':
            return False
    return True

def sell(pos): # processes the sales process
    x = len(pos[0]) - 1
    y = len(pos) - 1
    try:
        row = int(raw_input("Purchase from which row: "))
    except ValueError:
        print("Please enter number")
        sell(pos)
    else:
        if row > y or row < 0:
                print("Please enter valid row")
                sell(pos)
        else:
            if isFull(pos, row):
                print("Row is full")
                sell(pos)
            else:
                handleInput(pos, row)
