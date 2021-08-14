from PySide2 import QtWidgets


class window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.open = QtWidgets.QPushButton(self, text='Open', clicked=self.openme)
        self.setCentralWidget(self.open)
        self.objects = []

    def openme(self):
        self.objects.append(window())
        self.objects[-1].show()

    def closeEvent(self, event):
        print('you really closed me')
        super().closeEvent(event)


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.main = window()
        self.main.show()


test().exec_()
