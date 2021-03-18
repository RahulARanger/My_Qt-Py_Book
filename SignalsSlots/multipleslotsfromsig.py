from PyQt5 import QtWidgets


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='Multiple Slots from a single Single')
        self.bt = QtWidgets.QPushButton(self.window, text='Push Me')
        self.bt.clicked.connect(self.first)
        self.bt.clicked.connect(self.second)
        self.bt.show()
        self.window.show()

    def first(self):
        print('called first function')

    def second(self):
        print('called second function')


test().exec()
