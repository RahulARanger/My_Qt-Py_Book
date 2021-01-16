from PyQt5 import QtGui, QtWidgets, QtCore
import os


class ListContainer:
    def __init__(self, container=[], parent=None):
        super().__init__(parent)
        self.__container = []
        self.__length = 0

    def __getattr__(self, item):
        if item == 'length':
            return self.__length
        elif item == 'tuple':
            return tuple(self.__container)
        else:
            return super().__getattr__(item)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    store = ListContainer(range(100))
    store.show()
    app.exec()
