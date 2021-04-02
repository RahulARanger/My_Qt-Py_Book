from PyQt5 import QtGui
from PyQt5 import QtWidgets
import re


class Validator(QtGui.QValidator):
    def __init__(self):
        super().__init__()

    def validate(self, string, index):
        print(self)
        print(string, index)  # String: text inside the widget and index is the latest updated index (starts from 1)
        result = re.findall(r'[0-9]', string)
        state = QtGui.QValidator.Acceptable
        if len(result) > 6:
            state = QtGui.QValidator.Invalid
        elif len(result) == 6:
            state = QtGui.QValidator.Intermediate
        # ! if the state is invalid then the changes are not accepted
        return state, string, index  # state,string and then the index


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='Validator')
        self.entry = QtWidgets.QLineEdit(self.window, toolTip='Entry', clearButtonEnabled=True)
        self.entry.setValidator(Validator())
        self.layout = QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.layout.addWidget(self.entry)
        self.window.show()


test().exec_()
