from PyQt5 import QtWidgets
import sys
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window=QtWidgets.QWidget(windowTitle='QLIneEdit')
        self.entry=QtWidgets.QLineEdit(self.window,text='Edit this Line',toolTip='Entry Box')
        self.entrywithph=QtWidgets.QLineEdit(placeholderText='Enter the Text',toolTip='With Place Holder text')
        self.limit=QtWidgets.QLineEdit(placeholderText='Enter text',maxLength=100)
        self.clear=QtWidgets.QLineEdit(placeholderText='clear this',clearButtonEnabled=True,toolTip='With Clear Button')
        self.clear.show()
        self.limit.show()
        self.entrywithph.show()
        self.entry.show()
        self.grabInfo()
        self.setThem()
        self.window.show()
    def grabInfo(self):
        # would be meaningful with the events
        self.entry.text()
    def setThem(self):
        self.entry.setText('Now Edit This')
test().exec()