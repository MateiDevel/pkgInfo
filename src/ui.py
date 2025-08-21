from PyQt5.QtWidgets import QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QFont

font = QFont('Arial', 30)

def createUI(window):
    title = QLabel("pkgInfo", window)
    title.setFont(font)
    title.move(400 // 2 - 60, 0)

    # File 
    fileBtn = QPushButton("File", window)
    fileBtn.move(300, 70)

    def fileBtn_clicked():
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Select Package or file",
            "",
            "All Files(*)"
        )

        if file_path:
            print(file_path)

    fileBtn.clicked.connect(fileBtn_clicked)
