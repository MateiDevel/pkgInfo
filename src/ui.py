from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QFont
from src.fileChooser import fileBtn_clicked

font = QFont('Arial', 30)

def createUI(window):
    title = QLabel("pkgInfo", window)
    title.setFont(font)
    title.move(400 // 2 - 60, 0)

    pkgIcon = QLabel(window)
    pkgIcon.move(20, 70)
    pkgIcon.show()

    # File 
    fileBtn = QPushButton("File", window)
    fileBtn.move(300, 70)

    fileBtn.clicked.connect(lambda : fileBtn_clicked(pkgIcon)) # give the button a function with arguments