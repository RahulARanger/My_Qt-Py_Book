from PyQt5 import QtWidgets, QtCore, QtGui
import os

# Refer this for the item flags: https://doc.qt.io/qt-5/qt.html#ItemFlag-enum
class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget()
        self.testwidget = QtWidgets.QListWidget(self.window)
        os.chdir('..')
        self.testwidget.addItems(os.listdir(os.getcwd()))
        for i in range(self.testwidget.count()):
            self.testwidget.item(i).setFlags(self.testwidget.item(i).flags() | QtCore.Qt.ItemIsEditable) # ! use pipes for seperating multiple flags
        self.testwidget.move(10, 10)
        self.window.show()
store = Test()
store.exec()