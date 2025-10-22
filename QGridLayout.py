from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.show()
        
    def init_UI(self):
        self.setWindowTitle("QGridLayout Example")
        self.resize(300, 200)
        
        layout = QGridLayout(self)
        
        blue_label = QLabel()
        blue_label.setStyleSheet("background-color: blue;")
        
        red_label = QLabel()
        red_label.setStyleSheet("background-color: red;")
        
        green_label = QLabel()
        green_label.setStyleSheet("background-color: green;")
        
        layout.addWidget(blue_label, 0, 0)
        layout.addWidget(red_label, 0, 1)
        layout.addWidget(green_label, 1, 3)
        
        self.setLayout(layout)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    