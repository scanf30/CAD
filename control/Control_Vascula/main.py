#! /usr/bin/python3
from fileManage import fileMAngage

if __name__ == "__main__":
    file = fileMAngage()
    kilos = 1
    while (kilos > 0):
        kilos = float(input("kilos pesados  "))
        if (kilos > 0):
            file.addCount(kilos)
        else:
            print ("File created")
            file.closeFile()