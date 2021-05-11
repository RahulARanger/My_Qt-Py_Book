# https://doc.qt.io/archives/qt-4.8/threads-qobject.html#qobject-reentrancy

from PySide2 import QtWidgets
import threading

checking = QtWidgets.QApplication([])
counter = 0
test = QtWidgets.QLabel()


def counting():
    while True:
        global counter
        counter += 1
        test.setText(str(counter))


test2 = threading.Thread(target=counting)
test2.start()

test.show()
checking.exec_()
