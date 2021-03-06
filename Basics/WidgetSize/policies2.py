from PyQt5 import QtWidgets, QtCore


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='Size Policy')
        self.layout = QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.hint = QtCore.QSize(100, 100)
        self.numbers = [QtWidgets.QPushButton(text=str(i), toolTip='The Number is {}'.format(i)) for i in range(10)]
        self.sublayouts = [QtWidgets.QHBoxLayout() for i in range(4)]
        for i in self.sublayouts: self.layout.addLayout(i)
        for i in range(1, 10):
            self.sublayouts[i // 3 if i % 3 != 0 else i // 3 - 1].addWidget(self.numbers[i])
            self.numbers[i].setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.numbers[i].sizeHint = lambda: self.hint
            # * Try to modify the value in that SizePolicy to know the difference
            # ? expands equally on both sides (expanding)
            # ? minimum doesnt allow to less than the sizeHint or the default ones
            # ? Ignored forgets about the size hint and expands and shrinks as much as it can
            # ? maximum doesn't grow bigger than the default or sizeHint dimensions
            # ? fixed for the setting the sizeHint as the fixed dimeneions
        self.sublayouts[-1].addWidget(self.numbers[0])
        self.window.show()


test().exec()
