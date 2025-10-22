from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel, QPushButton

import sys

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.show()
        
    def init_UI(self):
        self.setWindowTitle("Login Form")
        
        layout = QFormLayout(self)
        self.login_input = QLineEdit(self)
        self.password_input = QLineEdit(self)
        layout.addRow(QLabel("Login:"), self.login_input)
        layout.addRow(QLabel("Password:"), self.password_input)
        
        self.login_button = QPushButton("Zatwierdź", self)
        self.login_button.clicked.connect(self.handle_login)
        self.close_button = QPushButton("Zamknij", self)
        self.close_button.clicked.connect(self.close)
        
        layout.addRow(self.login_button, self.close_button)
        
        self.setLayout(layout)
        
    def handle_login(self):
        login = self.login_input.text()
        password = self.password_input.text()
        if not login:
            print("Proszę podać login")
        elif not password:
            print("Proszę podać hasło")
        else:
            print(f"Login: {login}, Hasło: {password}")
        
    def close(self):
        QApplication.quit()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = LoginForm()
    sys.exit(app.exec())