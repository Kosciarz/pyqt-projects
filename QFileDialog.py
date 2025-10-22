from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QGridLayout
from PyQt6.QtCore import Qt

from pathlib import Path

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog")
        self.resize(200, 150)
        
        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        button = QPushButton("Wybierz plik")
        button.clicked.connect(self.show_file_dialog)
        layout.addWidget(button)
        
        self.setLayout(layout)
        
    def show_file_dialog(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Wybierz plik",
            "C:/Users/barto/pictures",
            "Images (*.png *.jpg)"
        )

        if filename:
            path = Path(filename)
            print(str(path))
            

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()
    
