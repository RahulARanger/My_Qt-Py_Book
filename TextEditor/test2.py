import os

from PyQt5 import QtWidgets, QtCore


class Model(QtCore.QObject):
    # inherited QObject incase if we want to create some custom slots or signals

    def __init__(self):
        super().__init__()
        self.saved = None

    @QtCore.pyqtSlot(str)
    def saveThis(self, text):
        if self.saved is None:
            return self.saveThisAs(text)
        with open(self.saved, "w") as hand:
            hand.write(text)

    @QtCore.pyqtSlot(str)
    def saveThisAs(self, text):
        print('wht happened')
        result = QtWidgets.QFileDialog.getSaveFileName(self, "Save as", os.getcwd(),
                                                       "python files (*.py) ;; text files (*.txt)")
        if result[-1] != "":
            self.saved = result[0]
            return self.saveThis(text)


class View(QtWidgets.QTextEdit):
    def __init__(self, parent):
        super().__init__(parent)


class App(QtWidgets.QMainWindow, Model):
    def __init__(self):
        super().__init__()
        self.__viewpart = View(self)
        self.setCentralWidget(self.__viewpart)
        self.mb = self.menuBar()
        self.__setmenu()

    def __setmenu(self):
        self.file = QtWidgets.QMenu("file", self)
        self.save = QtWidgets.QAction(self.file)
        self.save.setText("save")
        self.save.setShortcut("Ctrl+S")
        self.save.triggered.connect(lambda: self.saveThis(self.__viewpart.toPlainText()))
        self.saveas = QtWidgets.QAction(self.file)
        self.saveas.setText("save as")
        self.saveas.setShortcut("Ctrl+Shift+S")
        self.saveas.triggered.connect(lambda: self.saveThisAs(self.__viewpart.toPlainText()))
        self.file.addAction(self.save)
        self.file.addAction(self.saveas)
        self.mb.addMenu(self.file)


class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.app = App()
        self.app.show()


store = Test()
store.exec()
