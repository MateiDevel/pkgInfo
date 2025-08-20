import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui import createLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("pkgInfo")
window.setFixedSize(400, 400)

layout = createLayout()
window.setLayout(layout)
window.show()

sys.exit(app.exec_())