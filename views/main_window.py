# views/main_window.py
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QStackedWidget,
    QFrame, QGraphicsDropShadowEffect
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from views.animated_button import AnimatedButton
from views.login_page import LoginPage

class MenuPage(QWidget):
    def __init__(self, parent=None):
        super(MenuPage, self).__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        # Set a subtle horizontal gradient as the background
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #f8f9fa, stop:1 #e9ecef
                );
            }
        """)

        # Create a central container for the menu with rounded corners
        container = QFrame(self)
        container.setObjectName("menuContainer")
        container.setStyleSheet("""
            QFrame#menuContainer {
                background-color: white;
                border-radius: 20px;
                padding: 40px;
                border: 1px solid #dcdcdc;
            }
        """)

        # Apply a drop shadow effect to the container
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setXOffset(0)
        shadow.setYOffset(10)
        shadow.setColor(Qt.gray)
        container.setGraphicsEffect(shadow)

        # Layout for the container
        container_layout = QVBoxLayout(container)
        container_layout.setAlignment(Qt.AlignCenter)
        container_layout.setSpacing(30)

        # Title label with modern font and dark color
        title_label = QLabel("Hotel App Menu")
        title_label.setFont(QFont("Segoe UI", 36, QFont.Bold))
        title_label.setStyleSheet("color: #333333;")
        title_label.setAlignment(Qt.AlignCenter)
        container_layout.addWidget(title_label)

        # Create animated menu buttons
        btn_create = AnimatedButton("Create Reservation")
        btn_edit = AnimatedButton("Edit Reservation")
        btn_delete = AnimatedButton("Delete Reservation")
        btn_list = AnimatedButton("List Reservations")

        # Enhanced button style with gradient background and modern typography
        button_style = """
            QPushButton {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #0062E6, stop:1 #33AEFF
                );
                color: white;
                border: none;
                border-radius: 10px;
                padding: 15px;
                font-size: 20px;
                font-family: 'Segoe UI';
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #0051bf, stop:1 #2f98e0
                );
            }
        """
        for btn in [btn_create, btn_edit, btn_delete, btn_list]:
            btn.setStyleSheet(button_style)
            btn.setMinimumHeight(60)
            container_layout.addWidget(btn)

        # Main layout centers the container vertically
        main_layout = QVBoxLayout(self)
        main_layout.addStretch()
        main_layout.addWidget(container, alignment=Qt.AlignCenter)
        main_layout.addStretch()

        # Connect buttons to functions
        btn_create.clicked.connect(self.create_reservation)
        btn_edit.clicked.connect(self.edit_reservation)
        btn_delete.clicked.connect(self.delete_reservation)
        btn_list.clicked.connect(self.list_reservations)

    def create_reservation(self):
        print("Creating reservation...")

    def edit_reservation(self):
        print("Editing reservation...")

    def delete_reservation(self):
        print("Deleting reservation...")

    def list_reservations(self):
        print("Listing reservations...")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Hotel App")
        self.setFixedSize(1024, 768)  # Fixed window size
        self.stack = QStackedWidget()  # Container for multiple pages
        self.setCentralWidget(self.stack)
        self.init_ui()

    def init_ui(self):
        # Create the login page and pass the callback to switch pages
        self.login_page = LoginPage(self.show_menu)
        self.menu_page = MenuPage()

        # Add pages to the stack
        self.stack.addWidget(self.login_page)  # index 0: login page
        self.stack.addWidget(self.menu_page)     # index 1: menu page

        # Start with the login page
        self.stack.setCurrentIndex(0)

    def show_menu(self):
        # Switch to the menu page after a successful login
        self.stack.setCurrentIndex(1)
