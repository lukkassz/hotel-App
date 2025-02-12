# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from views.login import LoginDialog  # Adjust the import path if necessary

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotel App")
        self.setGeometry(100, 100, 800, 600)  # Position and size

def main():
    app = QApplication(sys.argv)

    # Show the login dialog first
    login_dialog = LoginDialog()
    if login_dialog.exec_() == QDialog.Accepted:
        # If login is successful, show the main window
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    else:
        # Exit the application if login is canceled or fails
        sys.exit()

if __name__ == '__main__':
    main()
