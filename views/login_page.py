# views/login_page.py
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from models.database import Session, User

class LoginPage(QWidget):
    def __init__(self, on_login_success, parent=None):
        super(LoginPage, self).__init__(parent)
        self.on_login_success = on_login_success
        self.setup_ui()

    def setup_ui(self):
        # Container for the login form with styling
        container = QFrame(self)
        container.setObjectName("loginContainer")
        container.setStyleSheet("""
            QFrame#loginContainer {
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 10px;
                padding: 20px;
            }
        """)

        # Layout for the container
        container_layout = QVBoxLayout(container)
        container_layout.setSpacing(15)

        # Title label
        title_label = QLabel("Welcome to Hotel App")
        title_label.setFont(QFont("Helvetica", 20, QFont.Bold))
        title_label.setStyleSheet("color: #333;")
        title_label.setAlignment(Qt.AlignCenter)

        # Username components
        self.username_label = QLabel("Username:")
        self.username_edit = QLineEdit()
        self.username_edit.setPlaceholderText("Enter your username")
        self.username_edit.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)

        # Password components
        self.password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.setPlaceholderText("Enter your password")
        self.password_edit.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)

        # Create login and cancel buttons with styling
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)

        # Connect buttons to functions
        self.login_button.clicked.connect(self.handle_login)
        self.cancel_button.clicked.connect(self.handle_cancel)

        # Layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.cancel_button)

        # Add widgets to container layout
        container_layout.addWidget(title_label)
        container_layout.addWidget(self.username_label)
        container_layout.addWidget(self.username_edit)
        container_layout.addWidget(self.password_label)
        container_layout.addWidget(self.password_edit)
        container_layout.addLayout(button_layout)

        # Main layout for the login page
        main_layout = QVBoxLayout(self)
        main_layout.addStretch()
        main_layout.addWidget(container, 0, Qt.AlignCenter)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def handle_login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        session = Session()
        user = session.query(User).filter_by(username=username).first()
        if user and user.password == password:
            self.on_login_success()  # Switch to menu page
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")

    def handle_cancel(self):
        self.username_edit.clear()
        self.password_edit.clear()
