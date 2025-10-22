from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QSpinBox, QLabel
from PyQt6.QtCore import Qt

import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        
    def init_UI(self):
        self.setWindowTitle("QSpinBox")
        self.resize(200, 150)
        
        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(1, 10)
        self.spinbox.setSingleStep(1)
        self.spinbox.setValue(5)
        
        self.label = QLabel(f"Wybrana liczba: {self.spinbox.value()}")
        self.spinbox.valueChanged.connect(self.update_value)
        
        layout.addWidget(self.spinbox)
        layout.addWidget(self.label)
        
        self.setLayout(layout)

    def update_value(self, value: int):
        self.label.setText(f"Wybrana liczba: {value}")

    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
    