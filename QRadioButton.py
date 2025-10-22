from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(150, 150)
        self.setWindowTitle("QRadioButton")
    
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Wybierz system:"))
        systems = ["Android", "iOS", "Windows"]
        for system in systems:
            radio_button = QRadioButton(system)
            radio_button.toggled.connect(self.update)
            layout.addWidget(radio_button)

        self.result = QLabel("Wybrano:")
        layout.addWidget(self.result)
        
        self.setLayout(layout)
        self.show()
        
    def update(self):
        sender = self.sender()
        if sender.isChecked():
            self.result.setText(f"Wybrano: {sender.text()}")

        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    