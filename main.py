import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui import createUI

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("pkgInfo")
window.setFixedSize(400, 400)

createUI(window)
window.show()

sys.exit(app.exec_())