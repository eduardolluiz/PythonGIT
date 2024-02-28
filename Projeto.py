import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5 import QtCore

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projeto Python")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: gray;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout para o botão
        layout = QVBoxLayout(self.central_widget)

        # Criar botão
        button = QPushButton("Botão")
        layout.addWidget(button, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)

        # Adicionar margem e preenchimento (padding) ao botão
        button.setContentsMargins(10, 10, 10, 10)

        # Definir estilo do botão
        button.setStyleSheet("background-color: white; padding: 15px;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
