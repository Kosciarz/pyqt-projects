from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QDateEdit
from PyQt6.QtCore import Qt, QDate

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        
    def init_UI(self):
        self.setWindowTitle("QDateEdit")
        self.resize(200, 150)
        
        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.date_edit = QDateEdit(self)
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        self.date_edit.dateChanged.connect(self.update_date)
        
        self.label = QLabel(f"Dzisiaj jest {self.date_edit.date().toString("dd.MM.yyyy")}")
        
        layout.addWidget(self.date_edit)
        layout.addWidget(self.label)
        
        self.setLayout(layout)
        
    def update_date(self, date: QDate):
        self.label.setText(f"Dzisiaj jest {date.toString("dd.MM.yyyy")}")
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
    