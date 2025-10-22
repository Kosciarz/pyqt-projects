from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        
    def init_UI(self):
        self.setWindowTitle("QPixMap")
        self.resize(300, 200)
        self.setWindowIcon(QIcon("python-logo.png"))

        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label = QLabel(self)
        pixmap = QPixmap("python-logo.png")
        pixmap = pixmap.scaledToWidth(200)
        label.setPixmap(pixmap)
        layout.addWidget(label)

        self.setLayout(layout)

        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
    