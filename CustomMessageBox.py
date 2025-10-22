from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QGridLayout
from PyQt6.QtCore import Qt

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Message Box")
        self.resize(200, 150)
        
        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        button = QPushButton("Pytanie", self)
        button.clicked.connect(self.show_question)
        layout.addWidget(button)
        
        self.setLayout(layout)
        
    def show_question(self):
        question = QMessageBox(self)
        question.setWindowTitle("Pytanie")
        question.setText("Czy chcesz wyjść?")
        yes_button = question.addButton("Tak", QMessageBox.ButtonRole.YesRole)
        _ = question.addButton("Nie", QMessageBox.ButtonRole.NoRole)
        question.exec()
        
        if question.clickedButton() == yes_button:
            self.close()
        else:
            print("Wybrałeś NIE.")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
    
if __name__ == "__main__":
    main()
