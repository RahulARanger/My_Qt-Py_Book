from PySide2 import QtWidgets, QtCore, QtGui


class Test(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout())
        self.history = []
        self.enter = QtWidgets.QLineEdit(self)
        self.back, self.front = QtWidgets.QToolButton(self), QtWidgets.QToolButton(self)
        self.rows = [
            QtWidgets.QHBoxLayout()
            for _ in "..."
        ]
        self.view = QtWidgets.QListWidget(self)
        self.arrange()

    def arrange(self):
        self.back.setText("back")
        self.front.setText("front")

        [self.layout().addLayout(_) for _ in self.rows]
        self.rows[0].addWidget(self.back)
        self.rows[0].addWidget(self.front)
        self.rows[1].addWidget(self.view)
        self.rows[2].addWidget(self.enter)


testing = QtWidgets.QApplication([])
test = Test()
test.show()
testing.exec_()
