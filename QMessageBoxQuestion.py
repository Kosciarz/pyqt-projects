from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QGridLayout
from PyQt6.QtCore import Qt

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QMessageBox Question")
        self.resize(200, 150)
        
        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        button = QPushButton("Wyjdź", self)
        button.clicked.connect(self.show_question)
        layout.addWidget(button)
        
        self.setLayout(layout)
        
    def show_question(self):
        anwser = QMessageBox.question(self,
                                      "Potwierdzenie",
                                      "Czy chcesz wyjść?",
                                      QMessageBox.StandardButton.Yes |
                                      QMessageBox.StandardButton.No
        )
        
        if anwser == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self,
                                    "Informacja",
                                    "Wybrałeś TAK. Program zostanie zamknięty.",
                                    QMessageBox.StandardButton.Ok
            )
            self.close()
        else:
            QMessageBox.information(self,
                                    "Informacja",
                                    "Wybrałeś NIE.",
                                    QMessageBox.StandardButton.Ok
            )
            

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
            