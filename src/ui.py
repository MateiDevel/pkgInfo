from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel

def createLayout():
    layout = QVBoxLayout()
    title = QLabel("pkgInfo")
    layout.addWidget(title)
    return layout