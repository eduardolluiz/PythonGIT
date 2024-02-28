import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projeto Python")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: gray;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())