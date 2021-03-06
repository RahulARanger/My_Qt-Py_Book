from PyQt5 import QtWidgets, QtCore


# ! SIGNALS and SLOTS may return some values but they can't be accessed
class signals(QtCore.QObject):
    showinfo = QtCore.pyqtSignal([], [bool])
    # can accept slot that takes no arguments or the one with bool argument

    def __init__(self):
        super().__init__()
        self.__privates1 = ['a', 'b']
        self.__privates2 = ['c', 'd']
        self.showinfo.connect(self.show1)
        self.showinfo[bool].connect(self.show2)

    def manual(self, wht=None):
        if wht is None:
            self.showinfo.emit()
            return None  # ! remains same as usual
        elif type(wht) == bool:
            return self.showinfo[bool].emit(wht)

    @QtCore.pyqtSlot()
    def show1(self):
        print('showed 1')
        return self.__privates2

    @QtCore.pyqtSlot(bool)
    def show2(self, wht):
        print('showed 2')
        return self.__privates1


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='Overriding Signals')
        self.info = signals()
        self.lb = QtWidgets.QLabel(self.window, text='Direct')
        self.lb2 = QtWidgets.QLabel(self.window, text='InDirect')

        self.bt = QtWidgets.QTextEdit(self.window, textChanged=self.info.showinfo)
        self.bt2 = QtWidgets.QPushButton(self.window, text='private1', clicked=self.info.showinfo)
        self.bt3 = QtWidgets.QTextEdit(self.window,
                                       textChanged=lambda: self.accessdata(lambda x: self.info.manual(), []))
        self.bt4 = QtWidgets.QPushButton(self.window, text='private2',
                                         clicked=lambda xy: self.accessdata(lambda x: self.info.manual(x), xy))

        self.window.setLayout(QtWidgets.QVBoxLayout())
        self.window.layout().addWidget(self.lb)
        self.window.layout().addWidget(self.bt)
        self.window.layout().addWidget(self.bt2)
        self.window.layout().addWidget(self.lb2)
        self.window.layout().addWidget(self.bt3)
        self.window.layout().addWidget(self.bt4)
        self.window.show()

    def accessdata(self, function, *args):
        print(function([]))  # ! None


test().exec()
