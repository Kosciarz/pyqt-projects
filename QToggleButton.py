from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_IU()
        self.show()
        
    def init_IU(self):
        self.setWindowTitle("QToggleButton")
        self.resize(300, 200)
        
        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        button = QPushButton("Click", self)
        button.setCheckable(True)
        button.clicked.connect(self.show_status)
        button.resize(100, 50)
        button.setIcon(QIcon("python-logo.png"))
        layout.addWidget(button)
        
        self.setLayout(layout)
        
    def show_status(self, checked: bool):
        print(checked)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()