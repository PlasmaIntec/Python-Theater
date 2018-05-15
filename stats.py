from handleInput import removeNewline

def stats(pos): # displays stats on seats sold, seats left, and revenue from sales
    sold = 0
    left = 0
    revenue = 0
    for row in pos:
        for seat in row:
            if seat == '#':
                sold += 1
            elif seat == '*':
                left += 1
    with open("prices.txt", "r") as fileObj:
        prices = fileObj.read()
        prices = removeNewline(prices)
        for i, row in enumerate(pos):
            for seat in row:
                if seat == '#':
                    revenue += prices[i]
    print("Total seats sold: %d" % sold)
    print("Total seats left: %d" % left)
    print("Total revenue: %d" % revenue)
