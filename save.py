def save(pos): # saves contents of pos to theater.txt
    print("Saving to file")
    with open("theater.txt", "w") as fileObj: 
        for row in pos:
            for seat in row:
                fileObj.write(seat)
            if '*' or '#' in row:
                fileObj.write('\n')

