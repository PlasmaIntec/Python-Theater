import os
from menu import menu
from printTheatre import printTheatre
from reset import reset
from save import save
from load import load

pos = []
temp = []

f = open("theater.txt", "a+") # if theater.txt does not exist, create theater.txt

if os.stat("theater.txt").st_size == 0: # if theater.txt is empty, create pos
    reset(pos)
    print("Instantiated theater.txt")

else: # else load pos from theater.txt
    load(pos)
    print("Loaded theater.txt")

menu(pos) # run program

save(pos) # save pos to theater.txt
