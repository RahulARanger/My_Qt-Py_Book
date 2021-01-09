from PyQt5 import QtWidgets

class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Setting Up Menu')
        self.mainwindow=QtWidgets.QMainWindow()
        self.mainwindow.setCentralWidget(self.mainwindow)
        self.setupMenu()
        self.mainwindow.show()
    def setupMenu(self):
        self.menu=self.mainwindow.menuBar() # * can also be created QtWidgets.QMenu()
        menu=QtWidgets.QMenu()
        print(self.mainwindow.actions())
test().exec()
        