from PyQt6.QtWidgets import *
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__();
        self.resize(200, 100)

        layout = QVBoxLayout(self)
        self.cb_language = QComboBox()
        self.cb_language.addItems(["Python", "C++", "Java", "TypeScript"])

        self.button_submit = QPushButton("Zatwierdź")
        self.button_submit.clicked.connect(self.update)

        self.label_result = QLabel()

        layout.addWidget(self.cb_language)
        layout.addWidget(self.button_submit)
        layout.addWidget(self.label_result)

        self.show()


    def update(self):
        self.label_result.setText(f"Wybrałeś {self.cb_language.currentText()}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
