from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QLineEdit, QLabel, QFileDialog

from pathlib import Path

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog with button")
        self.resize(200, 150)
        
        layout = QGridLayout(self)
        
        file_browse = QPushButton("Browse", self)
        file_browse.clicked.connect(self.browse_files)
        
        self.filename_edit = QLineEdit(self)
        
        layout.addWidget(QLabel("File: ", self), 0, 0)
        layout.addWidget(self.filename_edit, 0, 1)
        layout.addWidget(file_browse, 0, 2)
        
    def browse_files(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Wybierz plik",
            "C:/Users/barto/Pictures",
            "Images (*.png *.jpg)"
        )
        
        if filename:
            path = Path(filename)
            self.filename_edit.setText(str(path))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
   main() 
