import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

        self.button.clicked.connect(self.onButtonClick)

        self.count_clicks = 0


    def initUI(self):

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Example 2')

        self.button = QtWidgets.QPushButton(self)
        self.button.move(130, 130)
        self.button.resize(40, 40)

        self.show()

    def onButtonClick(self):
        self.count_clicks += 1
        self.button.setText(str(self.count_clicks))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())