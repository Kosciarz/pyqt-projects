from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QDialog, QLabel, QMainWindow
from PyQt6.QtCore import Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Dialog Box")
        self.resize(300, 200)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        dialog_button = QPushButton("Show Dialog")
        dialog_button.clicked.connect(self.show_dialog)
        
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(dialog_button)
        central_widget.setLayout(layout)
        
    def show_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dialog Box")
        
        label = QLabel("This is a message in the dialog box.", self)
        
        dialog_layout = QGridLayout()
        dialog_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dialog_layout.addWidget(label)

        dialog.setLayout(dialog_layout)
        dialog.exec()
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
