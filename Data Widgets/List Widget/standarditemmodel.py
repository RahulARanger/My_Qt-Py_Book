# standarditemmodel() has more options for the customization of the listview than the stringListModel() (not just for
# the listview() tho).

from PyQt5 import QtWidgets, QtCore, QtGui


class Test(QtWidgets.QApplication):
    def __init__(self):
        super()._init__([])
        self.window = QtWidgets.QWidget()
        
        self.window.show()


store = Test()
store.exec()
