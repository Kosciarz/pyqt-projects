from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt

import sys

class ConsentForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.show()
        
    def init_UI(self):
        self.setWindowTitle("Consent Form")
        self.resize(200, 150)
        layout = QVBoxLayout(self)
        
        top_layout = QGridLayout()
        top_layout.addWidget(QCheckBox("Wyrażam zgodę"), 0, 0, Qt.AlignmentFlag.AlignCenter)
        
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(QPushButton("Zatwierdź"))
        bottom_layout.addWidget(QPushButton("Anuluj"))
        
        layout.addLayout(top_layout)
        layout.addLayout(bottom_layout)
        
        self.setLayout(layout)
        
    def show_state(self, state):
        print(f"Checkbox state: {Qt.CheckState(state).name}")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConsentForm()
    sys.exit(app.exec())