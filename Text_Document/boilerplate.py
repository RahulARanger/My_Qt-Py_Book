from PyQt5 import QtWidgets
class Editor(QtWidgets.QPlainTextEdit):
    def __init__(self,parent):
        super().__init__(parent)
        
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Editor with Cursor')
        self.app=Editor(self.window)
        self.app.move(50,50)
        self.window.show()
        
test().exec()