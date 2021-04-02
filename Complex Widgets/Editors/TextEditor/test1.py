from PyQt5 import QtWidgets, QtCore, QtGui
import os


class Editor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mb = self.menuBar()
        self.file = QtWidgets.QMenu("file", self)
        self.saveas = QtWidgets.QAction(self.file)
        self.save = QtWidgets.QAction(self.file)

        self.editor = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.editor)
        self.saved = None
        self.setMenuBarThing()

    def setMenuBarThing(self):
        self.save.setText("save")
        self.save.triggered.connect(self.saveThis)
        self.saveas.setText("save as")
        self.saveas.triggered.connect(self.saveAsThis)
        self.file.addAction(self.save)
        self.save.setShortcut("Ctrl+S")
        self.saveas.setShortcut("Ctrl+Shift+S")
        self.file.addAction(self.saveas)
        self.mb.addMenu(self.file)

    def saveThis(self):
        if self.saved is None: return self.saveAsThis()
        with open(self.saved, 'w') as hand:
            hand.write(self.editor.toPlainText())

    def saveAsThis(self):
        result = QtWidgets.QFileDialog.getSaveFileName(self, "Save as", os.getcwd(),
                                                       "python files (*.py) ;; text files (*.txt)")
        if result[-1] != '':
            self.saved = result[0]
            return self.saveThis()

    def start(self):
        self.show()


class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.app = Editor()
        self.app.start()


store = Test()
store.exec()
