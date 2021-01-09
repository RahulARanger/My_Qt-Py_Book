from PyQt5 import QtWidgets,QtCore,QtGui
class Editor(QtWidgets.QPlainTextEdit):
    def __init__(self,parent):
        super().__init__(parent)
        self.cur=QtGui.QTextCursor(self.document())
        self.setDocumentTitle('Editor')
        self.setPlaceholderText('Press Enter to Print the text of the current Line')
    def keyPressEvent(self,event):
        if event.key()==QtCore.Qt.Key_Return:
            self.print_line()
        super().keyPressEvent(event)
    def print_line(self):
        print('recongized')
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Editor with Cursor')
        self.app=Editor(self.window)
        self.app.move(50,50)
        self.window.show()
        
test().exec()