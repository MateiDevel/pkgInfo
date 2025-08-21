from PyQt5.QtWidgets import QLabel, QFileDialog, QFileIconProvider
from PyQt5.QtCore import QFileInfo

def fileBtn_clicked(window):
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

        pixmap = icon.pixmap(64, 64) # using pixmap bcs its optimized , qimage is used for manipulating the pixels of the image.
       
        pkgIcon = QLabel(window)
        pkgIcon.move(20, 70)
        pkgIcon.setPixmap(pixmap)
        pkgIcon.show()

        print(file_path)
