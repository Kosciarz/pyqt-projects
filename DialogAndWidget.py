from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QDialog, QGridLayout
from PyQt6.QtCore import Qt

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog and Widget")
        
        layout = QHBoxLayout(self)
        
        button_dialog = QPushButton("Otwórz dialog", self)
        button_dialog.clicked.connect(self.show_dialog)
        
        button_widget = QPushButton("Otwórz widget", self)
        button_widget.clicked.connect(self.show_widget)
        
        layout.addWidget(button_dialog)
        layout.addWidget(button_widget)
        self.setLayout(layout)

    def show_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dialog")
        
        label = QLabel("Message from the dialog")
        
        dialog_layout = QGridLayout()
        dialog_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dialog_layout.addWidget(label)
        
        dialog.setLayout(dialog_layout)
        dialog.exec()
        
    def show_widget(self):
        self.widget = QWidget()
        self.widget.setWindowTitle("Widget")
        
        label = QLabel("Message from the widget")
        
        widget_layout = QGridLayout()
        widget_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget_layout.addWidget(label)
        
        self.widget.setLayout(widget_layout)
        self.widget.show()
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()