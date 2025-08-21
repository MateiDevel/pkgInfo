from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QFont
from src.fileChooser import fileBtn_clicked

font = QFont('Arial', 30)

def createUI(window):
    title = QLabel("pkgInfo", window)
    title.setFont(font)
    title.move(400 // 2 - 60, 0)

    # File 
    fileBtn = QPushButton("File", window)
    fileBtn.move(300, 70)

    fileBtn.clicked.connect(lambda : fileBtn_clicked(window=window)) # give the button a function with arguments