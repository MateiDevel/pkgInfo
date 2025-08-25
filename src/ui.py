from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QFileIconProvider
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QFileInfo
from src.fileChooser import fileBtn_clicked
from src.copyPath import copy
from src.isAptPkg import isAptPkg
import os

font = QFont('Arial', 30)
file_path = None


def createUI(window):
    icon_path = os.path.join(os.path.dirname(__file__), "assets/icon.jpg")
    placeHolder = QPixmap(icon_path)  

    if placeHolder.isNull():
        print("not imported")
    else:
        print("imported")

    title = QLabel("pkgInfo", window)
    title.setFont(font)
    title.move(400 // 2 - 60, 0)

    pkgIcon = QLabel(window)
    pkgIcon.move(20, 70)
    pkgIcon.setPixmap(placeHolder)
    pkgIcon.resize(64, 64)
    pkgIcon.show()

    fileLb = QLabel('Pkg/File Title', window)
    fileLb.move(90, 70)
    fileLb.show()

    pathLb = QLineEdit(window)
    pathLb.setPlaceholderText("Path")
    pathLb.setText(file_path)
    pathLb.move(90, 100)

    def pathChange():
        currentPath = pathLb.text()
        if currentPath:
            info = QFileInfo(currentPath)
            getter = QFileIconProvider()
            icon = getter.icon(info)
            name = info.fileName()
            pixmap = icon.pixmap(64, 64) # using pixmap bcs its optimized , qimage is used for manipulating the pixels of the image.

            fileLb.setText(name)
            fileLb.adjustSize()

            pathLb.setText(currentPath)
            pathLb.adjustSize()
            pathLb.show()
            copyBtn.show()

            pkgIcon.setPixmap(pixmap)
            pkgIcon.adjustSize()

            print(currentPath)

    pathLb.textChanged.connect(pathChange)
    pathLb.show()

    copyBtn = QPushButton("Copy", window)
    copyBtn.move(240, 100)
    copyBtn.show()

    # File 
    fileBtn = QPushButton("File", window)
    fileBtn.move(300, 70)

    fileBtn.clicked.connect(lambda : (fileBtn_clicked(pkgIcon, fileLb, pathLb, copyBtn), isAptPkg()))# give the button a function with arguments
    copyBtn.clicked.connect(lambda : copy(pathLb))