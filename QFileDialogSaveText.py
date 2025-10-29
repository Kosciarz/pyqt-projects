from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QFileDialog, QVBoxLayout

import sys

from pathlib import Path

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDiloag save text")
        self.resize(300, 200)
        
        layout = QVBoxLayout(self)
        
        self.text_edit = QTextEdit(self)
        button = QPushButton("Zapisz do pliku", self)
        button.clicked.connect(self.select_file)
        
        layout.addWidget(self.text_edit)
        layout.addWidget(button)
        self.setLayout(layout)
    
    
    def select_file(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Wybierz plik",
            "C:/Users/barto",
            "Text files (*.txt);;All files (*)"
        )
        if not filename:
            return
        
        if not filename.endswith("txt"):
            filename += ".txt"
            
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.text_edit.toPlainText())
        
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
        
        
if __name__ == "__main__":
    main()
    