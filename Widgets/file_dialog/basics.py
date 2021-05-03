from PySide2 import QtWidgets, QtCore
import os


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='QFileDialog')
        f1 = lambda x=True: print(
            QtWidgets.QFileDialog.getOpenFileName(self.window, 'Open File', QtCore.QDir.homePath(),
                                                  'python files (*.py) ;; ui files (*.ui)'))
        f2 = lambda x=True: print(QtWidgets.QFileDialog.getOpenFileNames(self.window, 'Open Files', os.getcwd(),
                                                                         'python files (*.py) ;; ui files (*.ui)'))
        f3 = lambda x=True: print(
            QtWidgets.QFileDialog.getSaveFileName(self.window, 'Save .py file', os.getcwd(), 'Python File (*.py)'))

        self.layout = QtWidgets.QHBoxLayout()
        self.openfile = QtWidgets.QPushButton(self.window, text='Open File', clicked=f1)
        self.openfiles = QtWidgets.QPushButton(self.window, text='Open Files', clicked=f2)
        self.savefile = QtWidgets.QPushButton(self.window, text='Save File',
                                              clicked=f3)  # ! doesnt actually save the file
        self.window.setLayout(self.layout)
        self.layout.addWidget(self.openfile)
        self.layout.addWidget(self.openfiles)
        self.layout.addWidget(self.savefile)
        self.window.show()


test().exec_()
