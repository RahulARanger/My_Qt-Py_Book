from PySide2 import QtWidgets, QtCore


class Test(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.setText(f"Counted: {self.count}")
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.count_it)
        self.timer.start()

    def count_it(self):
        self.count += 1
        self.setText(f"Counted: {self.count}")


check = QtWidgets.QApplication([])
test = Test()
test.show()
check.exec_()
