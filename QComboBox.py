from PyQt6.QtWidgets import *
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout(self)
        self.cb_platform = QComboBox()
        self.cb_platform.addItems(["Android", "iOS", "Windows"])
        self.cb_platform.activated.connect(self.update)

        self.label_result = QLabel()

        layout.addWidget(QLabel("Wybierz platformę"))
        layout.addWidget(self.cb_platform)
        layout.addWidget(self.label_result)

        self.show()


    def update(self):
        self.label_result.setText(f"Wybrałeś {self.cb_platform.currentText()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
