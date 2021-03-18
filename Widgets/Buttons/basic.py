from PyQt5 import QtWidgets
import sys


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = QtWidgets.QWidget(windowTitle='QPushButtons')
        self.button = QtWidgets.QPushButton(self.window,
                                            text='Push Me',
                                            toolTip='Button'
                                            )
        self.toggleButton = QtWidgets.QPushButton(toolTip='Toggle button',
                                                  text='Toggle Me',
                                                  checkable=True, checked=True)
        self.toggleButton.show()
        self.button.show()
        self.window.show()


test().exec()
