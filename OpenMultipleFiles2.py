import os
from tkinter import *
from tkinter import filedialog

Tk().withdraw()
path = filedialog.askdirectory(title ="Chose folder with data" )
FILES = os.listdir(path)                                              # gets the names of all files in
nTxt = 0
for filename in FILES:
    extention = filename.split(".")[-1]                                # gets the extension of a file
    if extention == "txt":
        filepath = path + "/" + filename
        K = open(filepath, "r")
        print (filepath)
        K.close()
        nTxt = nTxt + 1

print (str(nTxt) + " files founds in folder")
