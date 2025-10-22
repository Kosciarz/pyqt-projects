from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QGridLayout
from PyQt6.QtCore import Qt

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog")
        self.resize(300, 150)
        
        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        button = QPushButton("Zmień nazwę", self)
        button.clicked.connect(self.show_input_dialog)
        layout.addWidget(button)
        
        self.setLayout(layout)
        
    def show_input_dialog(self):
        title, ok = QInputDialog.getText(self, "Zmień nazwę", "Nowa nazwa:")
        if ok and title:
            self.setWindowTitle(title)

            
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
