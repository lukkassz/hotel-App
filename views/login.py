# views/login.py
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setWindowTitle("Login")
        self.setup_ui()

    def setup_ui(self):
        self.username_label = QLabel("Username:")
        self.username_edit = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.cancel_button = QPushButton("Cancel")

        self.login_button.clicked.connect(self.handle_login)
        self.cancel_button.clicked.connect(self.reject)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.cancel_button)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        from models.database import Session, User
        session = Session()

        user = session.query(User).filter_by(username=username).first()
        if user and user.password == password:
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")
