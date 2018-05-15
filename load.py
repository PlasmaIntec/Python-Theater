def load(pos): # loads contents of theater.txt to pos
    temp = []
    with open("theater.txt", "r") as fileObj:
        content = fileObj.read()
        for char in content:
            if char == '\n':
                pos.append(temp)
                temp = []
            else:
                temp.append(char)
