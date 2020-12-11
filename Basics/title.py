from PyQt5 import QtWidgets
class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='') # implicit way
        self.window.setWindowTitle('Hello There') # explicit way
        print(self.window.windowTitle()) # in order to get the title of the window
        self.window.show()
a=Test()
a.exec()