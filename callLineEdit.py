import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QApplication

from lay import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        #self.ui = Ui_Dialog()
        #self.ui.setupUi(self)
        self.ui =  uic.loadUi("lay.ui", self)
        self.ui.buttonClickMe.clicked.connect(self.dispmessage)
        self.show()
    def dispmessage(self):
        self.ui.labelResponse.setText("Hello"+" "+ self.ui.lineEditName.text())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())