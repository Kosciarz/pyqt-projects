from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QTimeEdit
from PyQt6.QtCore import Qt, QTime

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        
    def init_UI(self):
        self.setWindowTitle("QTimeEdit")
        self.resize(200, 150)
        
        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.time_edit = QTimeEdit(self)
        self.time_edit.setTime(QTime.currentTime())
        self.time_edit.timeChanged.connect(self.update_time)
        
        
        self.label = QLabel(f"Aktualny czas: {self.time_edit.time().toString("hh:mm:ss")}")
        
        layout.addWidget(self.time_edit)
        layout.addWidget(self.label)
        
        self.setLayout(layout)

    def update_time(self, time: QTime):
        self.label.setText(f"Aktualny czas: {time.toString("hh:mm:ss")}")
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
