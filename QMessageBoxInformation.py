from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QGridLayout, QPushButton
from PyQt6.QtCore import Qt

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox Information")
        self.resize(300, 150)
        
        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        button_info = QPushButton("Informacja", self)
        button_info.clicked.connect(self.show_info)
        layout.addWidget(button_info)
        
        self.setLayout(layout)         
        
    def show_info(self):
        QMessageBox.information(self, "Informacja", "Moja pierwsza informacja")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
    
if __name__ == "__main__":
    main()
    