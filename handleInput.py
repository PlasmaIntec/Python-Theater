from printTheatre import printTheatre

def isInt(List): # checks that List is comprised only of digits
    for i in List:
        if not (i.isdigit()):
            return False
    return True

def reduceSelection(List): # strips List of characters other than digits or '-'
    temp = list()
    for i in List:
        if not(i.isdigit() or i == '-'):
            temp.append(i)
    return temp

def isOrdered(List): # checks that List is in the form %d-%d
    for i, element in enumerate(List):
        if i == 0 and not element.isdigit():
            return False
        if element == '-':
            temp = List[i+1:]
            if not isInt(temp) or len(temp) == 0:
                return False
    return True

def isSelection(List): # checks that List is in the form %d or %d-%d
    temp = reduceSelection(List)
    if len(temp) != 0 or not isOrdered(List):
        return False
    return True

def findRange(List): # given List in the form %d-%d, return selectionRange, which is a list of two digit elements
    cutPoint = 0
    for i, element in enumerate(List):
        if not element.isdigit():
            cutPoint = i
            break
    first = int(''.join(List[:cutPoint]))
    second = int(''.join(List[cutPoint+1:]))
    selectionRange = list()
    selectionRange.append(first)
    selectionRange.append(second)
    return selectionRange

def removeNewline(List): # removes newlines from List
    temp = []
    num = []
    for i in List:
        if i != '\n':
            num.append(i)
        else:
            temp.append(int(''.join(num)))
            num = []
    return temp

def handleInput(pos, row): # handles input for sell function
    List = raw_input("Purchase from which column: ")
    x = len(pos[0]) - 1
    y = len(pos) - 1
    with open("prices.txt", "r") as fileObj:
        prices = fileObj.read()
        prices = removeNewline(prices)
        cost = 0
        if isSelection(List):
            if isInt(List): # input is only number
                num = int(''.join(List))
                if num > x or num < 0:
                    print("Please enter valid column")
                    handleInput(pos, row)
                elif pos[row][num] == "#":
                    print("Seat already taken")
                    handleInput(pos, row)
                else:
                    pos[row][num] = "#"
                    cost += int(prices[row])
                    print("Cost is: %d" % cost)
            else: # input is a range      
                selectionRange = findRange(List)
                first = selectionRange[0]
                second = selectionRange[1]
                if first < 0 or first > x or second < 0 or second > x or first > second:
                    print("Please enter valid column selection")
                    handleInput(pos, row)
                else:
                    proceed = True
                    for i in range(first, second+1): # checks if seat is taken
                        if pos[row][i] == "#":
                            proceed = False
                            break
                    if proceed:
                        for i in range(first, second+1):
                            pos[row][i] = "#"
                        cost += int(prices[row]) * (second - first + 1)
                        print("Cost is: %d" % cost)
                    else:
                        print("Seat in the selection already taken")
                        handleInput(pos, row)
        else:
            print("Please enter valid selection")
            handleInput(pos, row)

