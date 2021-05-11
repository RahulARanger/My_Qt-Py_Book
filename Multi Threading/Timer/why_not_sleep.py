import time
from PySide2 import QtWidgets


class Test(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("Click me!")
        self.clicked.connect(self.print_tht)

    def print_tht(self):
        time.sleep(2000)  # wait for 2 seconds
        self.setText("printing this!")


check = QtWidgets.QApplication([])
test = Test()
test.show()
check.exec_()

# This creates the frozen GUI, and we have to force close that, to avoid this we have to implement
# Qt based methods
