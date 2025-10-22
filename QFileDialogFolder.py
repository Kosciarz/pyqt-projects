from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QGridLayout, QLineEdit, QLabel
from PyQt6.QtCore import Qt

from pathlib import Path

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog Folder Picker")
        self.resize(400, 150)

        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button = QPushButton("Browse", self)
        button.clicked.connect(self.open_file)
        self.dir_name_edit = QLineEdit()

        layout.addWidget(QLabel("Folder:", self), 0, 0)
        layout.addWidget(self.dir_name_edit, 0, 1)
        layout.addWidget(button, 0, 2)

        self.setLayout(layout)

    
    def open_file(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Wybierz folder")
        if dir_name:
            path = Path(dir_name)
            self.dir_name_edit.setText(str(path))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
