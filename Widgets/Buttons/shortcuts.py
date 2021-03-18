from PyQt5 import QtWidgets, QtGui, QtCore
# QtGui is used for supporting GUI Widgets (for catching the keyboard events)
# QtCore has some important variables (here for identfying the keys)
import sys


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = QtWidgets.QWidget(windowTitle='QPushButton with shortcuts')
        self.button = QtWidgets.QPushButton(
            self.window,
            toolTip='Press Ctrl+a',
            text='Click me or press ctrl+a',
            shortcut=QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_A)  # More info about this is included in
            # README.md in this current working directory

        )
        self.button.show()
        self.window.show()


test().exec()
