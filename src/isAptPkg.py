import os 

path = None

def isAptPkg():
    os.system(f'dpkg -l {path}')
