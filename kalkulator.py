from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit

import sys

class Kalkulator(QWidget):
    def __init__(self):
        super().__init__()
        buttons = ['7', '8', '9', '+', 
                        '4', '5', '6', '-', 
                        '1', '2', '3', '=',]
        
        layout = QGridLayout(self)
        layout.addWidget(QLineEdit(), 0, 0, 1, 4)
        
        for i in range(len(buttons)):
            layout.addWidget(QPushButton(buttons[i]), i // 4 + 1, i % 4)
            
        layout.addWidget(QPushButton('0'), 4, 0, 1, 2)
        
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    kalkulator = Kalkulator()
    sys.exit(app.exec())