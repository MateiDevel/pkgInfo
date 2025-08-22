from PyQt5.QtWidgets import QApplication

def copy(pathLb):
    clipboard = QApplication.clipboard()
    clipboard.setText(pathLb.text())