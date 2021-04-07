from PySide2 import QtWidgets, QtGui
import collect


class test(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        temp = QtGui.QFont("KiwiMaru-Regular")
        self.setFont(temp)
        print(temp.family(), QtGui.QFontInfo(temp).family())
        # first returns the custom family name
        # second returns the name of the font that is actually used (both are same means that custom font is used)

        temp = QtGui.QFontDatabase.addApplicationFont(":/fonts/Regular")
        if temp == -1:
            print("failed")

        temp = QtGui.QFont(QtGui.QFontDatabase.applicationFontFamilies(temp)[0])
        self.setFont(temp)

        print(temp.family(), QtGui.QFontInfo(temp).family())  # now both are same
        self.setText("This is just for testing")


note = QtWidgets.QApplication([])
check = test()
check.show()
note.exec_()
