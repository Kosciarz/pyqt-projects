from PyQt6.QtWidgets import *

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        top_layout = QHBoxLayout()
        top_layout.addWidget(QPushButton("Lewy"))
        top_layout.addWidget(QPushButton("Prawy"))

        bottom_layout = QVBoxLayout()
        bottom_layout.addWidget(QPushButton("Dół1"))
        bottom_layout.addWidget(QPushButton("Dół2"))

        main_layout = QVBoxLayout(self)
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())