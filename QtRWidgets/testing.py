from QtRWidgets import *
from PyQt5 import QtWidgets

class testing(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget()
        self.scrollarea=QtWidgets.QScrollArea(self.window)
        self.scrollarea.setWidget(QtWidgets.QFrame())
        self.scrollarea.setWidgetResizable(True)
        self.window.show()
testing().exec()