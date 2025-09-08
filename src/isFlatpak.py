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

    id = None
    try:
         with open(real_path) as f:
            for line in f:
                if line.startswith("X-Flatpak="):
                    id = line.split("=", 1)[1].strip()
                    result = subprocess.run(["flatpak", "info" , id], capture_output=True, text=True)
                    output = result.stdout
                    print(output)
                    break
    except Exception:
        return False


    if id:
        pkgStatusLb.setText(f"Package found! \n{id}")
        pkgStatusLb.adjustSize()
    else:
        pkgStatusLb.setText("Not a flatpak")
        pkgStatusLb.adjustSize()
        return False