from printTheatre import printTheatre
from sell import sell
from reset import reset
from stats import stats

def menu(pos):
    instruction = """Select:
(1) Display Seating Chart
(2) Sell one or more tickets
(3) Display statistics
(4) Reset program
(X) Exit program
"""
    select = raw_input(instruction)
    options = ["1","2","3","4","X"]
    if select == "1":
        printTheatre(pos)
        menu(pos)
    elif select == "2":
        sell(pos)
        menu(pos)
    elif select == "3":
        stats(pos)
        menu(pos)
    elif select == "4":
        reset(pos)
        menu(pos)
    elif select.lower() == "x":
        print("Have a bedraggled day ruffian :<")
    elif select not in options:
        print("Enter a number from 1 to 4 fool")
        menu(pos)
