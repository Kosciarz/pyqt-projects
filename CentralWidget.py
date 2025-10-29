from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Central Widget")
        self.resize(300, 200)
        
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
