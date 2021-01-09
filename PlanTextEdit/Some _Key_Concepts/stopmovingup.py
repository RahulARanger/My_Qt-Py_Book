from PyQt5 import QtWidgets,QtGui,QtCore
class Editor(QtWidgets.QPlainTextEdit):
    def __init__(self,parent):
        super().__init__(parent)        
    def keyPressEvent(self,event):
        if event.key()==QtCore.Qt.Key_Up: pass
        super().keyPressEvent(event)
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Editor with Cursor')
        self.app=Editor(self.window)
        self.app.move(50,50)
        self.window.show()
        
a=test()
a.exec()