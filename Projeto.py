import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl, Qt  # Adicionando a importação de Qt

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
        button = QPushButton("Abrir Link")
        layout.addWidget(button, alignment=Qt.AlignBottom | Qt.AlignRight)  # Use Qt.Align* em vez de QtCore.Qt.Align*

        # Adicionar margem e preenchimento (padding) ao botão
        button.setContentsMargins(10, 10, 10, 10)

        # Definir estilo do botão
        button.setStyleSheet("background-color: white; padding: 15px;")

        # Conectar sinal clicked do botão à função openLink
        button.clicked.connect(self.openLink)

    def openLink(self):
        url = "https://www.twitch.tv/nako"  # Coloque aqui o link que deseja abrir
        QDesktopServices.openUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
