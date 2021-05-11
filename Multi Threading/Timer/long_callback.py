from PySide2 import QtWidgets, QtCore
import time


class Test(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setText("Wait for it")
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(
            self.check
        )
        self.timer.start()

    def check(self):
        time.sleep(10)  # some big process
        self.setText("Did u wait for that long? expecting something, sorry no nuke codes!")


# will get stuck again
# This is the disadvantage of the QTimer
# This is because QTimer can't handle heavy tasks

check = QtWidgets.QApplication([])
test = Test()
test.show()
check.exec_()
