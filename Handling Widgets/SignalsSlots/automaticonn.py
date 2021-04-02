from PyQt5 import QtWidgets, QtCore


class test(QtWidgets.QWidget):
    def __init__(self):
        super().__init__(windowTitle='QtCore.QMetaObject.connectSlotsByName()')
        self.bt = QtWidgets.QPushButton(self, text='Push Me')
        self.bt.setObjectName('test')
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.bt)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    @QtCore.pyqtSlot()
    def on_test_clicked(self):
        print('You Pushed a button')


app = QtWidgets.QApplication([])
a = test()
app.exec()
