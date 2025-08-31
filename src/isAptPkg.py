import os 

path = None

def isAptPkg():
    # the actual file it points to after following any shortcuts or links
    real_path = os.path.realpath(path)
    os.system(f'dpkg -S {real_path}')
