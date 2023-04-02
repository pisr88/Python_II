import os

path = '.\\Python II\\2-13.txt'

def readFile(path):
    with open(path,"r") as f:
        t = f.read()
        i = len(t.split(" "))
        return i


os.path.isfile(path) and print(readFile(path))