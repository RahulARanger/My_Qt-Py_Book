# TODO: here we directly use the xml file rather than the python file

from PyQt5 import uic, QtWidgets

class1, class2 = uic.loadUiType('Calculator\\try2.ui')
print(type(class1), class1, class2, type(class2))


class Calcu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.object_ = class1()
        self.object_.setupUi(self)
        self.show()


# extra code for execution
app = QtWidgets.QApplication([])
a = Calcu()
# a.show()
app.exec_()
