from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QTextEdit, QToolBar, QDialog, QLabel, QVBoxLayout, QFileDialog, QStyle
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QSize

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini edytor")
        self.resize(500, 350)
        
        self.create_menu_bar()
        # self.create_tool_bar()
        self.create_icon_tool_bar()

        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.update_status_bar)
        self.setCentralWidget(self.text_edit)

        self.create_status_bar()
        

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&Plik")
        edit_menu = menu_bar.addMenu("&Edycja")
        help_menu = menu_bar.addMenu("&Pomoc")
        
        self.new_action = QAction("Nowy")
        self.new_action.setShortcut("Ctrl+N")
        self.new_action.triggered.connect(lambda: self.text_edit.clear())
        file_menu.addAction(self.new_action)
        
        self.open_action = QAction("Otwórz")
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.triggered.connect(self.open_document)
        file_menu.addAction(self.open_action)
        
        self.save_action = QAction("Zapisz jako")
        self.save_action.triggered.connect(self.save_document)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        
        self.quit_action = QAction("Zakończ")
        self.quit_action.triggered.connect(lambda: self.close())
        file_menu.addAction(self.quit_action)
        
        self.undo_action = QAction("Cofnij")
        self.undo_action.setShortcut("Ctrl+Z")
        self.undo_action.triggered.connect(lambda: self.text_edit.undo())
        edit_menu.addAction(self.undo_action)
        
        self.redo_action = QAction("Ponów")
        self.redo_action.setShortcut("Ctrl+Y")
        self.redo_action.triggered.connect(lambda: self.text_edit.redo())
        edit_menu.addAction(self.redo_action)
        edit_menu.addSeparator()
        
        self.cut_action = QAction("Wytnij")
        self.cut_action.setShortcut("Ctrl+X")
        self.cut_action.triggered.connect(lambda: self.text_edit.cut())
        edit_menu.addAction(self.cut_action)

        self.copy_action = QAction("Kopiuj")
        self.copy_action.setShortcut("Ctrl+C")
        self.copy_action.triggered.connect(lambda: self.text_edit.copy())
        edit_menu.addAction(self.copy_action)
        
        self.paste_action = QAction("Wklej")
        self.paste_action.setShortcut("Ctrl+V")
        self.paste_action.triggered.connect(lambda: self.text_edit.paste())
        edit_menu.addAction(self.paste_action)
        
        self.about_action = QAction("O programie")
        self.about_action.triggered.connect(self.show_program_information)
        help_menu.addAction(self.about_action)
        
        
    def create_tool_bar(self):
        tool_bar = QToolBar("ToolBar")
        tool_bar.setMovable(False)
        tool_bar.setIconSize(QSize(16, 16))
        self.addToolBar(tool_bar)
        tool_bar.addAction(self.new_action)
        tool_bar.addAction(self.open_action)
        tool_bar.addAction(self.save_action)
        tool_bar.addAction(self.undo_action)
        tool_bar.addAction(self.redo_action)
        
        
    def create_icon_tool_bar(self):
        tool_bar = QToolBar("ToolBar")
        tool_bar.setMovable(False)
        tool_bar.setIconSize(QSize(16, 16))
        self.addToolBar(tool_bar)
        
        style = self.style()
        
        self.new_action.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_FileDialogNewFolder))
        tool_bar.addAction(self.new_action)
        
        self.open_action.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_DialogOpenButton))
        tool_bar.addAction(self.open_action)
        
        self.save_action.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_DialogSaveButton))
        tool_bar.addAction(self.save_action)
        
        self.undo_action.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_ArrowLeft))
        tool_bar.addAction(self.undo_action)
        
        self.redo_action.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_ArrowRight))
        tool_bar.addAction(self.redo_action)
        
    
    def create_status_bar(self):
        self.status_bar = self.statusBar()
        self.word_count = QLabel("Ilość słów: 0")
        self.letter_count = QLabel("Ilość liter: 0")
        self.status_bar.addWidget(self.word_count)
        self.status_bar.addWidget(self.letter_count)
    
    
    def update_status_bar(self):
        text = self.text_edit.toPlainText()
        self.word_count.setText(f"Ilość słów: {len(text.split(" "))}")
        self.letter_count.setText(f"Ilość liter: {len(text)}")
    
        
    def show_program_information(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("O programie")
        
        dialog_label = QLabel("""Mini edytor
Prosty edytor tekstu z podstawowymi funkcjami
Wersja 1.1
(c) 2025 by Me"""
        )
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(dialog_label)
        dialog.setLayout(dialog_layout)
        dialog.exec()
        
    
    def open_document(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Wybierz plik",
            "C:/Users",
            "Text files (*.txt);;All files (*)"
        )
        if filename:
            with open(filename, encoding="utf-8") as f:
                self.text_edit.setText(f.read())
    
    
    def save_document(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Wybierz plik",
            "C:/Users",
            "Text files (*.txt);;All files (*)"
        )
        if not filename:
            return
        if not filename.endswith(".txt"):
            filename += ".txt"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.text_edit.toPlainText())
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
