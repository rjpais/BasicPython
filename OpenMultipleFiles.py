# This script opens all files in a given folder that has a given extention, F]for example txt. 

import os 
from Tkinter import Tk
from tkFileDialog import askdirectory


Tk().withdraw() 
path = askdirectory(title ="Chose folder with pre-processed samples" )
FILES = os.listdir(path)                                              # gets the names of all files in 
for filename in FILES:
    extention = filename.split(".")[-1]                                # gets the extension of a file
    if extention == "txt":
        filepath = path + "/" + filename
        K = open(filepath, "r")
        print filepath
        K.close()
    
print len(FILES), " txt files found in folder"
