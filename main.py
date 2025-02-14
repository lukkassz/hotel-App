# main.py
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from views.main_window import MainWindow 

def main():
    app = QApplication(sys.argv)
    window = MainWindow() # Creates a window with login and menu pages
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
