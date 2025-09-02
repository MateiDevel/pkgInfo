<table align='center', width='100%'>
  <tr>
    <td align='left'>
      <img src='icon.png', style="width: 320px; height: 200px;">
    </td> 
    <td align='center'>
      <h1>pkgInfo</h1>
      <h2>An obviously open-source viewer for Linux Distro packages of package managers.</h2>
    </td>
    </tr>
</table>

# A simple app (still in development)
**Built with PyQt5**

Simply add the path of a file and the app will search for its Package (Currently only APT packages work)

# Setup
Debian-based distros:
```
sudo apt install python3-venv python3-pip
python3 -m venv myenv
source myenv/bin/activate
pip install PyQt5
```
- Run with:
```
python main.py
```

# Coming soon
- Flatpak support
