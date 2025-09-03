import os
import subprocess

path = None

def isFlatpak(pkgStatusLb):
    if path is None:
        print('error: path is none')
        pkgStatusLb.setText("Path is None")
        pkgStatusLb.adjustSize()
        return False 
    
    real_path = os.path.realpath(path)
    result = subprocess.run(["grep", "-E", "Exec=|X-Flatpak=", real_path], capture_output=True, text=True)
    output = result.stdout

    with open(real_path) as f:
        for line in f:
            if line.startswith("X-Flatpak="):
                id = line.split("=", 1)[1].strip()
                print(id)


    if output:
        pkgStatusLb.setText(f"Package found! \n{id}")
        pkgStatusLb.adjustSize()
    else:
        pkgStatusLb.setText("Package not found.")
        pkgStatusLb.adjustSize()