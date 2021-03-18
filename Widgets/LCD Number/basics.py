from PyQt5 import QtCore, QtWidgets, QtCore


# More info: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLCDNumber.html

class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("LCD Number")
        self.window.setLayout(QtWidgets.QVBoxLayout())
        self.test_on = QtWidgets.QLCDNumber(1, self.window)  # number indicates the max number of the digits
        self.test_on.setDigitCount(6)  # for modifying the max digit count
        self.increase = QtWidgets.QPushButton(self.window, text="increase")
        self.increase.clicked.connect(self.increase_num)
        self.test_on.setSegmentStyle(QtWidgets.QLCDNumber.Flat)

        # we can also use hex or oct mode

        self.test_on.setOctMode()
        self.window.layout().addWidget(self.test_on)
        self.window.layout().addWidget(self.increase)

        self.window.show()

    def increase_num(self):
        self.test_on.display(self.test_on.intValue() + 1)
        self.test_on.setBinMode()
        print(self.test_on.value())


testing = Test()
testing.exec()
