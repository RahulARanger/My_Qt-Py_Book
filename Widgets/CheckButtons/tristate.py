from PyQt5 import QtWidgets


class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='QCheckButton')
        self.checkbutton = QtWidgets.QCheckBox(self.window, toolTip='CheckBox', text='Check This')
        self.checkbutton.setTristate(True)  # for setting tristate for the checkbox
        self.window.show()
        self.checkbutton.show()
        self.checkbutton.setCheckState(2)  # 2 for tick and 1 for square and 0 for empty
        print(self.checkbutton.checkState())  # to print the selected choice


Test().exec()
