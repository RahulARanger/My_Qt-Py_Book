from PyQt5 import QtCore, QtWidgets


# why to follow this pattern refer: https://stackoverflow.com/a/65530516/12318454
class CustomWidget(QtCore.QObject):
    access = QtCore.pyqtSignal(str)  # first create the signal object (unbound signal)
    simple = QtCore.pyqtSignal()

    def __init__(self, parent):
        # arguments (as the types)
        super().__init__(parent)
        self.access.connect(self.show)  # second connect the signal to the slot
        self.__privates = ['private1', 'private2', 'private3']
        self.simple.connect(
            self.checkthis)  # (bound signal(object of the unbound signal (has the emit() destroy() and connect() but
        # the unbound doesn't have this)))

    def checkthis(self):
        print('can be connected by any other signals easily')
        return self.__privates

    @QtCore.pyqtSlot(str)
    def show(self, string):
        print('msg: {} and privates: {}'.format(string, self.__privates))
        return self.__privates

    def check(self, msg):
        print('used emit()')
        self.access.emit(msg)  # third emit it where ever u want


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='Custom Signals')
        self.bt = CustomWidget(self.window)
        self.layout = QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)

        self.bt2 = QtWidgets.QPushButton(self.window, text='manual',
                                         clicked=lambda x=True, y='message': self.bt.check(y))
        self.bt3 = QtWidgets.QPushButton(self.window, text='direct', clicked=self.bt.simple)
        self.layout.addWidget(self.bt2)
        self.layout.addWidget(self.bt3)
        self.window.show()


test().exec()
