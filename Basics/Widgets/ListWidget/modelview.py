
from PyQt5 import QtCore, QtGui, QtWidgets
import os, random
# custom models helps us to have sync between the data views/ any widgets

# QStringListModel() is the Model Classes for the QComboBox() and QListView()

# TODO: try modifying the items and press check how view and model automatically interact with each other

class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget()
        os.chdir('..')
        self.listview = QtWidgets.QListView(self.window)
        self.pointer = os.listdir(os.getcwd())
        self.listmodel = QtCore.QStringListModel(self.pointer)
        self.folder = QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'folder.png'))

        self.addMe = QtWidgets.QPushButton(self.window, text = 'Check', clicked = lambda x = True: print(self.listmodel.stringList()) )
        self.listview.setModel(self.listmodel)
        self.__modifylistview()
        self.listview.move(10, 10)
        self.addMe.move(100,300)
        self.window.show()

    def __modifylistview(self):
        self.listview.setMovement(QtWidgets.QListView.Free)
        self.listview.setViewMode(QtWidgets.QListView.IconMode)



store = Test()
store.exec()
