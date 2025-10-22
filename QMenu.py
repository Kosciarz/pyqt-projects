from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon

import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_IU()
        self.show()
        
    def init_IU(self):
        self.setWindowTitle("QMenu")
        self.setWindowIcon(QIcon("python-logo.png"))
        self.setGeometry(200, 200, 600, 400)

        button = QPushButton("Click", self)
        button.setGeometry(100, 100, 100, 50)
        button.setIcon(QIcon("python-logo.png"))

        menu = QMenu()
        menu.addAction("Cut")
        menu.addAction("Copy")
        menu.addSeparator()
        menu.addAction("Paste")
        
        button.setMenu(menu)
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()