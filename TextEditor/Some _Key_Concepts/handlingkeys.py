from PyQt5 import QtWidgets,QtCore,QtGui
class editor(QtWidgets.QTextEdit):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.installEventFilter(self) # 1. install event filter
    def eventFilter(self,object,event):  # 2 . override this function
        if event.type()==QtCore.QEvent.KeyPress:
            if event.key()==QtCore.Qt.Key_Return:  # find codes for the keys in https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html
                print('You Pressed Enter')
        return super().eventFilter(object,event)
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        a=editor()
        a.show()
        self.exec()
test()