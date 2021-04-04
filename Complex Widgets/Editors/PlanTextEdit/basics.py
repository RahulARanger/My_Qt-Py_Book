from PyQt5 import QtWidgets


class Testing(QtWidgets.QPlainTextEdit):
    def __init__(self, parent):
        super().__init__(parent)


class Show_This(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.editor = Testing(self)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.editor)


test = QtWidgets.QApplication([])
case = Show_This()
case.show()
test.exec()
