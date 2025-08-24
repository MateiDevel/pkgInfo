from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont
from src.fileChooser import fileBtn_clicked
from src.copyPath import copy
from src.isAptPkg import isAptPkg

font = QFont('Arial', 30)

def createUI(window):
    title = QLabel("pkgInfo", window)
    title.setFont(font)
    title.move(400 // 2 - 60, 0)

    pkgIcon = QLabel(window)
    pkgIcon.move(20, 70)
    pkgIcon.show()

    fileLb = QLabel(window)
    fileLb.move(90, 70)
    fileLb.show()

    pathLb = QLineEdit(window)
    pathLb.move(90, 100)
    pathLb.hide()

    copyBtn = QPushButton("Copy", window)
    copyBtn.move(240, 100)
    copyBtn.hide()

    # File 
    fileBtn = QPushButton("File", window)
    fileBtn.move(300, 70)

    fileBtn.clicked.connect(lambda : (fileBtn_clicked(pkgIcon, fileLb, pathLb, copyBtn), isAptPkg()))# give the button a function with arguments
    copyBtn.clicked.connect(lambda : copy(pathLb))