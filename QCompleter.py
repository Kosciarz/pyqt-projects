from PyQt6.QtWidgets import QApplication, QWidget, QCompleter, QLineEdit, QVBoxLayout

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.show()
        
    def init_UI(self):
        self.setWindowTitle("QCompleter Example")
        self.setGeometry(50, 50, 200, 150)
        layout = QVBoxLayout()
        
        fruits = QCompleter(["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"])
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Type a fruit name...")
        line_edit.setClearButtonEnabled(True)
        line_edit.setCompleter(fruits)
        layout.addWidget(line_edit)
        
        self.setLayout(layout)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    