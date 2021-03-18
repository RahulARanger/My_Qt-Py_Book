from PyQt5 import QtWidgets


class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='QCheckButton')
        self.checkbutton = QtWidgets.QCheckBox(self.window, toolTip='CheckBox', text='Check This')

        self.window.show()
        self.checkbutton.show()


Test().exec()
