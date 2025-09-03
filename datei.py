import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rechner")
        self.resize(300, 400)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.masterLayout = QVBoxLayout()
        self.Qline = QLineEdit(self)
        self.masterLayout.addWidget(self.Qline)

        self.layout2 = QGridLayout()
        self.buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '3', '2', '1', '*',
            '.', '0', '=', '/'
        ]

        row, col = 0, 0
        for i in self.buttons:
            button = QPushButton(i)
            self.layout2.addWidget(button, row, col)
            col += 1
            if col > 3:
                row += 1
                col = 0

        self.masterLayout.addLayout(self.layout2)
        centralWidget.setLayout(self.masterLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())