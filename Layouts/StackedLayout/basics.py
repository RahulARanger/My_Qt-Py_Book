from PyQt5 import QtWidgets


class Page(QtWidgets.QWidget):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.widget = QtWidgets.QLabel(self, text=text)
        self.widget.move(50, 50)


# * For switching b/w widgets in stackedlayout we can use any widget (not just combobox as used here)
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='StackedLayout')
        self.window.setLayout(QtWidgets.QHBoxLayout())
        self.leftframe = QtWidgets.QFrame(self.window)
        self.window.layout().addWidget(self.leftframe)
        self.rightframe = QtWidgets.QFrame(self.window)
        self.window.layout().addWidget(self.rightframe)
        self.rightframe.setLayout(QtWidgets.QStackedLayout())
        [self.rightframe.layout().addWidget(Page(self.rightframe, text='This is the Page {}'.format(i))) for i in
         range(10)]
        self.leftframe.setLayout(QtWidgets.QVBoxLayout())
        self.selector = QtWidgets.QComboBox(self.leftframe)
        self.selector.addItems(['Page {}'.format(i) for i in range(6)])

        # this is the key point
        self.selector.currentIndexChanged.connect(self.rightframe.layout().setCurrentIndex)
        self.leftframe.layout().addWidget(self.selector)
        self.window.show()


test().exec()
