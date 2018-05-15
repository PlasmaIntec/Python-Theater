class Error(Exception):
    """Base class for exceptions in this module."""
    pass

def priceSet(row, currentRow, fileObj): # allows for stepwise progression
    price = raw_input("Enter price for row %d: " % currentRow)
    try:
        int(price)
        if int(price) < 1:
            raise Error
    except ValueError:
        print("Please enter number")
        priceSet(row, currentRow, fileObj)
    except Error:
        print("Please enter positive number")
        priceSet(row, currentRow, fileObj)
    else:
        fileObj.write("%d\n" % int(price))

def reset(pos):
    with open("theater.txt", "w+") as fileObj: # resets theater.txt
        print("Reset theater.txt")
    row = raw_input("Enter row: ")
    column = raw_input("Enter column: ")
    try:
        int(row)
        int(column)
        if int(row) < 1 or int(column) < 1:
            raise Error

        del pos[:]
        temp = []

        for i in range(0,int(row)): # sets pos
            for j in range(0,int(column)):
                temp.append("*")
            pos.append(temp)
            temp = []

        with open("prices.txt", "w") as fileObj: # set row prices
            for i in range(0, int(row)):
                priceSet(int(row), i, fileObj)
    except ValueError:
        print("Please enter number")
        reset(pos)
    except Error:
        print("Please enter positive number")
        reset(pos)
    except OverflowError:
        print("Please enter small enough number")
