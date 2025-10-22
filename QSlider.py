from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QGridLayout, QLabel
from PyQt6.QtCore import Qt

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        
    def init_UI(self):
        self.setWindowTitle("QSlider")
        self.resize(300, 150)
        
        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.slider = QSlider(self)
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setSingleStep(5)
        self.slider.setValue(50)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(20)
        self.slider.valueChanged.connect(self.update_value)

        self.label = QLabel(f"Wybrana liczba: {self.slider.value()}")

        layout.addWidget(self.slider)
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