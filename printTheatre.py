from __future__ import print_function
        
def printTheatre(pos): # prints theatre arrangement
    y = len(pos)
    x = len(pos[0]) + 1    
    print("%8s " % "", end='') # %8s aligns to right
    for i in range(0,x/2 - 2):
        print(" ", end='')
    print("Seats")
    if (x > 10):
        print("%8s " % "", end='')
        for i in range(0,x-1):
            if (i % 10 == 0):
                print(i / 10, end='')
            else:
                print(" ", end='')
        print("")
    print("%8s " % "", end='')
    for i in range(0,x-1):
        print(i % 10, end='')
    print("")
    for i, row in enumerate(pos):
        print("Row  %3s " % i, end='') 
        for seat in row:
            print(seat, end='')
        print("")
