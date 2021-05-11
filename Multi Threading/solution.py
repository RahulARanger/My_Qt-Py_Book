import threading
from PySide2 import QtWidgets, QtCore
import time


class Check(threading.Thread, QtCore.QObject):
    throw_this = QtCore.Signal(str)

    def __init__(self, parent):
        threading.Thread.__init__(self)
        QtCore.QObject.__init__(self, parent)
        self.counter = 0

    def run(self):
        while True:
            self.counter += 1
            self.throw_this.emit(str(self.counter))
            time.sleep(1)


testing = QtWidgets.QApplication([])
test = QtWidgets.QLabel()
test2 = Check(test)
test2.throw_this.connect(test.setText)
test2.start()
test.show()
testing.exec_()