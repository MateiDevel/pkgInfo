import os 

path = None

def isAptPkg():
    os.system(f'dpkg -S {path}')
