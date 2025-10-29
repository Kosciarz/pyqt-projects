from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMenuBar")
        self.resize(200, 150)
        
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&Plik")
        edit_menu = menu_bar.addMenu("&Edycja")
        help_menu = menu_bar.addMenu("&Pomoc")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
        
        
if __name__ == "__main__":
    main()
    