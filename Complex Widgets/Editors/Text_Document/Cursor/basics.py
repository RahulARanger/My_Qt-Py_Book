from PyQt5 import QtWidgets,QtGui
class Editor(QtWidgets.QPlainTextEdit):
    def __init__(self,parent):
        super().__init__(parent)
        self.cur=QtGui.QTextCursor(self.document())
        self.setTextCursor(self.cur)
        self.count=0
        self.cursorPositionChanged.connect(self.test)
    def test(self,*args):
        print(args,self.count)
        self.count+=1
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Editor with Cursor')
        self.app=Editor(self.window)
        self.app.move(50,50)
        self.window.show()
        
a=test()
a.exec()