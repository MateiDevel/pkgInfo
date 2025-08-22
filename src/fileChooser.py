from PyQt5.QtWidgets import QFileDialog, QFileIconProvider
from PyQt5.QtCore import QFileInfo

def fileBtn_clicked(pkgIcon, fileLb, pathLb):
    file_path, _ = QFileDialog.getOpenFileName(
        None,
        "Select Package or file",
        "",
        "All Files(*)"
    )

    if file_path:

        info = QFileInfo(file_path)
        getter = QFileIconProvider()
        icon = getter.icon(info)
        name = info.fileName()
        pixmap = icon.pixmap(64, 64) # using pixmap bcs its optimized , qimage is used for manipulating the pixels of the image.

        fileLb.setText(name)
        fileLb.adjustSize()

        pathLb.setText(file_path)
        pathLb.adjustSize()

        pkgIcon.setPixmap(pixmap)
        pkgIcon.adjustSize()

        print(file_path)
