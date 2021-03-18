from PyQt5 import QtWidgets


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='QInputDialog')
        self.layout = QtWidgets.QHBoxLayout()
        # returns the tuple (value,boolean value) boolean value says whether user has choosen ok or cancel button (
        # ok-TRue and vice versa)
        f1 = lambda x=True: print(
            QtWidgets.QInputDialog.getInt(self.window, 'Get Integer', 'Select Some Integer', 69, -69420, 69420, 69))
        f2 = lambda x=True: print(
            QtWidgets.QInputDialog.getDouble(self.window, 'Get Floating Values', 'Select Some Decimal', 69.0, 0, 69.69,
                                             2))
        f3 = lambda x=True: print(QtWidgets.QInputDialog.getText(self.window, 'Single Line Text', 'Enter SomeThing'))
        f4 = lambda x=True: print(
            QtWidgets.QInputDialog.getMultiLineText(self.window, 'MultiLine Text', 'Some Some Lines of Text'))
        f5 = lambda x=True: print(
            QtWidgets.QInputDialog.getItem(self.window, 'Select', 'Select From List', ['Orange', 'Red', 'Green'],
                                           editable=False))
        self.integer = QtWidgets.QPushButton(self.window, text='Integer', clicked=f1)
        self.float = QtWidgets.QPushButton(self.window, text='Float', clicked=f2)
        self.line = QtWidgets.QPushButton(self.window, text='Text', clicked=f3)
        self.multiline = QtWidgets.QPushButton(self.window, text='MultiLine Text', clicked=f4)
        self.list = QtWidgets.QPushButton(self.window, text='Item Selection', clicked=f5)
        self.window.setLayout(self.layout)
        self.layout.addWidget(self.integer)
        self.layout.addWidget(self.float)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.multiline)
        self.layout.addWidget(self.list)
        self.window.show()


test().exec()
