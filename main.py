import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon
from src.ui import createUI

app = QApplication(sys.argv)

icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
print("icon:",os.path.exists(icon_path))

window = QWidget()
window.setWindowTitle("pkgInfo")
window.setFixedSize(400, 400)
window.setWindowIcon(QIcon(icon_path))

createUI(window)
window.show()

sys.exit(app.exec_())