from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QGridLayout
from PyQt6.QtCore import Qt

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setWindowTitle("Wyrażanie zgody")
        self.setGeometry(100, 100, 300, 200)
        layout = QGridLayout(self)
        
        self.checkbox = QCheckBox("Wyrażam zgodę", self)
        self.checkbox.stateChanged.connect(self.show_state)
        layout.addWidget(self.checkbox, 0, 0, Qt.AlignmentFlag.AlignCenter)
        
    def show_state(self, state):
        print(f"Stan checkboxa: {Qt.CheckState(state)}")
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())