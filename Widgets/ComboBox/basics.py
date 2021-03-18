from PyQt5 import QtWidgets


class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='ComboBox')
        self.cbox = QtWidgets.QComboBox(self.window, toolTip='ComboBox',
                                        editable=True,
                                        currentData=2,
                                        insertPolicy=QtWidgets.QComboBox.InsertAtTop)
        self.cbox.addItem('display', 'store this')  # text to display, data to store
        self.cbox.addItem('b', 'oohoh')
        self.cbox.insertSeparator(2)  # adds the seperator (design purposes)
        self.cbox.addItem('a', 'have to watch anime')
        self.cbox.insertItem(2, 'custom', 'second pos')  # pos,text,data to store
        self.window.show()
        self.cbox.show()


Test().exec()
