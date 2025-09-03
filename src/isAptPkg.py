import os
import subprocess

path = None

def isAptPkg(pkgStatusLb):
    if path is None:
        print('error: path is none')
        pkgStatusLb.setText("Path is None")
        pkgStatusLb.adjustSize()
        return False

    # the actual file it points to after following any shortcuts or links
    real_path = os.path.realpath(path)
    result = subprocess.run(["dpkg", "-S", real_path], capture_output=True, text=True)
    output = result.stdout
    print(output)

    if output:
        pkgStatusLb.setText(f"Package found! \n{output}")
        pkgStatusLb.adjustSize()
    else:
        pkgStatusLb.setText("Package not found.")
        pkgStatusLb.adjustSize()